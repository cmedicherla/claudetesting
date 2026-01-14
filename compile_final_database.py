#!/usr/bin/env python3
"""
Final Comprehensive Stroke Center Database - Targeting ~162 centers (54.5% of 297)
Combines: FL (49), PA (14), NY (26), TX (48), + Major Academic Centers (54)
"""

import json
import requests
import time

# New York Comprehensive Stroke Centers (26) - Official NYS Data
NY_CENTERS = [
    {"name": "Albany Medical Center Hospital", "city": "Albany", "state": "NY", "zipcode": "12208"},
    {"name": "Bellevue Hospital Center", "city": "New York", "state": "NY", "zipcode": "10016"},
    {"name": "Buffalo General Medical Center", "city": "Buffalo", "state": "NY", "zipcode": "14203"},
    {"name": "Crouse Hospital", "city": "Syracuse", "state": "NY", "zipcode": "13210"},
    {"name": "Good Samaritan Hospital Medical Center", "city": "West Islip", "state": "NY", "zipcode": "11795"},
    {"name": "Jamaica Hospital Medical Center", "city": "Jamaica", "state": "NY", "zipcode": "11418"},
    {"name": "Lenox Hill Hospital", "city": "New York", "state": "NY", "zipcode": "10021"},
    {"name": "Maimonides Medical Center", "city": "Brooklyn", "state": "NY", "zipcode": "11219"},
    {"name": "Mercy Hospital of Buffalo", "city": "Buffalo", "state": "NY", "zipcode": "14220"},
    {"name": "Montefiore Medical Center - Henry & Lucy Moses Div", "city": "Bronx", "state": "NY", "zipcode": "10467"},
    {"name": "Mount Sinai Hospital", "city": "New York", "state": "NY", "zipcode": "10029"},
    {"name": "New York-Presbyterian Hospital - Columbia", "city": "New York", "state": "NY", "zipcode": "10032"},
    {"name": "New York-Presbyterian Hospital - New York Weill", "city": "New York", "state": "NY", "zipcode": "10021"},
    {"name": "North Shore University Hospital", "city": "Manhasset", "state": "NY", "zipcode": "11030"},
    {"name": "NYU Langone Hospital-Brooklyn", "city": "Brooklyn", "state": "NY", "zipcode": "11220"},
    {"name": "NYU Langone Hospital-Long Island", "city": "Mineola", "state": "NY", "zipcode": "11501"},
    {"name": "NYU Langone Hospitals", "city": "New York", "state": "NY", "zipcode": "10016"},
    {"name": "Rochester General Hospital", "city": "Rochester", "state": "NY", "zipcode": "14621"},
    {"name": "South Shore University Hospital", "city": "Bay Shore", "state": "NY", "zipcode": "11706"},
    {"name": "Staten Island University Hosp-North", "city": "Staten Island", "state": "NY", "zipcode": "10305"},
    {"name": "Stony Brook University Hospital", "city": "Stony Brook", "state": "NY", "zipcode": "11794"},
    {"name": "Strong Memorial Hospital", "city": "Rochester", "state": "NY", "zipcode": "14642"},
    {"name": "United Health Services Hospitals Inc. - Wilson", "city": "Johnson City", "state": "NY", "zipcode": "13790"},
    {"name": "University Hospital SUNY Health Science Center", "city": "Syracuse", "state": "NY", "zipcode": "13210"},
    {"name": "Westchester Medical Center", "city": "Valhalla", "state": "NY", "zipcode": "10595"},
    {"name": "Wynn Hospital", "city": "Utica", "state": "NY", "zipcode": "13502"},
]

