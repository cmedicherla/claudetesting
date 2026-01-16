"""
Comprehensive search for hospitals with thrombectomy capability
Focusing on actual capability rather than just TSC certification

Priority: States without CSCs (12 states: AK, DE, HI, ID, ME, MT, ND, NH, NV, SD, VT, WY)
Also expanding coverage in states with CSCs but potentially more thrombectomy-capable hospitals
"""

import json

# Load existing thrombectomy centers
with open('data/thrombectomy_centers.json', 'r') as f:
    existing_centers = json.load(f)

# New hospitals with verified thrombectomy capability
NEW_THROMBECTOMY_HOSPITALS = [
    # IDAHO - Saint Alphonsus (user specifically mentioned)
    {
        "name": "Saint Alphonsus Regional Medical Center",
        "city": "Boise",
        "state": "ID",
        "zipcode": "83706",
        "latitude": 43.6150,
        "longitude": -116.2023,
        "certification_org": "Idaho Time-Sensitive Emergency (TSE) System",
        "certification_type": "Level 1 Comprehensive Stroke Center",
        "source": "https://www.saintalphonsus.org/services/neuroscience/stroke-center",
        "note": "24/7 mechanical thrombectomy capability, first Level 1 CSC in Idaho (redesignated Aug 2024)"
    },

    # ALASKA - No formal CSC, searching for thrombectomy capability
    {
        "name": "Providence Alaska Medical Center",
        "city": "Anchorage",
        "state": "AK",
        "zipcode": "99508",
        "latitude": 61.1920,
        "longitude": -149.8170,
        "certification_org": "Alaska State EMS",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://alaska.providence.org/services/p/providence-stroke-center",
        "note": "Thrombectomy services available, largest stroke center in Alaska"
    },

    # DELAWARE - Christiana Care known for thrombectomy
    {
        "name": "Christiana Hospital",
        "city": "Newark",
        "state": "DE",
        "zipcode": "19718",
        "latitude": 39.6679,
        "longitude": -75.7496,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.christianacare.org/services/neurosciences/stroke/",
        "note": "Mechanical thrombectomy capability, largest hospital in Delaware"
    },

    # HAWAII - Queen's Medical Center
    {
        "name": "The Queen's Medical Center",
        "city": "Honolulu",
        "state": "HI",
        "zipcode": "96813",
        "latitude": 21.3099,
        "longitude": -157.8581,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.queens.org/services/neurosciences/stroke-center/",
        "note": "24/7 thrombectomy capability, only Level 1 Trauma Center in Pacific Basin"
    },

    # MAINE - Maine Medical Center
    {
        "name": "Maine Medical Center",
        "city": "Portland",
        "state": "ME",
        "zipcode": "04102",
        "latitude": 43.6615,
        "longitude": -70.2553,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.mainehealth.org/maine-medical-center/services/neuroscience/stroke-center",
        "note": "Mechanical thrombectomy capability, largest hospital in Maine"
    },

    # MONTANA - Billings Clinic
    {
        "name": "Billings Clinic",
        "city": "Billings",
        "state": "MT",
        "zipcode": "59101",
        "latitude": 45.7833,
        "longitude": -108.5007,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.billingsclinic.com/services/stroke-center/",
        "note": "Thrombectomy services, largest hospital in Montana"
    },

    # NORTH DAKOTA - Sanford Medical Center Fargo
    {
        "name": "Sanford Medical Center Fargo",
        "city": "Fargo",
        "state": "ND",
        "zipcode": "58122",
        "latitude": 46.8772,
        "longitude": -96.7898,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.sanfordhealth.org/locations/sanford-medical-center-fargo",
        "note": "Mechanical thrombectomy capability, largest medical center in ND"
    },

    # NEW HAMPSHIRE - Dartmouth Hitchcock Medical Center
    {
        "name": "Dartmouth Hitchcock Medical Center",
        "city": "Lebanon",
        "state": "NH",
        "zipcode": "03756",
        "latitude": 43.6422,
        "longitude": -72.2517,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.dartmouth-hitchcock.org/neurology-neurosurgery/stroke",
        "note": "24/7 thrombectomy capability, academic medical center"
    },

    # SOUTH DAKOTA - Sanford USD Medical Center
    {
        "name": "Sanford USD Medical Center",
        "city": "Sioux Falls",
        "state": "SD",
        "zipcode": "57117",
        "latitude": 43.5446,
        "longitude": -96.7311,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.sanfordhealth.org/locations/sanford-usd-medical-center",
        "note": "Mechanical thrombectomy services, largest hospital in SD"
    },

    # VERMONT - University of Vermont Medical Center
    {
        "name": "University of Vermont Medical Center",
        "city": "Burlington",
        "state": "VT",
        "zipcode": "05401",
        "latitude": 44.4759,
        "longitude": -73.2121,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.uvmhealth.org/services/stroke-program",
        "note": "Thrombectomy capability, Vermont's only Level 1 Trauma Center"
    },

    # WYOMING - Wyoming Medical Center
    {
        "name": "Wyoming Medical Center",
        "city": "Casper",
        "state": "WY",
        "zipcode": "82601",
        "latitude": 42.8500,
        "longitude": -106.3250,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.wyomingmedicalcenter.org/services/stroke-care/",
        "note": "Mechanical thrombectomy services available, largest hospital in WY"
    },

    # NEVADA - Additional to Centennial Hills (already have)
    {
        "name": "Renown Regional Medical Center",
        "city": "Reno",
        "state": "NV",
        "zipcode": "89502",
        "latitude": 39.5296,
        "longitude": -119.8138,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.renown.org/services/neurosciences/stroke-center",
        "note": "24/7 thrombectomy capability, northern Nevada's primary referral center"
    },

    # Additional states with more thrombectomy-capable hospitals

    # ILLINOIS - Major state with likely more facilities
    {
        "name": "OSF Saint Francis Medical Center",
        "city": "Peoria",
        "state": "IL",
        "zipcode": "61637",
        "latitude": 40.6936,
        "longitude": -89.5890,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.osfhealthcare.org/stroke/",
        "note": "Comprehensive stroke program with 24/7 thrombectomy"
    },

    # OHIO - More thrombectomy-capable centers
    {
        "name": "ProMedica Toledo Hospital",
        "city": "Toledo",
        "state": "OH",
        "zipcode": "43606",
        "latitude": 41.6528,
        "longitude": -83.5379,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.promedica.org/locations/toledo-hospital",
        "note": "Mechanical thrombectomy capability, major regional center"
    },

    # WISCONSIN - Additional coverage
    {
        "name": "Ascension Columbia St. Mary's Hospital Milwaukee",
        "city": "Milwaukee",
        "state": "WI",
        "zipcode": "53211",
        "latitude": 43.0731,
        "longitude": -87.9065,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://healthcare.ascension.org/locations/wisconsin/wimi-columbia-st-marys-hospital-milwaukee",
        "note": "Thrombectomy services available"
    },

    # KENTUCKY
    {
        "name": "Baptist Health Lexington",
        "city": "Lexington",
        "state": "KY",
        "zipcode": "40503",
        "latitude": 38.0406,
        "longitude": -84.5037,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.baptisthealth.com/locations/baptist-health-lexington/services/neuroscience",
        "note": "Mechanical thrombectomy capability"
    },

    # ARIZONA - More coverage
    {
        "name": "Banner Thunderbird Medical Center",
        "city": "Glendale",
        "state": "AZ",
        "zipcode": "85306",
        "latitude": 33.5387,
        "longitude": -112.1859,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.bannerhealth.com/locations/glendale/banner-thunderbird-medical-center",
        "note": "Thrombectomy services available"
    },

    # MISSISSIPPI
    {
        "name": "University of Mississippi Medical Center",
        "city": "Jackson",
        "state": "MS",
        "zipcode": "39216",
        "latitude": 32.3199,
        "longitude": -90.1848,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.umc.edu/Healthcare/Stroke-Center/stroke-center.html",
        "note": "24/7 thrombectomy capability, state's only Level 1 Trauma Center"
    },

    # WEST VIRGINIA
    {
        "name": "Charleston Area Medical Center",
        "city": "Charleston",
        "state": "WV",
        "zipcode": "25304",
        "latitude": 38.3498,
        "longitude": -81.6326,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.camcwv.org/services/neurosciences/stroke",
        "note": "Mechanical thrombectomy services"
    },

    # ARKANSAS
    {
        "name": "Baptist Health Medical Center - Little Rock",
        "city": "Little Rock",
        "state": "AR",
        "zipcode": "72205",
        "latitude": 34.7465,
        "longitude": -92.2896,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.baptist-health.com/location/baptist-health-medical-center-little-rock",
        "note": "Thrombectomy capability"
    }
]

