let cachedSchedule = [];
let cache = {};
const fetchStationDetails = async () => {
    const stationId = window.location.pathname.split('/').pop();
    console.log(`Station ID: ${stationId}`); // Debugging
    const stationName = document.getElementById("station-name")
    const scheduleSection = document.getElementById("schedule")
    try {
        const response = await fetch(`${BASE_URL}api/get_station.php?station_id=${stationId}`);
        const data = await response.json();

        if (data.success) {
            stationName.textContent = data.station.name; // Set station name
            return stationId; // Pass station ID to fetch schedule
        } else {
            stationName.textContent = 'Station not found.';
            scheduleSection.innerHTML = '<p>Unable to load station details.</p>';
            throw new Error(data.message);
        }
    } catch (error) {
        console.error('Error fetching station details:', error);
    }
};

const fetchThreadDetails = async (uid) => {
    try {
        const response = await fetch(`${BASE_URL}api/get_thread.php?uid=${uid}`);
        const data = await response.json();

        if (data.success) {
        
            return data.thread; 
        } else {
            throw new Error(data.message);
        }
    } catch (error) {
        console.error('Error fetching thread details:', error);
    }
};

const fetchCarrierDetails = async (code) => {
    try {
        const response = await fetch(`${BASE_URL}api/get_carrier.php?code=${code}`);
        const data = await response.json();

        if (data.success) {
        
            return data.carrier;
        } else {
            throw new Error(data.message);
        }
    } catch (error) {
        console.error('Error fetching carrier details:', error);
    }
};

const renderSchedule = async (schedule) => {
    const scheduleSection = document.getElementById("schedule");
    scheduleSection.innerHTML = ""; // Clear existing content

    if (!schedule || schedule.length === 0) {
        scheduleSection.innerHTML = "<p>Расписание недоступно для выбранных фильтров.</p>";
        return;
    }
    const eventType = document.getElementById("event_type").value;
    // Wait for all cards to be built before rendering
    const cards = await Promise.all(
        schedule.map(async (train) => {
            const card = document.createElement("div");
            card.classList.add("train-card");
            //console.log(formatDateInOriginalTimezone(train[eventType + "_time"]));
            //console.log(train[eventType + "_time"]);
            if(train[eventType+"_time"] !== null){
            
                //console.log(eventType);
                const time = train[eventType + "_time"].substring(11, 16)
                
                
                // Fetch thread and carrier details
                const thread = await fetchThreadDetails(train.uid);
                const carrier = await fetchCarrierDetails(train.carrier_code);

                const timeInTrip = parseInt(thread?.duration);
                card.innerHTML = `
                    <div class="train-time">
                        <div class="train-number">№ ${train.number}</div>
                        <div class="time">${time}</div>
                    </div>

                    <div class="train-route">
                        <div class="direction">${thread?.start} → ${thread?.end}</div>
                        <div class="duration">В пути: ${Math.floor(timeInTrip / 3600)}ч ${
                    (timeInTrip % 3600) / 60
                }м</div>
                    </div>

                    <div class="carrier">
                        ${carrier.logo !== null ? "<img src=" + carrier.logo + " alt=" + carrier.title + ">" : ""}
                        <span class="carrier-name">${carrier?.title || "Не указано"}</span>
                    </div>

                    <div class="transport-type">${train.transport_type === "train" ? "поезд" : "электричка"}</div>
                    ${train.transport_subtype !== null ? '<div class="transport-subtype">' + train.transport_subtype + "</div>" : ""}
                `;


                return card;
            }
        })
    );

    // Append cards in order
    cards.forEach((card) => scheduleSection.appendChild(card));
};


document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('station-search');
    const suggestionsDiv = document.getElementById('autocomplete-results');
    //console.log("123");
    handler = async () => {
        const query = searchInput.value.trim();

        if (query.length < 2) {
            suggestionsDiv.innerHTML = '';
            suggestionsDiv.style.display = 'none';
            return;
        }

        try {
            // Fetch suggestions from the server
            const response = await fetch(`${BASE_URL}api/search_stations.php?query=${encodeURIComponent(query)}`);
            const json = await response.json();
            const results = json.results;
            // Clear previous suggestions
            suggestionsDiv.innerHTML = '';

            if (results.length > 0) {
                results.forEach((station) => {
                    const suggestion = document.createElement('div');
                    suggestion.className = 'autocomplete-item';
                    suggestion.textContent = station.name;
                    suggestion.addEventListener('click', () => {
                        // Redirect to the station's page
                        window.location.href = `${station.code}`;
                    });
                    suggestionsDiv.appendChild(suggestion);
                });
                suggestionsDiv.style.display = 'block';
            } else {
                suggestionsDiv.style.display = 'none';
            }
        } catch (error) {
            console.error('Error fetching suggestions:', error);
        }
    }
    // Handle search input
    searchInput.addEventListener('input', handler);
    searchInput.addEventListener('click', handler);

    // Hide suggestions when clicking outside
    document.addEventListener('click', (event) => {
        if (!event.target.closest('.search-bar')) {
            suggestionsDiv.innerHTML = '';
            suggestionsDiv.style.display = 'none';
        }
    });
});



