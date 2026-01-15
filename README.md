# Comprehensive Stroke Center Finder

A web-based dashboard that allows users to find certified Comprehensive Stroke Centers within a 50-mile radius of any US zipcode. This tool helps patients and healthcare providers quickly locate the nearest comprehensive stroke care facilities.

## Features

- Search by any valid US zipcode
- Displays comprehensive stroke centers within 50-mile radius
- Distance calculation using Haversine formula
- Shows facility details (address, phone, certification)
- Responsive design for mobile and desktop
- Data from reputable sources (Joint Commission & DNV Healthcare)

## Quick Start

### 1. View the Dashboard

Simply open `index.html` in your web browser:

```bash
# Using Python's built-in server (recommended)
python3 -m http.server 8000

# Then visit: http://localhost:8000
```

Or just double-click `index.html` to open in your default browser.

### 2. Search for Stroke Centers

- Enter any 5-digit US zipcode
- Click "Find Centers" or press Enter
- View results sorted by distance

## Data Setup

### Zipcode Database (Already Configured)

The zipcode database with coordinates for all US zipcodes has been automatically downloaded:
- **File**: `data/zipcodes.json`
- **Contains**: 33,144+ US zipcodes with latitude/longitude
- **Source**: US Government Census Data

To refresh the zipcode data:
```bash
python3 download_zipcode_data.py
```

### Stroke Center Data (✓ Real Data Included)

**UPDATED**: The database now contains **243 real comprehensive stroke centers** across **41 states**, compiled from:
- **Texas**: 51 centers (complete official Texas DSHS data)
- **Florida**: 49 centers (complete official Florida Agency for Healthcare Administration data)
- **New York**: 30 centers (complete official NYS Department of Health designations)
- **California**: 20 centers (major LA, San Diego, and Bay Area comprehensive stroke centers)
- **Pennsylvania**: 14 centers (official PA Department of Health designations)
- **Other 36 States**: 79 centers (comprehensive stroke centers from VA, WA, TN, NC, GA, OH, MI, IL, WI, IN, MD, DC, CT, CO, AZ, and more)
- All centers have been geocoded with accurate coordinates
- **Coverage**: 81.8% of the estimated 297 total US comprehensive stroke centers

**To update the database with more centers:**
```bash
python3 compile_all_stroke_centers.py
```

This script automatically geocodes addresses using free OpenStreetMap data (no API key required).

#### Option 1: Joint Commission (Recommended)

The Joint Commission is the primary accreditation organization for stroke centers in the US.

1. Visit: [Joint Commission Quality Check](https://www.qualitycheck.org/data-download/)
2. Navigate to "Certification Data Download"
3. Look for stroke certification files
4. Download the file (usually Excel or CSV format)
5. Save to `data/stroke_centers.json` in this format:

```json
[
  {
    "name": "Hospital Name",
    "address": "123 Main St",
    "city": "City",
    "state": "ST",
    "zipcode": "12345",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "phone": "(555) 123-4567",
    "certification_org": "Joint Commission",
    "certification_type": "Comprehensive Stroke Center"
  }
]
```

#### Option 2: DNV Healthcare

DNV is another major accreditation organization for stroke centers.

1. Visit: [DNV Stroke Care Certification](https://www.dnv.us/supplychain/healthcare/stroke-certs/)
2. Search their hospital database
3. Filter for Comprehensive Stroke Centers (CSC)
4. Compile data into the JSON format above

#### Option 3: State Health Departments

Many states maintain their own stroke center designation lists:
- [New York State Stroke Centers](https://www.health.ny.gov/diseases/cardiovascular/stroke/designation/)
- Search "[Your State] comprehensive stroke centers" for state-specific lists

#### Converting CSV to JSON

If you download CSV data from Joint Commission, use the helper script:

```bash
# Edit prepare_stroke_centers.py to use convert_csv_to_json()
# Then run:
python3 prepare_stroke_centers.py
```

## Project Structure

```
stroke-center-finder/
├── index.html                        # Main dashboard HTML
├── styles.css                        # Minimalistic white/grey styling
├── app.js                            # Frontend JavaScript logic
├── download_zipcode_data.py          # Script to download zipcode data
├── prepare_stroke_centers.py        # Script to prepare stroke center data
├── compile_all_stroke_centers.py    # Original compilation script
├── compile_comprehensive_centers.py # Enhanced script with FL + PA data
├── compile_final_database.py        # Final database with TX + NY data
├── data/
│   ├── zipcodes.json                # US zipcode coordinates (33,144 entries)
│   └── stroke_centers.json          # Stroke center data (243 centers)
├── add_remaining_centers.py         # Script to add manually researched centers
└── README.md                         # This file
```

## How It Works

1. **User Input**: User enters a 5-digit US zipcode
2. **Validation**: System checks if zipcode exists in database
3. **Distance Calculation**: Uses Haversine formula to calculate great-circle distance between user location and each stroke center
4. **Filtering**: Filters centers within 50-mile radius
5. **Display**: Shows results sorted by distance, closest first

### Distance Calculation

The Haversine formula calculates the shortest distance between two points on a sphere:

```javascript
distance = 2 * R * arcsin(sqrt(
  sin²((lat2 - lat1) / 2) +
  cos(lat1) * cos(lat2) * sin²((lon2 - lon1) / 2)
))
```

Where R = 3,959 miles (Earth's radius)

## Technology Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data Processing**: Python 3
- **Data Storage**: JSON files (client-side)
- **No backend required**: Fully static site

## Updating the Data

### Updating Zipcode Data

```bash
python3 download_zipcode_data.py
```

This downloads the latest US zipcode coordinates from government sources.

### Updating Stroke Center Data

1. Download latest data from Joint Commission or DNV
2. Convert to JSON format (see example above)
3. Replace `data/stroke_centers.json`
4. Refresh the web page

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Privacy & Security

- All data processing happens in the browser
- No data is sent to external servers
- No user tracking or analytics
- HIPAA-friendly (no patient data collected)

## Limitations

- Distance is calculated "as the crow flies" (straight line), not driving distance
- Database includes 243 comprehensive stroke centers (81.8% of ~297 total US centers)
- Covers 41 states; additional centers can be added from other state health departments and certification databases
- Requires internet connection only to load initial page (can work offline after)

## Emergency Notice

**IN CASE OF STROKE, CALL 911 IMMEDIATELY**

Time is critical for stroke treatment. Always call emergency services first.

## Contributing

To add more features:
1. Add more search filters (certification type, hospital rating)
2. Integrate mapping (Google Maps, Mapbox)
3. Add driving directions
4. Include more certification types (Primary Stroke Centers, Thrombectomy-Capable)

## Data Sources

- **Zipcodes**: US Government Census Bureau Data
- **Stroke Centers**: Joint Commission & DNV Healthcare
- **Certification Standards**: [Joint Commission Comprehensive Stroke Center Requirements](https://www.jointcommission.org)

## License

This project is provided as-is for healthcare and educational purposes.

## Support

For questions about:
- **Certification data**: Contact Joint Commission or DNV Healthcare
- **Technical issues**: Check browser console for errors
- **Feature requests**: Submit via GitHub issues

---

**Remember**: This tool is for informational purposes only. Always verify facility certifications and call 911 in emergencies.
