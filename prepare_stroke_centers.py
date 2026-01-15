#!/usr/bin/env python3
"""
Script to prepare stroke center data.
This includes sample data and instructions for obtaining real data from Joint Commission.
"""

import json
import os

def create_sample_stroke_centers():
    """
    Create sample stroke center data as a template.
    Users should replace this with actual data from Joint Commission or DNV.
    """

    print("Creating sample stroke center data...")
    print("\n" + "="*70)
    print("IMPORTANT: This creates SAMPLE data for testing purposes.")
    print("="*70)
    print("\nTo get real comprehensive stroke center data:")
    print("\n1. Joint Commission (Recommended):")
    print("   - Visit: https://www.qualitycheck.org/data-download/")
    print("   - Look for 'Certification Data Download'")
    print("   - Download stroke certification files")
    print("   - File may be Excel or CSV format")
    print("\n2. DNV Healthcare:")
    print("   - Visit: https://www.dnv.us/supplychain/healthcare/stroke-certs/")
    print("   - Search their hospital database")
    print("   - May need to compile data manually or contact DNV")
    print("\n3. State Health Departments:")
    print("   - Many states publish stroke center lists")
    print("   - Example: https://www.health.ny.gov/diseases/cardiovascular/stroke/")
    print("\n" + "="*70)

    # Sample data with major comprehensive stroke centers across the US
    sample_centers = [
        {
            "name": "Mayo Clinic Hospital",
            "address": "200 First Street SW",
            "city": "Rochester",
            "state": "MN",
            "zipcode": "55905",
            "latitude": 44.0225,
            "longitude": -92.4668,
            "phone": "(507) 284-2511",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "Johns Hopkins Hospital",
            "address": "1800 Orleans Street",
            "city": "Baltimore",
            "state": "MD",
            "zipcode": "21287",
            "latitude": 39.2971,
            "longitude": -76.5929,
            "phone": "(410) 955-5000",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "Massachusetts General Hospital",
            "address": "55 Fruit Street",
            "city": "Boston",
            "state": "MA",
            "zipcode": "02114",
            "latitude": 42.3631,
            "longitude": -71.0686,
            "phone": "(617) 726-2000",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "Cleveland Clinic",
            "address": "9500 Euclid Avenue",
            "city": "Cleveland",
            "state": "OH",
            "zipcode": "44195",
            "latitude": 41.5034,
            "longitude": -81.6219,
            "phone": "(216) 444-2200",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "UCLA Medical Center",
            "address": "757 Westwood Plaza",
            "city": "Los Angeles",
            "state": "CA",
            "zipcode": "90095",
            "latitude": 34.0653,
            "longitude": -118.4454,
            "phone": "(310) 825-9111",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "New York-Presbyterian Hospital",
            "address": "525 East 68th Street",
            "city": "New York",
            "state": "NY",
            "zipcode": "10065",
            "latitude": 40.7650,
            "longitude": -73.9540,
            "phone": "(212) 746-5454",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "Northwestern Memorial Hospital",
            "address": "251 East Huron Street",
            "city": "Chicago",
            "state": "IL",
            "zipcode": "60611",
            "latitude": 41.8949,
            "longitude": -87.6217,
            "phone": "(312) 926-2000",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "Houston Methodist Hospital",
            "address": "6565 Fannin Street",
            "city": "Houston",
            "state": "TX",
            "zipcode": "77030",
            "latitude": 29.7091,
            "longitude": -95.3980,
            "phone": "(713) 790-3311",
            "certification_org": "DNV",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "UCSF Medical Center",
            "address": "505 Parnassus Avenue",
            "city": "San Francisco",
            "state": "CA",
            "zipcode": "94143",
            "latitude": 37.7627,
            "longitude": -122.4581,
            "phone": "(415) 476-1000",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        },
        {
            "name": "Stanford Health Care",
            "address": "300 Pasteur Drive",
            "city": "Stanford",
            "state": "CA",
            "zipcode": "94305",
            "latitude": 37.4419,
            "longitude": -122.1740,
            "phone": "(650) 723-4000",
            "certification_org": "Joint Commission",
            "certification_type": "Comprehensive Stroke Center"
        }
    ]

    # Create data directory
    os.makedirs('data', exist_ok=True)

    # Save sample data
    output_file = 'data/stroke_centers.json'
    with open(output_file, 'w') as f:
        json.dump(sample_centers, f, indent=2)

    print(f"\nSample data created: {output_file}")
    print(f"Contains {len(sample_centers)} sample comprehensive stroke centers")
    print("\nReplace this file with actual data from Joint Commission or DNV!")

    return True

def convert_csv_to_json(csv_file):
    """
    Helper function to convert downloaded CSV data to JSON format.
    Call this function if you download CSV data from Joint Commission.
    """
    import csv

    print(f"Converting {csv_file} to JSON...")

    centers = []

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Adjust these field names based on actual CSV structure
                center = {
                    "name": row.get('Organization Name', ''),
                    "address": row.get('Address', ''),
                    "city": row.get('City', ''),
                    "state": row.get('State', ''),
                    "zipcode": row.get('Zip', ''),
                    "latitude": float(row.get('Latitude', 0)) if row.get('Latitude') else 0,
                    "longitude": float(row.get('Longitude', 0)) if row.get('Longitude') else 0,
                    "phone": row.get('Phone', ''),
                    "certification_org": row.get('Certification Organization', 'Joint Commission'),
                    "certification_type": row.get('Certification Type', 'Comprehensive Stroke Center')
                }

                centers.append(center)

        # Save to JSON
        output_file = 'data/stroke_centers.json'
        with open(output_file, 'w') as f:
            json.dump(centers, f, indent=2)

        print(f"Converted {len(centers)} centers to {output_file}")
        return True

    except Exception as e:
        print(f"Error converting CSV: {e}")
        return False

if __name__ == "__main__":
    create_sample_stroke_centers()
