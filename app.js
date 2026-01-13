// Load data files
let strokeCenters = [];
let zipcodeData = {};

// Initialize the application
async function init() {
    try {
        // Load stroke centers data
        const centersResponse = await fetch('data/stroke_centers.json');
        strokeCenters = await centersResponse.json();

        // Load zipcode data
        const zipResponse = await fetch('data/zipcodes.json');
        zipcodeData = await zipResponse.json();

        console.log(`Loaded ${strokeCenters.length} stroke centers`);
        console.log(`Loaded ${Object.keys(zipcodeData).length} zipcodes`);
    } catch (error) {
        console.error('Error loading data:', error);
        showError('Error loading data files. Please ensure data files are present.');
    }
}

// Calculate distance between two coordinates using Haversine formula
function calculateDistance(lat1, lon1, lat2, lon2) {
    const R = 3959; // Earth's radius in miles
    const dLat = toRadians(lat2 - lat1);
    const dLon = toRadians(lon2 - lon1);

    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(toRadians(lat1)) * Math.cos(toRadians(lat2)) *
              Math.sin(dLon / 2) * Math.sin(dLon / 2);

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c;

    return distance;
}

function toRadians(degrees) {
    return degrees * (Math.PI / 180);
}

// Search for stroke centers
async function searchStrokeCenters() {
    const zipcodeInput = document.getElementById('zipcode');
    const zipcode = zipcodeInput.value.trim();

    // Clear previous error
    showError('');

    // Validate zipcode
    if (!zipcode || !/^\d{5}$/.test(zipcode)) {
        showError('Please enter a valid 5-digit US zipcode');
        return;
    }

    // Check if zipcode exists in database
    if (!zipcodeData[zipcode]) {
        showError('Zipcode not found. Please enter a valid US zipcode.');
        return;
    }

    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';

    // Simulate processing time for better UX
    setTimeout(() => {
        performSearch(zipcode);
    }, 500);
}

function performSearch(zipcode) {
    const userLocation = zipcodeData[zipcode];
    const userLat = userLocation.lat;
    const userLon = userLocation.lon;

    // Find centers within 50 miles
    const centersWithDistance = strokeCenters
        .map(center => {
            const distance = calculateDistance(
                userLat,
                userLon,
                center.latitude,
                center.longitude
            );
            return { ...center, distance };
        })
        .filter(center => center.distance <= 50)
        .sort((a, b) => a.distance - b.distance);

    // Hide loading, show results
    document.getElementById('loading').style.display = 'none';
    displayResults(zipcode, centersWithDistance, userLocation.city, userLocation.state);
}

function displayResults(zipcode, centers, city, state) {
    const resultsDiv = document.getElementById('results');
    const centersListDiv = document.getElementById('centersList');
    const searchZipcodeSpan = document.getElementById('searchZipcode');
    const resultsCountP = document.getElementById('resultsCount');

    searchZipcodeSpan.textContent = `${zipcode} (${city}, ${state})`;

    if (centers.length === 0) {
        resultsCountP.textContent = 'No comprehensive stroke centers found within 50 miles';
        centersListDiv.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #666;">
                <p style="font-size: 1.2em; margin-bottom: 10px;">No centers found nearby</p>
                <p>Try searching a different zipcode or expand your search radius.</p>
            </div>
        `;
    } else {
        resultsCountP.textContent = `Found ${centers.length} comprehensive stroke center${centers.length !== 1 ? 's' : ''} within 50 miles`;

        centersListDiv.innerHTML = centers.map(center => `
            <div class="center-card">
                <div class="center-name">
                    ${center.name}
                    ${center.certification_org ? `<span class="cert-badge">${center.certification_org}</span>` : ''}
                </div>
                <div class="center-info">
                    <div class="info-row">
                        <span class="info-label">Address:</span>
                        <span>${center.address}${center.city ? `, ${center.city}` : ''}${center.state ? `, ${center.state}` : ''} ${center.zipcode || ''}</span>
                    </div>
                    ${center.phone ? `
                    <div class="info-row">
                        <span class="info-label">Phone:</span>
                        <span>${center.phone}</span>
                    </div>
                    ` : ''}
                    ${center.certification_type ? `
                    <div class="info-row">
                        <span class="info-label">Certification:</span>
                        <span>${center.certification_type}</span>
                    </div>
                    ` : ''}
                    <div class="info-row">
                        <span class="distance-badge">📍 ${center.distance.toFixed(1)} miles away</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    resultsDiv.style.display = 'block';
    resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
}

// Allow Enter key to trigger search
document.addEventListener('DOMContentLoaded', () => {
    init();

    const zipcodeInput = document.getElementById('zipcode');
    zipcodeInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            searchStrokeCenters();
        }
    });

    // Only allow numeric input
    zipcodeInput.addEventListener('input', (e) => {
        e.target.value = e.target.value.replace(/[^0-9]/g, '');
    });
});