# Texas Comprehensive Stroke Centers (48) - Official TX DSHS Data
TX_CENTERS = [
    {"name": "Baylor Scott & White Medical Center - Grapevine", "city": "Grapevine", "state": "TX", "zipcode": "76051"},
    {"name": "Baylor Scott & White Medical Center - Plano", "city": "Plano", "state": "TX", "zipcode": "75093"},
    {"name": "Baylor Scott & White Medical Center - Temple", "city": "Temple", "state": "TX", "zipcode": "76508"},
    {"name": "Baylor University Medical Center", "city": "Dallas", "state": "TX", "zipcode": "75246"},
    {"name": "CHI St Lukes Health Baylor College of Medicine Medical Center", "city": "Houston", "state": "TX", "zipcode": "77030"},
    {"name": "Christus Mother Frances Hospital - Tyler", "city": "Tyler", "state": "TX", "zipcode": "75702"},
    {"name": "Christus Spohn Hospital Corpus Christi Shoreline", "city": "Corpus Christi", "state": "TX", "zipcode": "78404"},
    {"name": "Covenant Medical Center", "city": "Lubbock", "state": "TX", "zipcode": "79410"},
    {"name": "Dell Seton Medical Center at the University of Texas", "city": "Austin", "state": "TX", "zipcode": "78701"},
    {"name": "Doctors Hospital at Renaissance", "city": "Edinburg", "state": "TX", "zipcode": "78539"},
    {"name": "Harris Health Ben Taub Hospital", "city": "Houston", "state": "TX", "zipcode": "77030"},
    {"name": "HCA Houston Healthcare Clear Lake", "city": "Webster", "state": "TX", "zipcode": "77598"},
    {"name": "HCA Houston Healthcare Conroe", "city": "Conroe", "state": "TX", "zipcode": "77304"},
    {"name": "HCA Houston Healthcare Kingwood", "city": "Kingwood", "state": "TX", "zipcode": "77339"},
    {"name": "HCA Houston Healthcare Northwest", "city": "Houston", "state": "TX", "zipcode": "77090"},
    {"name": "Houston Methodist Hospital", "city": "Houston", "state": "TX", "zipcode": "77030"},
    {"name": "Houston Methodist Sugar Land Hospital", "city": "Sugar Land", "state": "TX", "zipcode": "77479"},
    {"name": "Houston Methodist The Woodlands Hospital", "city": "The Woodlands", "state": "TX", "zipcode": "77380"},
    {"name": "Houston Methodist Willowbrook Hospital", "city": "Houston", "state": "TX", "zipcode": "77070"},
    {"name": "John Peter Smith Hospital", "city": "Fort Worth", "state": "TX", "zipcode": "76104"},
    {"name": "Medical City Arlington", "city": "Arlington", "state": "TX", "zipcode": "76015"},
    {"name": "Medical City Dallas Hospital", "city": "Dallas", "state": "TX", "zipcode": "75230"},
    {"name": "Medical City Fort Worth", "city": "Fort Worth", "state": "TX", "zipcode": "76104"},
    {"name": "Medical City Plano", "city": "Plano", "state": "TX", "zipcode": "75075"},
    {"name": "Memorial Hermann - Texas Medical Center", "city": "Houston", "state": "TX", "zipcode": "77030"},
    {"name": "Memorial Hermann Memorial City Medical Center", "city": "Houston", "state": "TX", "zipcode": "77024"},
    {"name": "Memorial Hermann Southwest Hospital", "city": "Houston", "state": "TX", "zipcode": "77074"},
    {"name": "Memorial Hermann The Woodlands Medical Center", "city": "The Woodlands", "state": "TX", "zipcode": "77380"},
    {"name": "Methodist Dallas Medical Center", "city": "Dallas", "state": "TX", "zipcode": "75203"},
    {"name": "Methodist Hospital", "city": "San Antonio", "state": "TX", "zipcode": "78229"},
    {"name": "Methodist Richardson Medical Center", "city": "Richardson", "state": "TX", "zipcode": "75082"},
    {"name": "Michael E DeBakey VA Medical Center", "city": "Houston", "state": "TX", "zipcode": "77030"},
    {"name": "Parkland Memorial Hospital", "city": "Dallas", "state": "TX", "zipcode": "75235"},
    {"name": "South Texas Health System McAllen", "city": "McAllen", "state": "TX", "zipcode": "78503"},
    {"name": "St David's Medical Center", "city": "Austin", "state": "TX", "zipcode": "78705"},
    {"name": "St Lukes Baptist Hospital", "city": "San Antonio", "state": "TX", "zipcode": "78229"},
    {"name": "St Lukes The Woodlands Hospital", "city": "The Woodlands", "state": "TX", "zipcode": "77384"},
    {"name": "Texas Health Harris Methodist Hospital Fort Worth", "city": "Fort Worth", "state": "TX", "zipcode": "76104"},
    {"name": "Texas Health Presbyterian Hospital Dallas", "city": "Dallas", "state": "TX", "zipcode": "75231"},
    {"name": "Texas Health Presbyterian Hospital Plano", "city": "Plano", "state": "TX", "zipcode": "75093"},
    {"name": "The Hospitals of Providence Sierra Campus", "city": "El Paso", "state": "TX", "zipcode": "79915"},
    {"name": "University Hospital", "city": "San Antonio", "state": "TX", "zipcode": "78229"},
    {"name": "University Medical Center of El Paso", "city": "El Paso", "state": "TX", "zipcode": "79905"},
    {"name": "University of Texas Medical Branch", "city": "Galveston", "state": "TX", "zipcode": "77555"},
    {"name": "University of Texas Medical Branch - Clear Lake Campus", "city": "Webster", "state": "TX", "zipcode": "77598"},
    {"name": "UT Health East Texas Tyler Regional Hospital", "city": "Tyler", "state": "TX", "zipcode": "75701"},
    {"name": "Valley Baptist Medical Center", "city": "Harlingen", "state": "TX", "zipcode": "78550"},
    {"name": "William P Clements University Hospital", "city": "Dallas", "state": "TX", "zipcode": "75390"},
]


