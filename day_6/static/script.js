function triggerGate(endpoint) {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            document.querySelector('.msg').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            document.querySelector('.msg').innerHTML = `<pre>Error: ${error}</pre>`;
        });
}