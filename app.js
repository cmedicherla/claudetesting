// Load data files
let strokeCenters = [];
let zipcodeData = {};
let statesList = [];

// State name mapping
const stateNames = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
    'DC': 'District of Columbia'
};

// Initialize the application
async function init() {
    try {
        // Load stroke centers data
        const centersResponse = await fetch('data/stroke_centers.json');
        strokeCenters = await centersResponse.json();

        // Load zipcode data
        const zipResponse = await fetch('data/zipcodes.json');
        zipcodeData = await zipResponse.json();

        // Get unique states and populate dropdown
        const uniqueStates = [...new Set(strokeCenters.map(center => center.state))].sort();
        statesList = uniqueStates;
        populateStateDropdown(uniqueStates);

        // Update stats
        document.getElementById('totalCenters').textContent = strokeCenters.length;
        document.getElementById('totalStates').textContent = uniqueStates.length;

        console.log(`Loaded ${strokeCenters.length} stroke centers`);
        console.log(`Loaded ${Object.keys(zipcodeData).length} zipcodes`);
        console.log(`States available: ${uniqueStates.join(', ')}`);
    } catch (error) {
        console.error('Error loading data:', error);
        showError('Error loading data files. Please ensure data files are present.');
    }
}

// Populate state dropdown
function populateStateDropdown(states) {
    const stateSelect = document.getElementById('stateSelect');
    states.forEach(state => {
        const option = document.createElement('option');
        option.value = state;
        option.textContent = `${stateNames[state] || state} (${state})`;
        stateSelect.appendChild(option);
    });
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

    // Find centers within 100 miles
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
        .filter(center => center.distance <= 100)
        .sort((a, b) => a.distance - b.distance);

    // Hide loading, show results
    document.getElementById('loading').style.display = 'none';
    displayResults(zipcode, centersWithDistance, userLocation.city, userLocation.state);
}

// Search by state
function searchByState() {
    const stateSelect = document.getElementById('stateSelect');
    const selectedState = stateSelect.value;

    // Clear previous error
    showError('');

    // Validate state selection
    if (!selectedState) {
        showError('Please select a state from the dropdown');
        return;
    }

    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('loadingText').textContent = `Loading centers in ${stateNames[selectedState]}...`;
    document.getElementById('results').style.display = 'none';

    // Simulate processing time for better UX
    setTimeout(() => {
        performStateSearch(selectedState);
    }, 500);
}

function performStateSearch(state) {
    // Find all centers in the selected state
    const centersInState = strokeCenters
        .filter(center => center.state === state)
        .sort((a, b) => {
            // Sort by city first, then by name
            const cityCompare = (a.city || '').localeCompare(b.city || '');
            if (cityCompare !== 0) return cityCompare;
            return a.name.localeCompare(b.name);
        });

    // Hide loading, show results
    document.getElementById('loading').style.display = 'none';
    displayStateResults(state, centersInState);
}

// Switch between tabs
function switchTab(tabName) {
    // Clear errors
    showError('');

    // Hide results
    document.getElementById('results').style.display = 'none';

    // Update tab buttons
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => button.classList.remove('active'));
    event.target.classList.add('active');

    // Show/hide tab content
    document.getElementById('zipcodeTab').classList.remove('active');
    document.getElementById('stateTab').classList.remove('active');

    if (tabName === 'zipcode') {
        document.getElementById('zipcodeTab').classList.add('active');
    } else {
        document.getElementById('stateTab').classList.add('active');
    }
}

function displayResults(zipcode, centers, city, state) {
    const resultsDiv = document.getElementById('results');
    const centersListDiv = document.getElementById('centersList');
    const searchZipcodeSpan = document.getElementById('searchZipcode');
    const resultsCountP = document.getElementById('resultsCount');

    searchZipcodeSpan.textContent = `${zipcode} (${city}, ${state})`;

    if (centers.length === 0) {
        resultsCountP.textContent = 'No comprehensive stroke centers found within 100 miles';
        centersListDiv.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #666;">
                <p style="font-size: 1.2em; margin-bottom: 10px;">No centers found nearby</p>
                <p>Try searching a different zipcode or expand your search radius.</p>
            </div>
        `;
    } else {
        resultsCountP.textContent = `Found ${centers.length} comprehensive stroke center${centers.length !== 1 ? 's' : ''} within 100 miles`;

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

function displayStateResults(state, centers) {
    const resultsDiv = document.getElementById('results');
    const centersListDiv = document.getElementById('centersList');
    const searchZipcodeSpan = document.getElementById('searchZipcode');
    const resultsCountP = document.getElementById('resultsCount');

    searchZipcodeSpan.textContent = `${stateNames[state] || state} (${state})`;

    if (centers.length === 0) {
        resultsCountP.textContent = 'No comprehensive stroke centers found in this state';
        centersListDiv.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #666;">
                <p style="font-size: 1.2em; margin-bottom: 10px;">No centers found</p>
                <p>This state doesn't have any comprehensive stroke centers in our database.</p>
            </div>
        `;
    } else {
        resultsCountP.textContent = `Found ${centers.length} comprehensive stroke center${centers.length !== 1 ? 's' : ''} in ${stateNames[state]}`;

        centersListDiv.innerHTML = centers.map(center => `
            <div class="center-card">
                <div class="center-name">
                    ${center.name}
                    ${center.certification_org ? `<span class="cert-badge">${center.certification_org}</span>` : ''}
                </div>
                <div class="center-info">
                    <div class="info-row">
                        <span class="info-label">Location:</span>
                        <span>${center.city ? `${center.city}, ` : ''}${center.state} ${center.zipcode || ''}</span>
                    </div>
                    ${center.address ? `
                    <div class="info-row">
                        <span class="info-label">Address:</span>
                        <span>${center.address}</span>
                    </div>
                    ` : ''}
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
