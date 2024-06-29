document.addEventListener('DOMContentLoaded', function() {
    const fetchDataBtn = document.getElementById('fetchDataBtn');
    const dataContainer = document.getElementById('dataContainer');

    fetchDataBtn.addEventListener('click', async function() {
        try {
            const response = await fetch('/api/health-data'); // Updated endpoint
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            dataContainer.innerHTML = `<p>Received data from backend: ${JSON.stringify(data)}</p>`;
        } catch (error) {
            console.error('Error fetching data:', error);
            dataContainer.innerHTML = '<p>Error fetching data</p>';
        }
    });
});
