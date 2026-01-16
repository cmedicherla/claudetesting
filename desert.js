// Stroke center visualization with toggleable layers
let comprehensiveCenters = [];
let thrombectomyCenters = [];
let primaryCenters = [];
let map;

// Layer groups for each center type
let cscLayer;
let tscLayer;
let pscLayer;

// Initialize the application
async function init() {
    try {
        // Load all three datasets
        const cscResponse = await fetch('data/stroke_centers.json');
        comprehensiveCenters = await cscResponse.json();

        const tscResponse = await fetch('data/thrombectomy_centers.json');
        thrombectomyCenters = await tscResponse.json();

        const pscResponse = await fetch('data/psc_sample.json');
        primaryCenters = await pscResponse.json();

        console.log(`Loaded ${comprehensiveCenters.length} CSCs, ${thrombectomyCenters.length} TSCs, ${primaryCenters.length} PSCs`);

        // Initialize map
        initializeMap();

        // Add all stroke centers
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
        center: [39.8283, -98.5795],
        zoom: 5,
        minZoom: 4,
        maxZoom: 10
    });

    // Add minimalist grayscale basemap
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    }).addTo(map);

    // Create layer groups
    cscLayer = L.layerGroup().addTo(map);
    tscLayer = L.layerGroup().addTo(map);
    pscLayer = L.layerGroup().addTo(map);
}

// Add stroke centers with different colors and radii
function addStrokeCenters() {
    // CSC: Green, 60 miles (1 hour)
    addCenterType(comprehensiveCenters, cscLayer, 60 * 1609.34, '#4CAF50', 'CSC');

    // TSC: Blue, 45 miles (45 min)
    addCenterType(thrombectomyCenters, tscLayer, 45 * 1609.34, '#2196F3', 'TSC');

    // PSC: Orange, 30 miles (30 min)
    addCenterType(primaryCenters, pscLayer, 30 * 1609.34, '#FF9800', 'PSC');
}

function addCenterType(centers, layer, radiusMeters, color, type) {
    centers.forEach(center => {
        // Add coverage circle
        L.circle([center.latitude, center.longitude], {
            radius: radiusMeters,
            color: color,
            fillColor: color,
            fillOpacity: 0.12,
            weight: 1,
            opacity: 0.35
        }).addTo(layer);

        // Add marker
        const marker = L.circleMarker([center.latitude, center.longitude], {
            radius: 5,
            fillColor: color,
            color: '#fff',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.9
        }).addTo(layer);

        // Popup
        marker.bindPopup(`
            <div style="font-family: -apple-system, sans-serif;">
                <strong style="font-size: 14px; color: #1d1d1f;">${center.name}</strong><br>
                <span style="font-size: 12px; color: #6e6e73;">
                    ${center.city ? center.city + ', ' : ''}${center.state}<br>
                    ${center.certification_org || 'Certified'}<br>
                    <em>${type}</em>
                </span>
            </div>
        `);
    });
}

// Toggle center type visibility
function toggleCenterType(type) {
    const checkbox = document.getElementById(`toggle-${type}`);
    const isChecked = checkbox.checked;

    if (type === 'csc') {
        if (isChecked) {
            map.addLayer(cscLayer);
        } else {
            map.removeLayer(cscLayer);
        }
    } else if (type === 'tsc') {
        if (isChecked) {
            map.addLayer(tscLayer);
        } else {
            map.removeLayer(tscLayer);
        }
    } else if (type === 'psc') {
        if (isChecked) {
            map.addLayer(pscLayer);
        } else {
            map.removeLayer(pscLayer);
        }
    }
}

// Start the application
document.addEventListener('DOMContentLoaded', () => {
    init();
});
