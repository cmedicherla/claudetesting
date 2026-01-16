# Stroke Center Data Sources

This document outlines how to obtain complete data for TSC and PSC centers to replace the sample datasets.

## Current Status

- **CSC Data**: ✅ Complete (297 comprehensive stroke centers)
- **TSC Data**: ⚠️ Sample only (3 centers) - needs full dataset
- **PSC Data**: ⚠️ Sample only (3 centers) - needs full dataset

## Where to Find Data

### Option 1: Joint Commission Quality Check (Recommended)
- **URL**: https://www.jointcommission.org/en-us/about-us/facts-about-the-joint-commission/quality-check-and-quality-reports/
- **Alternative**: qualitycheck.org
- **Process**:
  1. Search by state or facility name
  2. Filter by certification type (TSC or PSC)
  3. Export results (may require multiple searches by state)
  4. Compile into JSON format matching our schema

### Option 2: State Health Departments
Many states publish their own stroke center lists:
- **North Carolina**: https://info.ncdhhs.gov/dhsr/ahc/pdf/strokecenters.pdf
- **Indiana**: https://www.in.gov/health/trauma-system/indiana-stroke-centers/
- **Connecticut**: https://portal.ct.gov/dph/emergency-medical-services/ems/certified-stroke-centers

Compile from all states and deduplicate.

### Option 3: Research Databases
- **PMC Inventory Study**: https://pmc.ncbi.nlm.nih.gov/articles/PMC8886184/
  - Contains supplemental data (Table S2) with state-specific counts
  - Contact: emnet@partners.org for research access
  - 2018 data: 1,459 PSCs, 12 TSCs nationally

### Option 4: Wikipedia
- **List of stroke centers**: https://en.wikipedia.org/wiki/List_of_stroke_centers_in_the_United_States
- Note: May not be complete or current

## Required Data Format

Each center needs:
```json
{
  "name": "Hospital Name",
  "city": "City",
  "state": "XX",
  "zipcode": "12345",
  "latitude": 00.0000,
  "longitude": -00.0000,
  "certification_org": "Joint Commission|DNV|ACHC",
  "certification_type": "Primary Stroke Center|Thrombectomy-Capable Stroke Center"
}
```

## Geocoding

If you have addresses but not lat/long:
- Use Google Maps Geocoding API
- Use OpenStreetMap Nominatim (free)
- Use batch geocoding services

## Estimated Numbers (2018 Data)

- **CSC**: ~297 (we have complete data)
- **TSC**: ~12-20 (growing rapidly since 2018)
- **PSC**: ~1,459

## Next Steps

1. Choose one or more data sources above
2. Download/scrape the data
3. Convert to JSON format
4. Add geocoding if needed
5. Replace `data/tsc_sample.json` and `data/psc_sample.json`
6. Update disclaimer in `desert.html` to remove "sample data" note

## Automation Suggestion

Create a Python script to:
1. Query Joint Commission Quality Check API (if available)
2. Or scrape state health department pages
3. Geocode addresses using Nominatim
4. Output to JSON files

Contact the maintainer if you need help with data compilation.
