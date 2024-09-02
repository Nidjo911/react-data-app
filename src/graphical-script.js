// Get the canvas element
const ctx = document.getElementById('myChart').getContext('2d');

// Data for the scatter plot
const data = {
    labels: ['A', 'B', 'C', 'D', 'E'], // Labels for the x-axis (optional)
    datasets: [{
        label: 'My Dataset',
        data: [
            { x: 10, y: 20 },
            { x: 30, y: 50 },
            { x: 50, y: 30 },
            { x: 70, y: 80 },
            { x: 90, y: 60 }
        ],
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        pointRadius: 5 // Adjust the point radius as needed
    }]
};

// Configuration options
const config = {
    type: 'scatter',
    data: data,
    options: {
        scales: {
            x: {
                type: 'linear', // Adjust the scale type if needed
                title: {
                    display: true,
                    text: 'X-axis label'
                }
            },
            y: {
                type: 'linear', // Adjust the scale type if needed
                title: {
                    display: true,
                    text: 'Y-axis label'
                }
            }
        }
    }
};

// Create the chart
const myChart = new Chart(ctx, config);