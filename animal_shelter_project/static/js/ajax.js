// Function to fetch and render shelter list
function renderShelterList() {
    fetch('/api/shelters/') // Assuming '/api/shelters/' is the endpoint for shelter list
        .then(response => response.json())
        .then(data => {
            const shelterListContainer = document.getElementById('shelter-list');
            shelterListContainer.innerHTML = ''; // Clear previous content
            data.forEach(shelter => {
                const shelterItem = document.createElement('div');
                shelterItem.textContent = `Name: ${shelter.name}, Location: ${shelter.location}`; // Adjust based on your serializer fields
                shelterListContainer.appendChild(shelterItem);
            });
        })
        .catch(error => console.error('Error fetching shelter list:', error));
}

// Function to fetch and render shelter detail
function renderShelterDetail(shelterId) {
    fetch(`/api/shelters/${shelterId}/`) // Assuming '/api/shelters/:id/' is the endpoint for shelter detail
        .then(response => response.json())
        .then(data => {
            const shelterDetailContainer = document.getElementById('shelter-detail');
            shelterDetailContainer.innerHTML = ''; // Clear previous content
            const shelterDetail = document.createElement('div');
            shelterDetail.textContent = `Name: ${data.name}, Location: ${data.location}`; // Adjust based on your serializer fields
            shelterDetailContainer.appendChild(shelterDetail);
        })
        .catch(error => console.error('Error fetching shelter detail:', error));
}

// Example usage:
renderShelterList(); // Render shelter list on page load
// Assuming shelterId is obtained from somewhere, like a click event
const shelterId = 1; // Example shelter ID
renderShelterDetail(shelterId); // Render shelter detail for the given shelter ID
