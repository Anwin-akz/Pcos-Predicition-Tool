document.getElementById("uploadForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    let formData = new FormData(this);

    fetch("/image_upload/", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
        }
    })
    .then(response => response.json())  // Convert response to JSON
    .then(data => {
        console.log("Received Data:", data);  // Debugging: Check response in console

        if (data.result) {
            let resultText = `<b>${data.result}</b><br><br>`;
            resultText += `<b>Severity Level:</b> ${data.severity}<br>`;

            // If PCOS is detected, show suggestions
            if (data.result === "PCOS Detected") {
                resultText += `<b>Suggested Management:</b> ${data.suggestion}<br>`;
            }

            document.getElementById("result-text").innerHTML = resultText;
            document.getElementById("popup").style.display = "flex";  // Show pop-up
        }
    })
    .catch(error => console.error("Error:", error));  // Handle errors
});

function closePopup() {
    document.getElementById("popup").style.display = "none";
}
