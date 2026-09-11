const form = document.getElementById("predictionForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const studentData = {
        study_hours: Number(document.getElementById("study_hours").value),
        attendance: Number(document.getElementById("attendance").value),
        previous_marks: Number(document.getElementById("previous_marks").value),
        assignments_completed: Number(
            document.getElementById("assignments_completed").value
        )
    };

    const response = await fetch("https://meachine-learning.onrender.com/", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(studentData)
    });

    const data = await response.json();

    result.textContent =
        `Predicted Score: ${data.predicted_score.toFixed(2)}`;
});