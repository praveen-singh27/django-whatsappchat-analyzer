// Fetch data from the 'monthly-timeline' API
fetch('/dashboard/busy-month/')
    .then(response => response.json())
    .then(timelineData => {
        var ctx = document.getElementById("busyMonthBarChart");
        var myBarChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: timelineData.labels,  // Months (e.g., "October-2024")
                datasets: [{
                    label: "Messages",
                    backgroundColor: "#4e73df",
                    hoverBackgroundColor: "#2e59d9",
                    borderColor: "#4e73df",
                    data: timelineData.messages  // Message count per month
                }]
            },
            options: {
                maintainAspectRatio: false,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    })
    .catch(error => console.error("Error fetching timeline data:", error));
