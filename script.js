document.addEventListener("DOMContentLoaded", () => {
  // --- Recommendation Logic ---
  const recButton = document.getElementById("rec-button");
  const recTitleInput = document.getElementById("rec-title");
  const recommendationsList = document.getElementById("recommendations-list");

  recButton.addEventListener("click", async () => {
    const title = recTitleInput.value;
    if (!title) {
      alert("Please enter a book title.");
      return;
    }

    try {
      // This is where we call our FastAPI back-end!
      const response = await fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: title }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();

      // Clear previous results
      recommendationsList.innerHTML = "";

      if (data.error) {
        recommendationsList.innerHTML = `<li>${data.error}</li>`;
      } else if (data.recommendations && data.recommendations.recommendations) {
        // Adjusting for the nested structure if it exists
        const books = data.recommendations.recommendations;
        books.forEach((book) => {
          const li = document.createElement("li");
          li.textContent = book;
          recommendationsList.appendChild(li);
        });
      }
    } catch (error) {
      console.error("Error fetching recommendations:", error);
      recommendationsList.innerHTML =
        "<li>Error fetching recommendations. Check console.</li>";
    }
  });

  // --- Prediction Logic ---
  const predForm = document.getElementById("pred-form");
  const predictionResult = document.getElementById("prediction-result");

  predForm.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent form from reloading the page

    const payload = {
      num_pages: parseInt(document.getElementById("num_pages").value),
      ratings_count: parseInt(document.getElementById("ratings_count").value),
      text_reviews_count: parseInt(
        document.getElementById("text_reviews_count").value
      ),
      publication_year: parseInt(
        document.getElementById("publication_year").value
      ),
      language_code: document.getElementById("language_code").value,
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      predictionResult.textContent = data.prediction;
    } catch (error) {
      console.error("Error fetching prediction:", error);
      predictionResult.textContent = "Error!";
    }
  });
});
