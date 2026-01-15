#!/usr/bin/env python3
"""
Extract comprehensive stroke centers from multiple state PDF sources
"""

import json
import time
import re
import requests
from urllib.parse import quote
import PyPDF2
from io import BytesIO

# State PDF sources with comprehensive stroke centers
STATE_SOURCES = {
    'NC': 'https://info.ncdhhs.gov/dhsr/ahc/pdf/strokecenters.pdf',
    'PA': 'https://www.pa.gov/content/dam/copapwp-pagov/en/health/documents/topics/documents/ems/Designated%20Stroke%20Centers.pdf',
    'GA': 'https://dph.georgia.gov/document/document/georgia-dph-stroke-centers-2-11-2025pdf/download',
    'FL': 'https://ahca.myflorida.com/content/download/24552/file/Comprehensive_Stroke_Centers.pdf',
}

def download_pdf(url):
    """Download PDF and return bytes"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return BytesIO(response.content)
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def extract_text_from_pdf(pdf_bytes):
    """Extract all text from PDF"""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_bytes)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
    return text

def parse_comprehensive_centers(text, state):
    """Parse comprehensive stroke centers from extracted text"""
    centers = []

    # Look for comprehensive stroke center indicators
    lines = text.split('\n')

    for i, line in enumerate(lines):
        line_lower = line.lower()

        # Check if this line mentions "comprehensive" stroke center
        if 'comprehensive' in line_lower and ('stroke' in line_lower or i > 0):
            # Try to extract hospital name from this line or nearby lines
            hospital_name = None
            city = None

            # Clean the line
            hospital_name = re.sub(r'\s+', ' ', line).strip()

            # Try to find city in the same line or next few lines
            for j in range(i, min(i+3, len(lines))):
                city_match = re.search(r',\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)', lines[j])
                if city_match:
                    city = city_match.group(1)
                    break

            if hospital_name and len(hospital_name) > 5:
                centers.append({
                    'name': hospital_name,
                    'city': city or 'Unknown',
                    'state': state,
                    'raw_line': line
                })

    return centers

def geocode_address(name, city, state, zipcode=''):
    """Geocode using OpenStreetMap Nominatim"""
    query = f"{name}, {city}, {state}, USA"
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': query,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'StrokeCenter FinderApp/1.0'
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
        print(f"Geocoding failed for {name}: {e}")

    return None

def main():
    print("Extracting comprehensive stroke centers from state PDFs...")

    all_centers = []

    for state, url in STATE_SOURCES.items():
        print(f"\nProcessing {state}...")

        # Download PDF
        pdf_bytes = download_pdf(url)
        if not pdf_bytes:
            print(f"  Failed to download {state} PDF")
            continue

        # Extract text
        text = extract_text_from_pdf(pdf_bytes)
        if not text:
            print(f"  Failed to extract text from {state} PDF")
            continue

        print(f"  Extracted {len(text)} characters of text")

        # Parse comprehensive centers
        centers = parse_comprehensive_centers(text, state)
        print(f"  Found {len(centers)} potential comprehensive stroke centers")

        all_centers.extend(centers)

    print(f"\nTotal centers found: {len(all_centers)}")

    # Save raw extracted data
    with open('data/extracted_centers_raw.json', 'w') as f:
        json.dump(all_centers, f, indent=2)

    print(f"Saved raw data to data/extracted_centers_raw.json")
    print("\nManual review needed - the parsing may need refinement based on PDF formats")

if __name__ == '__main__':
    main()
