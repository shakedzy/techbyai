---
layout: page
title: Statistics
permalink: /stats/
---

Start Date: <input type="date" id="startDate">
End Date: <input type="date" id="endDate">
<button onclick="updateChart()">Update Chart</button>

<canvas id="costChart"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script type="text/javascript">

function parseDuration(durationStr) {
    const parts = durationStr.split(':');
    const secondsParts = parts[2].split('.');
    const hours = parseInt(parts[0], 10);
    const minutes = parseInt(parts[1], 10);
    const seconds = parseInt(secondsParts[0], 10);
    const milliseconds_str = secondsParts[1];
    const milliseconds = parseInt(milliseconds_str, 10);

    return hours * 3600 + minutes * 60 + seconds + milliseconds / 10**milliseconds_str.length;
}

var postData = [
  {% for post in site.posts %}
    {
      date: "{{ post.date | date: '%Y-%m-%d' }}",
      cost: {{post.cost}},
      processingTime: parseDuration("{{ post.processing }}")
    },
  {% endfor %}
];


var costChart; // Chart variable for global access

// Function to create or update the chart
function createChart(data) {
    if (costChart) {
        costChart.destroy();
    }
    costChart = new Chart(document.getElementById('costChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: data.map(post => post.date),
            datasets: [{
                label: 'Cost ($)',
                data: data.map(post => post.cost),
                borderColor: 'rgb(75, 192, 192)',
                backgroundColor: 'rgba(75, 192, 192, 0.5)',
                yAxisID: 'y-axis-cost'
            }, {
                label: 'Processing Time (seconds)',
                data: data.map(post => post.processingTime),
                borderColor: 'rgb(244, 140, 105)',
                backgroundColor: 'rgba(244, 140, 105, 0.5)',
                yAxisID: 'y-axis-time'
            }]
        },
        options: {
            scales: {
                x: {
                    reverse: true,
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                'y-axis-cost': {
                    type: 'linear',
                    position: 'left',
                    title: {
                        display: true,
                        text: 'Cost ($)'
                    }
                },
                'y-axis-time': {
                    type: 'linear',
                    position: 'right',
                    title: {
                        display: true,
                        text: 'Time (seconds)'
                    },
                    grid: {
                        drawOnChartArea: false // This ensures grid lines for this axis don't appear on the left
                    }
                }
            }
        }
    });
}



// Function to update chart based on selected dates
function updateChart() {
    var startDate = document.getElementById('startDate').value;
    var endDate = document.getElementById('endDate').value;
    var filteredData = postData.filter(function(post) {
        return (!startDate || new Date(post.date) >= new Date(startDate)) &&
               (!endDate || new Date(post.date) <= new Date(endDate));
    });
    createChart(filteredData);
}

// Initialize date selectors
document.addEventListener('DOMContentLoaded', function() {
    var today = new Date();
    var lastWeek = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 7);

    document.getElementById('endDate').value = today.toISOString().split('T')[0];
    document.getElementById('startDate').value = lastWeek.toISOString().split('T')[0];

    updateChart(); // Update the chart to reflect the initial date range
});
</script>
