document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('station-search');
    const suggestionsDiv = document.getElementById('autocomplete-results');

    const handler = async () => {
        const query = searchInput.value.trim();

        if (query.length < 2) {
            suggestionsDiv.innerHTML = '';
            suggestionsDiv.style.display = 'none';
            return;
        }

        try {
            const response = await fetch(`${BASE_URL}api/search_stations.php?query=${query}`);
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
                        window.location.href = `stations/${station.code}`;
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
    };

    searchInput.addEventListener('input', handler);
    searchInput.addEventListener('click', handler);

    document.addEventListener('click', (event) => {
        if (!event.target.closest('#station-search-form')) {
            suggestionsDiv.innerHTML = '';
            suggestionsDiv.style.display = 'none';
        }
    });
});
