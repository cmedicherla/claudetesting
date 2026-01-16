"""
Additional TSC Centers - Expanding national coverage
Adding TSCs from Georgia, Ohio, Florida, California, and Illinois
"""

import json

# Load existing TSCs
with open('data/thrombectomy_centers.json', 'r') as f:
    existing_tscs = json.load(f)

# New TSCs to add from recent search
NEW_TSCS = [
    {
        "name": "St. Mary's Hospital",
        "city": "Athens",
        "state": "GA",
        "zipcode": "30606",
        "latitude": 33.9519,
        "longitude": -83.3676,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.stmaryshealthcaresystem.org/press-releases/st-marys-certified-georgias-first-thrombectomy-capable-stroke-center",
        "note": "First TSC in Georgia"
    },
    {
        "name": "Piedmont Columbus Regional - Midtown",
        "city": "Columbus",
        "state": "GA",
        "zipcode": "31901",
        "latitude": 32.4609,
        "longitude": -84.9877,
        "certification_org": "Georgia DPH",
        "certification_type": "Thrombectomy-Capable Stroke Center/Primary Stroke Center-PLUS",
        "source": "https://dph.georgia.gov/comprehensive-thrombectomy-primary-and-remote-treatment-stroke-centers"
    },
    {
        "name": "Bethesda North Hospital",
        "city": "Cincinnati",
        "state": "OH",
        "zipcode": "45242",
        "latitude": 39.2645,
        "longitude": -84.3733,
        "certification_org": "TriHealth",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.trihealth.com/services/trihealth-neuroscience-care/stroke-center"
    },
    {
        "name": "Holy Cross Hospital",
        "city": "Fort Lauderdale",
        "state": "FL",
        "zipcode": "33308",
        "latitude": 26.1224,
        "longitude": -80.1373,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.holy-cross.com/newsroom/press-releases/holy-cross-hospital-awarded-thrombectomy-capable-stroke-center",
        "note": "First in South Florida (March 2024)"
    },
    {
        "name": "Providence Saint John's Health Center",
        "city": "Santa Monica",
        "state": "CA",
        "zipcode": "90404",
        "latitude": 34.0194,
        "longitude": -118.4912,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.pacificneuroscienceinstitute.org/blog/stroke/finally-a-thrombectomy-capable-stroke-center-in-your-neighborhood/",
        "note": "First TSC in LA County"
    }
]

# Combine all TSCs
all_tscs = existing_tscs + NEW_TSCS

# Remove any duplicates based on name and state
seen = set()
unique_tscs = []
for tsc in all_tscs:
    key = (tsc['name'], tsc['state'])
    if key not in seen:
        seen.add(key)
        unique_tscs.append(tsc)

# Save updated list
with open('data/thrombectomy_centers.json', 'w') as f:
    json.dump(unique_tscs, f, indent=2)

print(f"Updated TSC database:")
print(f"  Previous: {len(existing_tscs)} centers")
print(f"  Added: {len(NEW_TSCS)} new centers")
print(f"  Total (unique): {len(unique_tscs)} centers")

# Count by state
states = {}
for tsc in unique_tscs:
    state = tsc['state']
    states[state] = states.get(state, 0) + 1

print(f"\nCenters by state:")
for state in sorted(states.keys()):
    print(f"  {state}: {states[state]}")
