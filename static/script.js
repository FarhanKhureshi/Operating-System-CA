let chartInstance = null;

document.getElementById('diskForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const requests = document.getElementById('requests').value;
    const start = document.getElementById('start').value;
    const max_track = document.getElementById('max_track').value;
    const direction = document.getElementById('direction').value;
    const algorithm = document.getElementById('algorithm').value;

    const data = {
        requests: requests,
        start: start,
        max_track: max_track,
        direction: direction,
        algorithm: algorithm
    };

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('seek_count').innerText = result.seek_count;
        document.getElementById('avg_seek_time').innerText = result.avg_seek_time.toFixed(2);
        document.getElementById('result').style.display = 'block';

        // Dynamically update the graph
        updateGraph(result.movements);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function updateGraph(movements) {
    const ctx = document.getElementById('diskMovementChart').getContext('2d');

    // If chartInstance already exists, destroy it to re-render with new data
    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: movements,  // The labels will be the movements in the order they occur
            datasets: [{
                label: 'Disk Head Movement',
                data: movements,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Time (Movements)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Track Number'
                    }
                }
            }
        }
    });
}
