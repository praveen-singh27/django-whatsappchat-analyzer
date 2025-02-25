// Fetch data from the 'weekly-heatmap' API
fetch('/dashboard/weekly-heatmap/')
    .then(response => response.json())
    .then(heatmapData => {
        var ctx = document.getElementById("stackedBarChart");

        // X-axis: 24-hour time slots
        var hours = Array.from({ length: 24 }, (_, i) => `${i}:00 - ${i + 1}:00`);

        // Y-axis: Message count
        var days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
        
        // Assign a unique color to each day
        var colors = [
            "rgba(255, 99, 132, 0.7)",  // Monday
            "rgba(54, 162, 235, 0.7)",  // Tuesday
            "rgba(255, 206, 86, 0.7)",  // Wednesday
            "rgba(75, 192, 192, 0.7)",  // Thursday
            "rgba(153, 102, 255, 0.7)", // Friday
            "rgba(255, 159, 64, 0.7)",  // Saturday
            "rgba(0, 128, 128, 0.7)"    // Sunday
        ];

        // Initialize datasets for each day of the week
        var datasets = days.map((day, index) => ({
            label: day,
            backgroundColor: colors[index],
            borderColor: colors[index].replace("0.7", "1"), // Darker border
            borderWidth: 1,
            data: Array(24).fill(0), // 24-hour time slots
            stack: "stack1"
        }));

        // Populate datasets with heatmap data
        heatmapData.forEach(item => {
            let dayIndex = days.indexOf(item.y);
            if (dayIndex !== -1) {
                datasets[dayIndex].data[item.x] = item.v;
            }
        });

        // Render the stacked bar chart
        var myStackedBarChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: hours, // 24-hour slots
                datasets: datasets
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                scales: {
                    x: { stacked: true, title: { display: true, text: "Time of Day" } },
                    y: { stacked: true, beginAtZero: true, title: { display: true, text: "Message Count" } }
                },
                plugins: {
                    legend: { display: true },
                    tooltip: { mode: "index", intersect: false }
                }
            }
        });
    })
    .catch(error => console.error("Error fetching heatmap data:", error));
