const numbers = [
    {"value": 9, "x": 10, "y": 5},
    {"value": 1, "x": 5, "y": 15},
    {"value": 2, "x": 15, "y": 10},
    {"value": 3, "x": 50, "y": 90},
    {"value": 4, "x": 50, "y": 50},
    {"value": 5, "x": 60, "y": 70},
    {"value": 6, "x": 80, "y": 20},
    {"value": 7, "x": 90, "y": 25},
    {"value": 8, "x": 10, "y": 23},
    {"value": 10, "x": 12, "y": 45},
]

const generateNumbers = (nums) => {
    const imgContainer = document.querySelector(".img-container");
    for(num of nums) {
        const number = document.createElement("div");
        number.className = "number";
        number.textContent = num["value"];
        number.style.top = num["y"] + "%";
        number.style.left = num["x"] + "%";
        imgContainer.appendChild(number);
    }
}

generateNumbers(numbers);