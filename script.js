async function fetchData() {
    try {
        const response = await fetch('/data');
        const data = await response.json();
        const table = document.getElementById('data-table');
        table.innerHTML = '';
        data.forEach(item => {
            const row = `<tr>
                            <td>${item.timestamp}</td>
                            <td>${item.heart_rate}</td>
                            <td>${item.oxygen_level}</td>
                         </tr>`;
            table.innerHTML += row;
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

setInterval(fetchData, 3000); // Update every 3 seconds
fetchData();