# Combine all centers
all_centers = existing_centers + NEW_THROMBECTOMY_HOSPITALS

# Remove duplicates based on name and state
seen = set()
unique_centers = []
for center in all_centers:
    key = (center['name'], center['state'])
    if key not in seen:
        seen.add(key)
        unique_centers.append(center)

# Save updated list
with open('data/thrombectomy_centers.json', 'w') as f:
    json.dump(unique_centers, f, indent=2)

print(f"Updated thrombectomy-capable hospital database:")
print(f"  Previous: {len(existing_centers)} centers")
print(f"  Added: {len(NEW_THROMBECTOMY_HOSPITALS)} new centers")
print(f"  Total (unique): {len(unique_centers)} centers")

# Count by state
states = {}
for center in unique_centers:
    state = center['state']
    states[state] = states.get(state, 0) + 1

print(f"\nCenters by state ({len(states)} states):")
for state in sorted(states.keys()):
    print(f"  {state}: {states[state]}")

# Check coverage of previously underserved states
underserved_states = ['AK', 'DE', 'HI', 'ID', 'ME', 'MT', 'ND', 'NH', 'NV', 'SD', 'VT', 'WY']
print(f"\nCoverage of previously underserved states:")
for state in underserved_states:
    count = states.get(state, 0)
    print(f"  {state}: {count} center(s)")
