#!/usr/bin/env python3
"""
Script to download and process US zipcode data with coordinates.
This will create a JSON file with zipcode -> lat/lon mappings.
"""

import json
import csv
import urllib.request
import os

def download_zipcode_data():
    """Download zipcode data from a reliable free source."""

    print("Downloading US zipcode data...")

    # Using a GitHub Gist with US zipcode data (free and reliable)
    url = "https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data"

    try:
        # Download the file
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')

        # Parse CSV data
        zipcode_dict = {}
        csv_reader = csv.DictReader(data.splitlines())

        for row in csv_reader:
            zipcode = row.get('ZIP', '').strip()
            lat = row.get('LAT', '').strip()
            lon = row.get('LNG', '').strip()
            city = row.get('CITY', '').strip()
            state = row.get('STATE', '').strip()

            if zipcode and lat and lon:
                try:
                    zipcode_dict[zipcode] = {
                        'lat': float(lat),
                        'lon': float(lon),
                        'city': city,
                        'state': state
                    }
                except ValueError:
                    continue

        print(f"Processed {len(zipcode_dict)} zipcodes")

        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)

        # Save to JSON file
        output_file = 'data/zipcodes.json'
        with open(output_file, 'w') as f:
            json.dump(zipcode_dict, f, indent=2)

        print(f"Zipcode data saved to {output_file}")
        return True

    except Exception as e:
        print(f"Error downloading zipcode data: {e}")
        print("\nAlternative: You can manually download zipcode data from:")
        print("- https://simplemaps.com/data/us-zips (Free download)")
        print("- https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude")
        return False

if __name__ == "__main__":
    download_zipcode_data()
