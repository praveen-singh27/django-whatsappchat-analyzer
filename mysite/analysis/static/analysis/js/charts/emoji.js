// Fetch data from the 'emojis' API
fetch('/dashboard/emojis/')
    .then(response => response.json())
    .then(emojiData => {
        var ctx = document.getElementById("emojipiechart").getContext("2d");

        // We instantiate a new Chart instance and provide two arguments: 
        // the canvas element where the chart would be rendered and the options object.
        new Chart(ctx, {          
            type: "doughnut",
            data: {
                labels: emojiData.emoji,  // Use emoji as labels
                datasets: [{
                    label: "Emoji Frequency",
                    data: emojiData.emoji_count,  // Use counts as data
                    backgroundColor: [
                        'rgb(255, 99, 132)',   // Red
                        'rgb(54, 162, 235)',   // Blue
                        'rgb(255, 205, 86)',   // Yellow
                        'rgb(75, 192, 192)',   // Teal
                        'rgb(153, 102, 255)',  // Purple
                        'rgb(255, 159, 64)',   // Orange
                        'rgb(0, 204, 102)',    // Green
                        'rgb(204, 0, 204)',    // Magenta
                        'rgb(255, 153, 204)',  // Pink
                        'rgb(102, 102, 255)'   // Light Blue
                    ],
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: "right" }
                }
            }
        });
    })
    .catch(error => console.error("Error fetching emoji data:", error));
