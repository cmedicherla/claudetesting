// Stroke desert visualization
let strokeCenters = [];
let map;

// Initialize the application
async function init() {
    try {
        // Load stroke centers data
        const centersResponse = await fetch('data/stroke_centers.json');
        strokeCenters = await centersResponse.json();

        console.log(`Loaded ${strokeCenters.length} stroke centers`);

        // Initialize map
        initializeMap();

        // Add stroke centers and coverage areas
        addStrokeCenters();
    } catch (error) {
        console.error('Error loading data:', error);
        alert('Error loading stroke center data. Please ensure data files are present.');
    }
}

// Initialize Leaflet map
function initializeMap() {
    // Create map centered on continental US
    map = L.map('map', {
        center: [39.8283, -98.5795], // Geographic center of continental US
        zoom: 5,
        minZoom: 4,
        maxZoom: 10
    });

    // Add a simple grayscale tile layer for minimalist look
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    }).addTo(map);
}

// Add stroke centers and coverage circles
function addStrokeCenters() {
    // 4.5 hours at 60 mph = 270 miles = approximately 434,522 meters
    const coverageRadiusMeters = 270 * 1609.34; // Convert miles to meters

    // First, add a pink overlay covering the continental US (the entire potential desert area)
    const usaBounds = [
        [24.396308, -125.0],  // Southwest corner
        [49.384358, -66.93457] // Northeast corner
    ];

    L.rectangle(usaBounds, {
        color: '#F44336',
        fillColor: '#F44336',
        fillOpacity: 0.35,
        weight: 0,
        interactive: false
    }).addTo(map);

    // Add white/transparent circles to "erase" the pink in covered areas
    strokeCenters.forEach(center => {
        L.circle([center.latitude, center.longitude], {
            radius: coverageRadiusMeters,
            color: 'rgba(255, 255, 255, 0.95)',
            fillColor: 'rgba(255, 255, 255, 0.95)',
            fillOpacity: 0.95,
            weight: 0,
            interactive: false
        }).addTo(map);
    });

    // Now add the black marker dots for each stroke center on top
    strokeCenters.forEach(center => {
        const marker = L.circleMarker([center.latitude, center.longitude], {
            radius: 5,
            fillColor: '#1d1d1f',
            color: '#fff',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.9
        }).addTo(map);

        // Add popup with center information
        let popupContent = `
            <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
                <strong style="font-size: 14px; color: #1d1d1f;">${center.name}</strong><br>
                <span style="font-size: 12px; color: #6e6e73;">
                    ${center.city ? center.city + ', ' : ''}${center.state}<br>
                    ${center.certification_org || 'Certified'}
                </span>
            </div>
        `;

        marker.bindPopup(popupContent);
    });

    // Console explanation
    console.log(`
        Stroke Desert Visualization (Inverted):
        - Pink areas show "stroke deserts" (>4.5 hours from a center)
        - White/cleared areas are within 270 miles of a stroke center
        - ${strokeCenters.length} comprehensive stroke centers mapped as black dots
    `);
}

// Start the application when page loads
document.addEventListener('DOMContentLoaded', () => {
    init();
});
