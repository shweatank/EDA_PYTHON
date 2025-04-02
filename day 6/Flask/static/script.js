function triggerGate(endpoint) {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => alert(JSON.stringify(data, null, 2)))
        .catch(error => console.error('Error:', error));
}