def geocode_address(name, city, state, zipcode):
    """Geocode using OpenStreetMap Nominatim API (free)"""
    try:
        query = f"{name}, {city}, {state} {zipcode}, USA"
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": query,
            "format": "json",
            "limit": 1,
            "countrycodes": "us"
        }
        headers = {"User-Agent": "StrokeCenterFinder/2.0"}

        response = requests.get(url, params=params, headers=headers, timeout=10)
        time.sleep(1.1)  # Rate limiting

        if response.status_code == 200:
            results = response.json()
            if results:
                return float(results[0]['lat']), float(results[0]['lon'])

        # Fallback: just city, state, zip
        query = f"{city}, {state} {zipcode}, USA"
        params["q"] = query
        response = requests.get(url, params=params, headers=headers, timeout=10)
        time.sleep(1.1)

        if response.status_code == 200:
            results = response.json()
            if results:
                return float(results[0]['lat']), float(results[0]['lon'])
    except Exception as e:
        print(f"  ✗ Geocoding failed for {name}: {e}")

    return None, None


def compile_final_database():
    """Compile final comprehensive database"""
    print("="*80)
    print("FINAL COMPREHENSIVE STROKE CENTER DATABASE COMPILER")
    print("Targeting ~162 centers (54.5% of 297 total US centers)")
    print("="*80)
    print()

    # Load existing data
    try:
        with open('data/stroke_centers.json', 'r') as f:
            existing = json.load(f)
        print(f"✓ Loaded {len(existing)} existing centers")
    except:
        existing = []
        print("✗ No existing data found, starting fresh")

    # Combine new data
    new_centers = NY_CENTERS + TX_CENTERS
    print(f"✓ Adding {len(NY_CENTERS)} New York centers")
    print(f"✓ Adding {len(TX_CENTERS)} Texas centers")
    print()

    # Deduplicate by name+city+state
    all_centers_dict = {}

    # Add existing first
    for center in existing:
        key = f"{center['name']}|{center['city']}|{center['state']}".lower()
        all_centers_dict[key] = center

    # Add new (will overwrite if duplicate)
    processed = 0
    for center in new_centers:
        key = f"{center['name']}|{center['city']}|{center['state']}".lower()
        if key not in all_centers_dict:
            processed += 1
            print(f"[{processed}] Processing: {center['name']}, {center['city']}, {center['state']}")

            lat, lon = geocode_address(center['name'], center['city'], center['state'], center['zipcode'])

            if lat and lon:
                all_centers_dict[key] = {
                    "name": center['name'],
                    "address": center.get('address', ''),
                    "city": center['city'],
                    "state": center['state'],
                    "zipcode": center['zipcode'],
                    "latitude": lat,
                    "longitude": lon,
                    "phone": center.get('phone', ''),
                    "certification_org": "Joint Commission/DNV",
                    "certification_type": "Comprehensive Stroke Center"
                }
                print(f"  ✓ Geocoded: ({lat}, {lon})")
            else:
                print(f"  ⚠ Skipping - geocoding failed")

    # Convert back to list
    final_centers = list(all_centers_dict.values())

    print()
    print("="*80)
    print(f"COMPILATION COMPLETE: {len(final_centers)} unique centers")
    print("="*80)
    print()

    # Save
    with open('data/stroke_centers.json', 'w') as f:
        json.dump(final_centers, f, indent=2)

    print(f"✓ Data saved to: data/stroke_centers.json")
    print(f"✓ Total comprehensive stroke centers: {len(final_centers)}")

    # Statistics
    states = {}
    for center in final_centers:
        state = center['state']
        states[state] = states.get(state, 0) + 1

    print()
    print(f"Coverage: {len(states)} states")
    print()
    print("Top 10 states by center count:")
    for state, count in sorted(states.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {state}: {count} centers")

    print()
    print(f"Coverage: {len(final_centers) / 297 * 100:.1f}% of estimated 297 total US comprehensive stroke centers")

    return final_centers


if __name__ == "__main__":
    try:
        centers = compile_final_database()
        print("\n✓ Success! Database expanded with NY + TX official data.")
        print("  Refresh index.html to see all centers.")
    except KeyboardInterrupt:
        print("\n\nProcess interrupted")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
