document.addEventListener("DOMContentLoaded", function () {
    let chartInstance;
    const dropdown = document.getElementById("wordCountFilter");

    // Function to fetch and update chart
    function fetchAndRenderChart(limit = 10) {
        fetch('/dashboard/common-words/')
            .then(response => response.json())
            .then(wordData => {
                var ctx = document.getElementById("commonWordsChart").getContext("2d");

                // Extract words and their frequencies
                let labels = wordData.word.slice(0, limit);       // X-axis: Words (limit selection)
                let data = wordData.word_count.slice(0, limit);   // Y-axis: Word frequencies

                // Generate dynamic colors
                let backgroundColors = labels.map((_, i) => `rgba(${(i * 40) % 255}, ${(i * 80) % 255}, ${(i * 120) % 255}, 0.7)`);
                let borderColors = labels.map((_, i) => `rgba(${(i * 40) % 255}, ${(i * 80) % 255}, ${(i * 120) % 255}, 1)`);

                // Destroy previous chart if exists
                if (chartInstance) {
                    chartInstance.destroy();
                }

                // Create new bar chart
                chartInstance = new Chart(ctx, {
                    type: "bar",
                    data: {
                        labels: labels,
                        datasets: [{
                            label: "Word Frequency",
                            data: data,
                            backgroundColor: backgroundColors,
                            borderColor: borderColors,
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true,
                                title: { display: true, text: "Count" }
                            },
                            x: {
                                title: { display: true, text: "Words" }
                            }
                        },
                        plugins: {
                            legend: { display: false },
                            tooltip: { mode: "index", intersect: false }
                        }
                    }
                });
            })
            .catch(error => console.error("Error fetching common words data:", error));
    }

    // Event listener for dropdown change
    dropdown.addEventListener("change", function () {
        let selectedLimit = parseInt(dropdown.value, 10);
        fetchAndRenderChart(selectedLimit);
    });

    // Initial fetch with default value
    fetchAndRenderChart();
});
