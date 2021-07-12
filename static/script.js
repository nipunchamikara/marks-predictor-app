// Runs when the DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    update();
    const hours_element = document.querySelector("#hours");
    hours_element.oninput = function() {
        if (hours_element.value === "" || hours_element.value < 0) {
            hours_element.value = "0";
        // We are going to assume that a student can study for a maximum of 12 hours
        } else if (hours_element.value > 12) {
            hours_element.value = 12
        } else {
            hours_element.value = parseFloat(hours_element.value);
        }

        update();
    };
})

// Updates the predicted marks
function update() {
    const hours_element = document.querySelector("#hours");
    const marks_element = document.querySelector("#marks");

    // POST request to server
    fetch("/", {
        method: "POST",
        body: JSON.stringify({
            hours: hours_element.value
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        if (result["success"]) {
            marks_element.innerHTML = result["score"];
        }
    });
}