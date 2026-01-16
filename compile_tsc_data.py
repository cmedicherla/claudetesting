"""
Script to compile Thrombectomy-Capable Stroke Center (TSC) data

This script helps gather TSC data from various sources since there's no unified national database.

Data Sources:
1. Joint Commission Quality Check - https://www.qualitycheck.org/
2. State Health Departments
3. Hospital press releases and news

Since Joint Commission doesn't provide a bulk download API, we'll compile from:
- State health department lists
- Manual searches
- News articles about certifications
"""

import json
import requests
from typing import List, Dict

# Known TSCs from recent news and announcements (2023-2026)
KNOWN_TSCS = [
    {
        "name": "Bridgeport Hospital",
        "city": "Bridgeport",
        "state": "CT",
        "zipcode": "06610",
        "latitude": 41.1865,
        "longitude": -73.2007,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.bridgeporthospital.org/news/bridgeport-hospital-certified-by-joint-commission-as-thrombectomy-capable-stroke-center"
    },
    {
        "name": "West Tennessee Healthcare",
        "city": "Jackson",
        "state": "TN",
        "zipcode": "38305",
        "latitude": 35.6145,
        "longitude": -88.8139,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.wbbjtv.com/2026/01/08/west-tennessee-healthcare-awarded-thrombectomy-capable-stroke-certification-from-the-joint-commission/"
    },
    {
        "name": "Phelps Hospital",
        "city": "Sleepy Hollow",
        "state": "NY",
        "zipcode": "10591",
        "latitude": 41.0862,
        "longitude": -73.8629,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.northwell.edu/news/the-latest/phelps-hospital-earns-advanced-thrombectomy-capable-stroke-center-certification"
    },
    {
        "name": "Centra Virginia Baptist Hospital",
        "city": "Lynchburg",
        "state": "VA",
        "zipcode": "24502",
        "latitude": 37.4138,
        "longitude": -79.1422,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.centrahealth.com/news/2023-05-23/joint-commission-awards-centra-thrombectomy-capable-stroke-center-certification"
    },
    {
        "name": "Mount Sinai Queens",
        "city": "Long Island City",
        "state": "NY",
        "zipcode": "11102",
        "latitude": 40.7614,
        "longitude": -73.9509,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.mountsinai.org/about/newsroom/2021/mount-sinai-queens-earns-prestigious-thrombectomy-capable-stroke-certification-from-joint-commission"
    },
    {
        "name": "NYC Health + Hospitals/South Brooklyn Health",
        "city": "Brooklyn",
        "state": "NY",
        "zipcode": "11235",
        "latitude": 40.5888,
        "longitude": -73.9493,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.nychealthandhospitals.org/pressrelease/nyc-health-hospitals-south-brooklyn-health-recognized-for-highest-quality-stroke-care-by-the-joint-commission/"
    },
    {
        "name": "Centennial Hills Hospital",
        "city": "Las Vegas",
        "state": "NV",
        "zipcode": "89149",
        "latitude": 36.2820,
        "longitude": -115.3018,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.centennialhillshospital.com/about/news/certified-thrombectomy-stroke-joint-commission"
    },
    {
        "name": "Trinity Health Oakland Hospital",
        "city": "Pontiac",
        "state": "MI",
        "zipcode": "48341",
        "latitude": 42.6389,
        "longitude": -83.2911,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.michigan.gov/mdhhs/keep-mi-healthy/communicablediseases/epidemiology/chronicepi/stroke/participating-hospitals",
        "note": "First TSC in the nation (March 2018)"
    }
]

def save_tsc_data(output_file="data/thrombectomy_centers.json"):
    """Save compiled TSC data to JSON file"""
    with open(output_file, 'w') as f:
        json.dump(KNOWN_TSCS, f, indent=2)
    print(f"Saved {len(KNOWN_TSCS)} TSC centers to {output_file}")

def get_geocode(address: str) -> tuple:
    """
    Get latitude/longitude from address using Nominatim (OpenStreetMap)
    Free tier, no API key required
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "StrokeDesertMap/1.0"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception as e:
        print(f"Geocoding error for {address}: {e}")

    return None, None

def add_tsc_manual():
    """
    Interactive function to manually add TSC centers
    Useful for adding centers from state lists or news articles
    """
    print("Manual TSC Entry")
    print("================")

    center = {}
    center["name"] = input("Hospital Name: ")
    center["city"] = input("City: ")
    center["state"] = input("State (2-letter code): ").upper()
    center["zipcode"] = input("Zipcode: ")

    # Try to geocode
    address = f"{center['name']}, {center['city']}, {center['state']} {center['zipcode']}"
    lat, lon = get_geocode(address)

    if lat and lon:
        center["latitude"] = lat
        center["longitude"] = lon
        print(f"Geocoded: {lat}, {lon}")
    else:
        center["latitude"] = float(input("Latitude: "))
        center["longitude"] = float(input("Longitude: "))

    center["certification_org"] = "Joint Commission"
    center["certification_type"] = "Thrombectomy-Capable Stroke Center"
    center["source"] = input("Source URL (optional): ") or "Manual entry"

    KNOWN_TSCS.append(center)
    print(f"\nAdded: {center['name']}")
    print(f"Total TSCs: {len(KNOWN_TSCS)}")

def print_state_instructions():
    """Print instructions for gathering data from state health departments"""
    print("""
State Health Department Data Collection Instructions:
====================================================

1. Indiana: https://www.in.gov/health/trauma-system/indiana-stroke-centers/
   - Download their published list
   - Filter for TSC certification type

2. Michigan: https://www.michigan.gov/mdhhs/keep-mi-healthy/communicablediseases/epidemiology/chronicepi/stroke/participating-hospitals
   - Review participating hospitals
   - Check for TSC designation

3. North Carolina: https://info.ncdhhs.gov/dhsr/ahc/pdf/strokecenters.pdf
   - Download PDF
   - Extract TSC entries

4. New York: https://www.health.ny.gov/diseases/cardiovascular/stroke/
   - Check designated stroke centers
   - Filter for TSC level

5. Connecticut: https://portal.ct.gov/dph/emergency-medical-services/ems/certified-stroke-centers
   - Review certified centers
   - Note TSC designations

For each state, compile hospital names, cities, and look up coordinates using geocoding.
""")

if __name__ == "__main__":
    print(f"Currently have {len(KNOWN_TSCS)} TSC centers compiled")
    print("\nOptions:")
    print("1. Save current data to JSON")
    print("2. Add a TSC manually")
    print("3. Show state data collection instructions")

    choice = input("\nChoice (1/2/3): ")

    if choice == "1":
        save_tsc_data("data/thrombectomy_centers.json")
    elif choice == "2":
        add_tsc_manual()
        save_again = input("Save updated data? (y/n): ")
        if save_again.lower() == 'y':
            save_tsc_data("data/thrombectomy_centers.json")
    elif choice == "3":
        print_state_instructions()
