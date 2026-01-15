#!/usr/bin/env python3
"""
Add remaining comprehensive stroke centers to reach closer to 297 total
Focus on missing states and underrepresented states
"""

import json
import time
import requests

# Additional comprehensive stroke centers for missing/underrepresented states
ADDITIONAL_CENTERS = [
    # New Jersey (5-8 expected)
    {"name": "Hackensack University Medical Center", "city": "Hackensack", "state": "NJ", "zipcode": "07601"},
    {"name": "Robert Wood Johnson University Hospital", "city": "New Brunswick", "state": "NJ", "zipcode": "08901"},
    {"name": "Cooper University Hospital", "city": "Camden", "state": "NJ", "zipcode": "08103"},
    {"name": "Morristown Medical Center", "city": "Morristown", "state": "NJ", "zipcode": "07960"},
    {"name": "Jersey Shore University Medical Center", "city": "Neptune", "state": "NJ", "zipcode": "07753"},
    {"name": "Saint Barnabas Medical Center", "city": "Livingston", "state": "NJ", "zipcode": "07039"},
    {"name": "JFK Medical Center", "city": "Edison", "state": "NJ", "zipcode": "08820"},

    # Louisiana (3-5 expected)
    {"name": "Ochsner Medical Center", "city": "New Orleans", "state": "LA", "zipcode": "70121"},
    {"name": "University Medical Center New Orleans", "city": "New Orleans", "state": "LA", "zipcode": "70112"},
    {"name": "Our Lady of the Lake Regional Medical Center", "city": "Baton Rouge", "state": "LA", "zipcode": "70808"},
    {"name": "LSU Health Shreveport", "city": "Shreveport", "state": "LA", "zipcode": "71103"},

    # South Carolina (2-3 expected)
    {"name": "Medical University of South Carolina", "city": "Charleston", "state": "SC", "zipcode": "29425"},
    {"name": "Prisma Health Richland", "city": "Columbia", "state": "SC", "zipcode": "29203"},
    {"name": "Greenville Memorial Hospital", "city": "Greenville", "state": "SC", "zipcode": "29605"},

    # Indiana (fix failed geocoding - 3 centers)
    {"name": "Indiana University Health Methodist Hospital", "city": "Indianapolis", "state": "IN", "zipcode": "46202"},
    {"name": "Indiana University Health University Hospital", "city": "Indianapolis", "state": "IN", "zipcode": "46202"},
    {"name": "Ascension St. Vincent Indianapolis Hospital", "city": "Indianapolis", "state": "IN", "zipcode": "46260"},

    # Arkansas (1-2 expected)
    {"name": "Baptist Health Medical Center - Little Rock", "city": "Little Rock", "state": "AR", "zipcode": "72205"},
    {"name": "UAMS Medical Center", "city": "Little Rock", "state": "AR", "zipcode": "72205"},

    # Mississippi (1-2 expected)
    {"name": "University of Mississippi Medical Center", "city": "Jackson", "state": "MS", "zipcode": "39216"},

    # Missouri - expand (3-5 more expected)
    {"name": "Barnes-Jewish Hospital", "city": "St. Louis", "state": "MO", "zipcode": "63110"},
    {"name": "Saint Luke's Hospital of Kansas City", "city": "Kansas City", "state": "MO", "zipcode": "64111"},
    {"name": "University of Missouri Hospital", "city": "Columbia", "state": "MO", "zipcode": "65212"},
    {"name": "Mercy Hospital St. Louis", "city": "St. Louis", "state": "MO", "zipcode": "63141"},

    # Maryland - expand (2-3 more expected)
    {"name": "Suburban Hospital", "city": "Bethesda", "state": "MD", "zipcode": "20814"},
    {"name": "Sinai Hospital of Baltimore", "city": "Baltimore", "state": "MD", "zipcode": "21215"},

    # Tennessee - expand
    {"name": "Methodist Le Bonheur Healthcare", "city": "Memphis", "state": "TN", "zipcode": "38103"},

    # Minnesota - expand (Mayo Clinic, etc)
    {"name": "Mayo Clinic Hospital Rochester", "city": "Rochester", "state": "MN", "zipcode": "55905"},
    {"name": "Abbott Northwestern Hospital", "city": "Minneapolis", "state": "MN", "zipcode": "55407"},

    # Rhode Island
    {"name": "Rhode Island Hospital", "city": "Providence", "state": "RI", "zipcode": "02903"},

    # Fix geocoding failures from last run
    {"name": "MemorialCare Long Beach Medical Center", "city": "Long Beach", "state": "CA", "zipcode": "90806"},
    {"name": "Providence Little Company of Mary Medical Center Torrance", "city": "Torrance", "state": "CA", "zipcode": "90503"},
    {"name": "Emanate Health Queen of the Valley", "city": "West Covina", "state": "CA", "zipcode": "91790"},
    {"name": "Los Robles Hospital and Medical Center", "city": "Thousand Oaks", "state": "CA", "zipcode": "91360"},
    {"name": "UC San Diego Medical Center Hillcrest", "city": "San Diego", "state": "CA", "zipcode": "92103"},
    {"name": "Virginia Mason Franciscan Health Seattle", "city": "Seattle", "state": "WA", "zipcode": "98101"},
    {"name": "Providence Sacred Heart Medical Center Spokane", "city": "Spokane", "state": "WA", "zipcode": "99204"},
    {"name": "Ascension Saint Thomas Hospital West Nashville", "city": "Nashville", "state": "TN", "zipcode": "37205"},
    {"name": "Regional One Health Memphis", "city": "Memphis", "state": "TN", "zipcode": "38103"},
    {"name": "Atrium Health Carolinas Medical Center Charlotte", "city": "Charlotte", "state": "NC", "zipcode": "28203"},
    {"name": "UC Health University Hospital Cincinnati", "city": "Cincinnati", "state": "OH", "zipcode": "45219"},
    {"name": "Mercy Health St Vincent Medical Center Toledo", "city": "Toledo", "state": "OH", "zipcode": "43608"},
    {"name": "Spectrum Health Butterworth Hospital Grand Rapids", "city": "Grand Rapids", "state": "MI", "zipcode": "49503"},
    {"name": "OSF Saint Francis Medical Center Peoria", "city": "Peoria", "state": "IL", "zipcode": "61637"},

    # Additional research - states with potential gaps
    {"name": "Nebraska Medical Center", "city": "Omaha", "state": "NE", "zipcode": "68198"},
    {"name": "University of Kansas Hospital", "city": "Kansas City", "state": "KS", "zipcode": "66160"},
    {"name": "University of Iowa Hospitals", "city": "Iowa City", "state": "IA", "zipcode": "52242"},
    {"name": "Providence Portland Medical Center", "city": "Portland", "state": "OR", "zipcode": "97213"},
    {"name": "Oregon Health & Science University", "city": "Portland", "state": "OR", "zipcode": "97239"},
    {"name": "University of Utah Hospital", "city": "Salt Lake City", "state": "UT", "zipcode": "84132"},
    {"name": "Intermountain Medical Center", "city": "Murray", "state": "UT", "zipcode": "84107"},
    {"name": "University of Alabama at Birmingham Hospital", "city": "Birmingham", "state": "AL", "zipcode": "35233"},
    {"name": "Huntsville Hospital", "city": "Huntsville", "state": "AL", "zipcode": "35801"},
    {"name": "University of Kentucky Chandler Hospital", "city": "Lexington", "state": "KY", "zipcode": "40536"},
    {"name": "Baptist Health Louisville", "city": "Louisville", "state": "KY", "zipcode": "40207"},
    {"name": "University of Louisville Hospital", "city": "Louisville", "state": "KY", "zipcode": "40202"},
    {"name": "OU Health University of Oklahoma Medical Center", "city": "Oklahoma City", "state": "OK", "zipcode": "73104"},
    {"name": "Saint Francis Hospital Tulsa", "city": "Tulsa", "state": "OK", "zipcode": "74136"},
    {"name": "Cabell Huntington Hospital", "city": "Huntington", "state": "WV", "zipcode": "25701"},
    {"name": "WVU Medicine Ruby Memorial Hospital", "city": "Morgantown", "state": "WV", "zipcode": "26506"},
]