const fetchSchedule = async (stationId, date) => {
    const scheduleSection = document.getElementById("schedule");
    const loadingIndicator = document.getElementById("loading-indicator");

    // Show loading state
    scheduleSection.classList.add("loading");
    loadingIndicator.style.display = "flex";

    
    const eventType = document.getElementById("event_type");
    const transportType = document.getElementById("transport_type");

    
    const event = eventType?.value || "departure";
    const transport = transportType?.value;


    try {
        const response = await fetch(
            `${BASE_URL}api/fetch_schedule.php?station_id=${stationId}&date=${date}&event=${event}&transport_type=${transport}`
        );
        const data = await response.json();
        
        // Ensure the schedule is sorted by the event time (arrival_time or departure_time)
        
        if(data.success) {
            data.schedule = data.schedule.filter((a) => (a[event+"_time"] !== null));

            data.schedule = data.schedule.sort((a, b) => {
                const timeA = new Date(a[event + "_time"].substring(0, 19) + "Z");
                const timeB = new Date(b[event + "_time"].substring(0, 19) + "Z");
                
                // Compare the two times
                return timeA - timeB;
            });
            
            //console.log(data.schedule);
            cachedSchedule = data.schedule;
            cache[transport] = data.schedule;
            applyFilters();
        } else {
            scheduleSection.classList.remove("loading");
            scheduleSection.textContent = data.message;    
        }
    } catch (error) {
        console.error("Error fetching schedule data:", error);
        scheduleSection.innerHTML = "<p>Error loading schedule. Please try again.</p>";
    } finally {
        // Hide loading state
        scheduleSection.classList.remove("loading");
        loadingIndicator.style.display = "none";
    }
    
   
};

// Handle filter changes
const applyFilters = () => {
    const eventType = document.getElementById("event_type").value; // "departure" or "arrival"
    const transportType = document.getElementById("transport_type").value; // Transport type
    const hideLeft = document.getElementById("hide_left").checked; // Hide past events
    const labelHideLeft = document.getElementById("label_hide_left");
    eventType=='arrival'?labelHideLeft.textContent="Скрыть пришедшие":labelHideLeft.textContent="Скрыть ушедшие";
    const now = new Date();
    cachedSchedule = cache[transportType];
    //console.log(cache);
    // Filter the cached schedule
    const filteredSchedule = cachedSchedule.filter((train) => {
        
        if(train[eventType+"_time"] == null) {
            return false;
        }
        //console.log(train[eventType + "_time"].substring(0, 19));
        const eventTime = new Date(train[eventType + "_time"]);

        // Apply hide left filter
        if (hideLeft && eventTime < now) {
            return false;
        }

        // Apply transport type filter
        if (transportType !== "all" && train.transport_type !== transportType) {
            return false;
        }

        return true;
    });

    // Sort the filtered schedule
    filteredSchedule.sort((a, b) => {
        const timeA = new Date(a[eventType + "_time"].substring(0, 19) + "Z");
        const timeB = new Date(b[eventType + "_time"].substring(0, 19) + "Z");
        return timeA - timeB;
    });

    // Render the filtered and sorted schedule
    renderSchedule(filteredSchedule);
};

// Handle date change
const handleDateChange = (stationId) => {
    const datePicker = document.getElementById("date_picker");
    const date = datePicker?.value || new Date().toISOString().split("T")[0];
    
    //const transportType = document.getElementById("transport_type").value;
    fetchSchedule(stationId, date);
};

// Initialize filters and events
document.addEventListener("DOMContentLoaded", () => {
    const stationId = window.location.pathname.split("/").pop();

    // Fetch the schedule on initial load
    fetchStationDetails().then(() => {
        fetchSchedule(stationId, document.getElementById("date_picker").value);
    });
    
    const transport_type = document.getElementById("transport_type").value;
    // Attach event listeners to filters
    document.getElementById("filters").addEventListener("change", (event) => {
        if (event.target.id === "date_picker") {
            Object.keys(cache).forEach(key => delete cache[key]);
            handleDateChange(stationId); // Fetch new data only if the date changes
        } else if ((event.target.id==="transport_type" && cache.transport_type===undefined)) {
            handleDateChange(stationId);
        } 
        else {
            console.log(transport_type);
            console.log(cache);
            applyFilters(); // Apply filters on the cached data
        }
    });
});


// // Call fetch functions on page load
// fetchStationDetails().then((stationId) => {
//     fetchSchedule(stationId);
// });