#!/usr/bin/env python3
"""
Add comprehensive stroke centers from manual web research
Based on official sources and hospital websites found during research
"""

import json
import time
import requests

# Comprehensive Stroke Centers identified from web research
NEW_CENTERS = [
    # California - Los Angeles County
    {"name": "Adventist Health Glendale", "city": "Glendale", "state": "CA", "zipcode": "91206"},
    {"name": "Antelope Valley Hospital", "city": "Lancaster", "state": "CA", "zipcode": "93534"},
    {"name": "Cedars-Sinai Medical Center", "city": "Los Angeles", "state": "CA", "zipcode": "90048"},
    {"name": "MemorialCare Long Beach Medical Center", "city": "Long Beach", "state": "CA", "zipcode": "90806"},
    {"name": "PIH Health Whittier Hospital", "city": "Whittier", "state": "CA", "zipcode": "90602"},
    {"name": "Pomona Valley Hospital Medical Center", "city": "Pomona", "state": "CA", "zipcode": "91767"},
    {"name": "Providence Holy Cross Medical Center", "city": "Mission Hills", "state": "CA", "zipcode": "91345"},
    {"name": "Providence Little Company of Mary Medical Center", "city": "Torrance", "state": "CA", "zipcode": "90503"},
    {"name": "Providence Saint John's Health Center", "city": "Santa Monica", "state": "CA", "zipcode": "90404"},
    {"name": "Providence Saint Joseph Medical Center", "city": "Burbank", "state": "CA", "zipcode": "91505"},
    {"name": "Ronald Reagan UCLA Medical Center", "city": "Los Angeles", "state": "CA", "zipcode": "90095"},
    {"name": "Emanate Health Queen of the Valley Hospital", "city": "West Covina", "state": "CA", "zipcode": "91790"},
    {"name": "Los Robles Regional Medical Center", "city": "Thousand Oaks", "state": "CA", "zipcode": "91360"},

    # California - San Diego County
    {"name": "UC San Diego Health Hillcrest", "city": "San Diego", "state": "CA", "zipcode": "92103"},
    {"name": "UC San Diego Health Jacobs Medical Center", "city": "La Jolla", "state": "CA", "zipcode": "92037"},
    {"name": "Sharp Grossmont Hospital", "city": "La Mesa", "state": "CA", "zipcode": "91942"},
    {"name": "Scripps Memorial Hospital La Jolla", "city": "La Jolla", "state": "CA", "zipcode": "92037"},

    # California - Bay Area
    {"name": "UCSF Medical Center", "city": "San Francisco", "state": "CA", "zipcode": "94143"},
    {"name": "Stanford Health Care", "city": "Palo Alto", "state": "CA", "zipcode": "94305"},
    {"name": "Good Samaritan Hospital", "city": "San Jose", "state": "CA", "zipcode": "95124"},

    # Virginia
    {"name": "VCU Medical Center", "city": "Richmond", "state": "VA", "zipcode": "23298"},
    {"name": "University of Virginia Medical Center", "city": "Charlottesville", "state": "VA", "zipcode": "22908"},
    {"name": "Riverside Regional Medical Center", "city": "Newport News", "state": "VA", "zipcode": "23601"},
    {"name": "Inova Fairfax Hospital", "city": "Falls Church", "state": "VA", "zipcode": "22042"},
    {"name": "Sentara Norfolk General Hospital", "city": "Norfolk", "state": "VA", "zipcode": "23507"},
    {"name": "Carilion Roanoke Memorial Hospital", "city": "Roanoke", "state": "VA", "zipcode": "24014"},

    # Washington State
    {"name": "Harborview Medical Center", "city": "Seattle", "state": "WA", "zipcode": "98104"},
    {"name": "University of Washington Medical Center", "city": "Seattle", "state": "WA", "zipcode": "98195"},
    {"name": "Virginia Mason Medical Center", "city": "Seattle", "state": "WA", "zipcode": "98101"},
    {"name": "Swedish Medical Center", "city": "Seattle", "state": "WA", "zipcode": "98122"},
    {"name": "Providence Sacred Heart Medical Center", "city": "Spokane", "state": "WA", "zipcode": "99204"},

    # Tennessee
    {"name": "Vanderbilt University Medical Center", "city": "Nashville", "state": "TN", "zipcode": "37232"},
    {"name": "University of Tennessee Medical Center", "city": "Knoxville", "state": "TN", "zipcode": "37920"},
    {"name": "TriStar Skyline Medical Center", "city": "Nashville", "state": "TN", "zipcode": "37207"},
    {"name": "Fort Sanders Regional Medical Center", "city": "Knoxville", "state": "TN", "zipcode": "37916"},
    {"name": "Ascension Saint Thomas Hospital West", "city": "Nashville", "state": "TN", "zipcode": "37205"},
    {"name": "Regional One Health", "city": "Memphis", "state": "TN", "zipcode": "38103"},

    # North Carolina
    {"name": "Duke University Hospital", "city": "Durham", "state": "NC", "zipcode": "27710"},
    {"name": "Wake Forest Baptist Medical Center", "city": "Winston-Salem", "state": "NC", "zipcode": "27157"},
    {"name": "Atrium Health Carolinas Medical Center", "city": "Charlotte", "state": "NC", "zipcode": "28203"},
    {"name": "UNC Medical Center", "city": "Chapel Hill", "state": "NC", "zipcode": "27514"},
    {"name": "Vidant Medical Center", "city": "Greenville", "state": "NC", "zipcode": "27834"},
    {"name": "Mission Hospital", "city": "Asheville", "state": "NC", "zipcode": "28801"},
    {"name": "Novant Health Forsyth Medical Center", "city": "Winston-Salem", "state": "NC", "zipcode": "27103"},

    # Georgia
    {"name": "Emory University Hospital", "city": "Atlanta", "state": "GA", "zipcode": "30322"},
    {"name": "Grady Memorial Hospital", "city": "Atlanta", "state": "GA", "zipcode": "30303"},
    {"name": "Wellstar Kennestone Hospital", "city": "Marietta", "state": "GA", "zipcode": "30060"},
    {"name": "Northside Hospital", "city": "Atlanta", "state": "GA", "zipcode": "30342"},
    {"name": "Piedmont Atlanta Hospital", "city": "Atlanta", "state": "GA", "zipcode": "30309"},
    {"name": "Augusta University Medical Center", "city": "Augusta", "state": "GA", "zipcode": "30912"},

    # Ohio
    {"name": "Cleveland Clinic", "city": "Cleveland", "state": "OH", "zipcode": "44195"},
    {"name": "University Hospitals Cleveland Medical Center", "city": "Cleveland", "state": "OH", "zipcode": "44106"},
    {"name": "Ohio State University Wexner Medical Center", "city": "Columbus", "state": "OH", "zipcode": "43210"},
    {"name": "UC Health University of Cincinnati Medical Center", "city": "Cincinnati", "state": "OH", "zipcode": "45219"},
    {"name": "MetroHealth Medical Center", "city": "Cleveland", "state": "OH", "zipcode": "44109"},
    {"name": "Miami Valley Hospital", "city": "Dayton", "state": "OH", "zipcode": "45409"},
    {"name": "Mercy Health St. Vincent Medical Center", "city": "Toledo", "state": "OH", "zipcode": "43608"},
    {"name": "OhioHealth Riverside Methodist Hospital", "city": "Columbus", "state": "OH", "zipcode": "43214"},

    # Michigan
    {"name": "University of Michigan Health", "city": "Ann Arbor", "state": "MI", "zipcode": "48109"},
    {"name": "Henry Ford Hospital", "city": "Detroit", "state": "MI", "zipcode": "48202"},
    {"name": "Beaumont Hospital Royal Oak", "city": "Royal Oak", "state": "MI", "zipcode": "48073"},
    {"name": "Spectrum Health Butterworth Hospital", "city": "Grand Rapids", "state": "MI", "zipcode": "49503"},
    {"name": "Detroit Receiving Hospital", "city": "Detroit", "state": "MI", "zipcode": "48201"},
    {"name": "Sparrow Hospital", "city": "Lansing", "state": "MI", "zipcode": "48912"},

    # Illinois
    {"name": "Northwestern Memorial Hospital", "city": "Chicago", "state": "IL", "zipcode": "60611"},
    {"name": "Rush University Medical Center", "city": "Chicago", "state": "IL", "zipcode": "60612"},
    {"name": "University of Chicago Medical Center", "city": "Chicago", "state": "IL", "zipcode": "60637"},
    {"name": "Advocate Christ Medical Center", "city": "Oak Lawn", "state": "IL", "zipcode": "60453"},
    {"name": "Loyola University Medical Center", "city": "Maywood", "state": "IL", "zipcode": "60153"},
    {"name": "OSF HealthCare Saint Francis Medical Center", "city": "Peoria", "state": "IL", "zipcode": "61637"},

    # Wisconsin
    {"name": "Froedtert Hospital", "city": "Milwaukee", "state": "WI", "zipcode": "53226"},
    {"name": "Aurora St. Luke's Medical Center", "city": "Milwaukee", "state": "WI", "zipcode": "53215"},
    {"name": "University of Wisconsin Hospital", "city": "Madison", "state": "WI", "zipcode": "53792"},
    {"name": "Ascension Columbia St. Mary's Hospital Milwaukee", "city": "Milwaukee", "state": "WI", "zipcode": "53211"},

    # Indiana
    {"name": "IU Health Methodist Hospital", "city": "Indianapolis", "state": "IN", "zipcode": "46202"},
    {"name": "Ascension St. Vincent Indianapolis Hospital", "city": "Indianapolis", "state": "IN", "zipcode": "46260"},
    {"name": "Indiana University Health University Hospital", "city": "Indianapolis", "state": "IN", "zipcode": "46202"},

    # Maryland
    {"name": "Johns Hopkins Hospital", "city": "Baltimore", "state": "MD", "zipcode": "21287"},
    {"name": "University of Maryland Medical Center", "city": "Baltimore", "state": "MD", "zipcode": "21201"},
    {"name": "MedStar Washington Hospital Center", "city": "Washington", "state": "DC", "zipcode": "20010"},
    {"name": "George Washington University Hospital", "city": "Washington", "state": "DC", "zipcode": "20037"},

    # Connecticut
    {"name": "Yale New Haven Hospital", "city": "New Haven", "state": "CT", "zipcode": "06510"},
    {"name": "Hartford Hospital", "city": "Hartford", "state": "CT", "zipcode": "06102"},
    {"name": "St. Francis Hospital", "city": "Hartford", "state": "CT", "zipcode": "06105"},

    # Colorado
    {"name": "UCHealth University of Colorado Hospital", "city": "Aurora", "state": "CO", "zipcode": "80045"},
    {"name": "Presbyterian St. Luke's Medical Center", "city": "Denver", "state": "CO", "zipcode": "80218"},
    {"name": "Medical Center of the Rockies", "city": "Loveland", "state": "CO", "zipcode": "80538"},

    # Arizona
    {"name": "Banner University Medical Center Phoenix", "city": "Phoenix", "state": "AZ", "zipcode": "85006"},
    {"name": "Mayo Clinic Hospital Phoenix", "city": "Phoenix", "state": "AZ", "zipcode": "85054"},
    {"name": "Banner University Medical Center Tucson", "city": "Tucson", "state": "AZ", "zipcode": "85724"},
    {"name": "HonorHealth Scottsdale Osborn Medical Center", "city": "Scottsdale", "state": "AZ", "zipcode": "85251"},
]