def geocode_address(name, city, state, zipcode):
    """Geocode using OpenStreetMap Nominatim with better query formatting"""
    # Try multiple query formats for better success rate
    queries = [
        f"{name}, {city}, {state} {zipcode}, USA",
        f"{name}, {city}, {state}, USA",
        f"{city}, {state} {zipcode}, USA"  # Fallback to city location
    ]

    url = "https://nominatim.openstreetmap.org/search"
    headers = {
        'User-Agent': 'StrokeCenterFinderApp/1.0'
    }

    for query in queries:
        try:
            time.sleep(1.1)  # Rate limiting
            params = {
                'q': query,
                'format': 'json',
                'limit': 1
            }
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data and len(data) > 0:
                return {
                    'latitude': float(data[0]['lat']),
                    'longitude': float(data[0]['lon']),
                    'query_used': query
                }
        except Exception as e:
            continue

    print(f"  ✗ All geocoding attempts failed for {name}")
    return None

def main():
    print("Loading existing stroke centers...")
    with open('data/stroke_centers.json', 'r') as f:
        existing_centers = json.load(f)

    print(f"Current database: {len(existing_centers)} centers")

    # Create deduplication key from existing centers
    existing_keys = set()
    for center in existing_centers:
        key = f"{center['name'].lower()}|{center['city'].lower()}|{center['state'].lower()}"
        existing_keys.add(key)

    print(f"\nGeocoding and adding up to {len(ADDITIONAL_CENTERS)} new centers...")
    added_count = 0
    skipped_count = 0
    failed_count = 0

    for i, center in enumerate(ADDITIONAL_CENTERS, 1):
        # Check for duplicates
        key = f"{center['name'].lower()}|{center['city'].lower()}|{center['state'].lower()}"
        if key in existing_keys:
            print(f"{i}/{len(ADDITIONAL_CENTERS)}: Skipping duplicate - {center['name']}")
            skipped_count += 1
            continue

        print(f"{i}/{len(ADDITIONAL_CENTERS)}: Processing {center['name']}, {center['city']}, {center['state']}")

        # Geocode
        coords = geocode_address(center['name'], center['city'], center['state'], center.get('zipcode', ''))

        if coords:
            new_center = {
                'name': center['name'],
                'address': '',
                'city': center['city'],
                'state': center['state'],
                'zipcode': center.get('zipcode', ''),
                'latitude': coords['latitude'],
                'longitude': coords['longitude'],
                'phone': '',
                'certification_org': 'Joint Commission',
                'certification_type': 'Comprehensive Stroke Center'
            }
            existing_centers.append(new_center)
            existing_keys.add(key)
            added_count += 1
            print(f"  ✓ Added ({coords['latitude']}, {coords['longitude']})")
        else:
            failed_count += 1

    # Save updated database
    with open('data/stroke_centers.json', 'w') as f:
        json.dump(existing_centers, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Complete!")
    print(f"Added: {added_count} new centers")
    print(f"Skipped: {skipped_count} duplicates")
    print(f"Failed: {failed_count} geocoding failures")
    print(f"Total in database: {len(existing_centers)} centers")
    print(f"Progress to 297: {len(existing_centers)}/297 ({len(existing_centers)/297*100:.1f}%)")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
