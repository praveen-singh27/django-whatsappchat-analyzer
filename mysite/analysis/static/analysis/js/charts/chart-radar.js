// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Radar Chart
var ctx = document.getElementById("myRadarChart");
var myRadarChart = new Chart(ctx, {
  type: 'radar',
  data: {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(78, 115, 223, 0.3)",  // Semi-transparent fill
      borderColor: "rgba(78, 115, 223, 1)",  // Border color
      pointBackgroundColor: "rgba(78, 115, 223, 1)", // Points color
      pointBorderColor: "#fff",
      pointHoverBackgroundColor: "#fff",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      data: [4215, 5312, 6251, 7841, 9821, 14984],
    }],
  },
  options: {
    maintainAspectRatio: false,
    scale: {  // Use 'scale' instead of 'scales' for radar charts
      angleLines: {
        display: true
      },
      ticks: {
        suggestedMin: 0,
        suggestedMax: 15000,
        callback: function(value) {
          return '$' + number_format(value);
        }
      }
    },
    legend: {
      display: true
    },
    tooltips: {
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ': $' + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
});