def geocode_address(name, city, state, zipcode):
    """Geocode using OpenStreetMap Nominatim"""
    query = f"{name}, {city}, {state} {zipcode}, USA"
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': query,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'StrokeCenterFinderApp/1.0'
    }

    try:
        time.sleep(1.1)  # Rate limiting
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data and len(data) > 0:
            return {
                'latitude': float(data[0]['lat']),
                'longitude': float(data[0]['lon'])
            }
    except Exception as e:
        print(f"  Geocoding failed for {name}: {e}")

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

    print(f"\nGeocoding and adding {len(NEW_CENTERS)} new centers...")
    added_count = 0
    skipped_count = 0

    for i, center in enumerate(NEW_CENTERS, 1):
        # Check for duplicates
        key = f"{center['name'].lower()}|{center['city'].lower()}|{center['state'].lower()}"
        if key in existing_keys:
            print(f"{i}/{len(NEW_CENTERS)}: Skipping duplicate - {center['name']}")
            skipped_count += 1
            continue

        print(f"{i}/{len(NEW_CENTERS)}: Processing {center['name']}, {center['city']}, {center['state']}")

        # Geocode
        coords = geocode_address(center['name'], center['city'], center['state'], center.get('zipcode', ''))

        if coords:
            new_center = {
                'name': center['name'],
                'address': '',  # Address not available from web research
                'city': center['city'],
                'state': center['state'],
                'zipcode': center.get('zipcode', ''),
                'latitude': coords['latitude'],
                'longitude': coords['longitude'],
                'phone': '',  # Phone not available from web research
                'certification_org': 'Joint Commission',
                'certification_type': 'Comprehensive Stroke Center'
            }
            existing_centers.append(new_center)
            existing_keys.add(key)
            added_count += 1
            print(f"  ✓ Added ({coords['latitude']}, {coords['longitude']})")
        else:
            print(f"  ✗ Failed to geocode")

    # Save updated database
    with open('data/stroke_centers.json', 'w') as f:
        json.dump(existing_centers, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Complete!")
    print(f"Added: {added_count} new centers")
    print(f"Skipped: {skipped_count} duplicates")
    print(f"Total in database: {len(existing_centers)} centers")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
