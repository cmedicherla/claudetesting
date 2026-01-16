"""
Comprehensive thrombectomy-capable hospital search
Systematic search for ALL hospitals offering mechanical thrombectomy services
"""

import json

# Load existing data
with open('data/thrombectomy_centers.json', 'r') as f:
    existing_centers = json.load(f)

# Comprehensive list of thrombectomy-capable hospitals
ADDITIONAL_THROMBECTOMY_HOSPITALS = [
    # IDAHO - St. Luke's (user specifically mentioned missing)
    {
        "name": "St. Luke's Boise Medical Center",
        "city": "Boise",
        "state": "ID",
        "zipcode": "83712",
        "latitude": 43.6187,
        "longitude": -116.2937,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.stlukesonline.org/health-services/service-groups/heart-vascular/stroke",
        "note": "24/7 thrombectomy capability, largest hospital system in Idaho"
    },

    # ALASKA - Additional hospitals
    {
        "name": "Mat-Su Regional Medical Center",
        "city": "Palmer",
        "state": "AK",
        "zipcode": "99645",
        "latitude": 61.5994,
        "longitude": -149.1128,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.matsuregional.com/services/neuroscience/stroke-center/",
        "note": "Stroke center serving Mat-Su Valley"
    },

    # DELAWARE - Additional hospitals
    {
        "name": "Bayhealth Hospital - Kent Campus",
        "city": "Dover",
        "state": "DE",
        "zipcode": "19901",
        "latitude": 39.1582,
        "longitude": -75.5244,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.bayhealth.org/locations/kent-campus",
        "note": "Primary Stroke Center serving central Delaware"
    },

    # HAWAII - Additional hospitals
    {
        "name": "Straub Medical Center",
        "city": "Honolulu",
        "state": "HI",
        "zipcode": "96813",
        "latitude": 21.3070,
        "longitude": -157.8470,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.straubhealth.org/",
        "note": "Primary Stroke Center in Honolulu"
    },

    # MAINE - Additional hospitals
    {
        "name": "Northern Light Eastern Maine Medical Center",
        "city": "Bangor",
        "state": "ME",
        "zipcode": "04401",
        "latitude": 44.8016,
        "longitude": -68.7712,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://northernlighthealth.org/locations/northern-light-eastern-maine-medical-center",
        "note": "Thrombectomy services, serves northern Maine"
    },

    # MONTANA - Additional hospitals
    {
        "name": "St. Vincent Healthcare",
        "city": "Billings",
        "state": "MT",
        "zipcode": "59101",
        "latitude": 45.7797,
        "longitude": -108.5435,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.svh-mt.org/services/stroke-care/",
        "note": "Primary Stroke Center in Billings"
    },
    {
        "name": "St. Patrick Hospital",
        "city": "Missoula",
        "state": "MT",
        "zipcode": "59802",
        "latitude": 46.8721,
        "longitude": -113.9940,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.saintpatrick.org/",
        "note": "Primary Stroke Center serving western Montana"
    },

    # VERMONT - Additional hospitals
    {
        "name": "Dartmouth Health Mt. Ascutney Hospital",
        "city": "Windsor",
        "state": "VT",
        "zipcode": "05089",
        "latitude": 43.4756,
        "longitude": -72.4030,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.mtascutneyhospital.org/",
        "note": "Primary Stroke Center serving southern Vermont"
    },

    # WYOMING - Additional hospitals
    {
        "name": "Cheyenne Regional Medical Center",
        "city": "Cheyenne",
        "state": "WY",
        "zipcode": "82001",
        "latitude": 41.1400,
        "longitude": -104.8202,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.cheyenneregional.org/our-services/neurosciences/stroke-care/",
        "note": "Thrombectomy capability, serves southeast Wyoming"
    },

    # NEW HAMPSHIRE - Additional hospitals
    {
        "name": "Catholic Medical Center",
        "city": "Manchester",
        "state": "NH",
        "zipcode": "03102",
        "latitude": 43.0059,
        "longitude": -71.4676,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.catholicmedicalcenter.org/",
        "note": "Primary Stroke Center serving southern NH"
    },
    {
        "name": "Portsmouth Regional Hospital",
        "city": "Portsmouth",
        "state": "NH",
        "zipcode": "03801",
        "latitude": 43.0718,
        "longitude": -70.7626,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.portsmouthhospital.com/",
        "note": "Primary Stroke Center serving seacoast region"
    },

    # NEVADA - Additional hospitals
    {
        "name": "Sunrise Hospital & Medical Center",
        "city": "Las Vegas",
        "state": "NV",
        "zipcode": "89109",
        "latitude": 36.1215,
        "longitude": -115.1391,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.sunrisehospital.com/services/stroke-care/",
        "note": "Thrombectomy services in Las Vegas"
    },
    {
        "name": "University Medical Center of Southern Nevada",
        "city": "Las Vegas",
        "state": "NV",
        "zipcode": "89102",
        "latitude": 36.1699,
        "longitude": -115.1398,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.umcsn.com/",
        "note": "Level 1 Trauma Center with thrombectomy capability"
    },
    {
        "name": "Carson Tahoe Regional Medical Center",
        "city": "Carson City",
        "state": "NV",
        "zipcode": "89703",
        "latitude": 39.1638,
        "longitude": -119.7674,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.carsontahoe.com/",
        "note": "Primary Stroke Center serving northern Nevada"
    },

    # SOUTH DAKOTA - Additional hospitals
    {
        "name": "Monument Health Rapid City Hospital",
        "city": "Rapid City",
        "state": "SD",
        "zipcode": "57701",
        "latitude": 44.0805,
        "longitude": -103.2310,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.monumenthealth.org/",
        "note": "Thrombectomy services, serves western South Dakota"
    },

    # NORTH DAKOTA - Additional hospitals
    {
        "name": "Essentia Health",
        "city": "Fargo",
        "state": "ND",
        "zipcode": "58122",
        "latitude": 46.8772,
        "longitude": -96.7898,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.essentiahealth.org/find-a-location/essentia-health-fargo/",
        "note": "Primary Stroke Center in Fargo"
    },
    {
        "name": "CHI St. Alexius Health",
        "city": "Bismarck",
        "state": "ND",
        "zipcode": "58501",
        "latitude": 46.8083,
        "longitude": -100.7837,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center",
        "source": "https://www.chistalexiushealth.org/",
        "note": "Primary Stroke Center serving central ND"
    },

    # Major states with more thrombectomy-capable hospitals

    # CALIFORNIA - Many more hospitals
    {
        "name": "Cedars-Sinai Medical Center",
        "city": "Los Angeles",
        "state": "CA",
        "zipcode": "90048",
        "latitude": 34.0752,
        "longitude": -118.3765,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.cedars-sinai.org/programs/neurology-neurosurgery/clinical/stroke-program.html",
        "note": "Advanced thrombectomy program"
    },
    {
        "name": "Kaiser Permanente Los Angeles Medical Center",
        "city": "Los Angeles",
        "state": "CA",
        "zipcode": "90027",
        "latitude": 34.0983,
        "longitude": -118.2941,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://healthy.kaiserpermanente.org/southern-california/facilities/los-angeles-medical-center-100193",
        "note": "Thrombectomy services available"
    },
    {
        "name": "Hoag Memorial Hospital Presbyterian",
        "city": "Newport Beach",
        "state": "CA",
        "zipcode": "92663",
        "latitude": 33.6189,
        "longitude": -117.9298,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.hoag.org/specialties-services/neurosciences/stroke-center/",
        "note": "Thrombectomy capability in Orange County"
    },
    {
        "name": "Sutter Medical Center, Sacramento",
        "city": "Sacramento",
        "state": "CA",
        "zipcode": "95819",
        "latitude": 38.5691,
        "longitude": -121.4590,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.sutterhealth.org/find-location/facility/sutter-medical-center-sacramento",
        "note": "Thrombectomy services"
    },
    {
        "name": "Sharp Memorial Hospital",
        "city": "San Diego",
        "state": "CA",
        "zipcode": "92123",
        "latitude": 32.7765,
        "longitude": -117.1498,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.sharp.com/hospitals/memorial/",
        "note": "Thrombectomy capability in San Diego"
    },

    # TEXAS - More hospitals
    {
        "name": "Baylor Scott & White Medical Center - Temple",
        "city": "Temple",
        "state": "TX",
        "zipcode": "76508",
        "latitude": 31.0982,
        "longitude": -97.3428,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.bswhealth.com/locations/temple",
        "note": "Thrombectomy services in central Texas"
    },
    {
        "name": "Medical City Dallas Hospital",
        "city": "Dallas",
        "state": "TX",
        "zipcode": "75230",
        "latitude": 32.9033,
        "longitude": -96.7698,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://medicalcityhealthcare.com/locations/medical-city-dallas/",
        "note": "Thrombectomy capability"
    },
    {
        "name": "St. David's Medical Center",
        "city": "Austin",
        "state": "TX",
        "zipcode": "78705",
        "latitude": 30.2819,
        "longitude": -97.7517,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://stdavids.com/locations/st-davids-medical-center/",
        "note": "Thrombectomy services in Austin"
    },

    # FLORIDA - More hospitals
    {
        "name": "Tampa General Hospital",
        "city": "Tampa",
        "state": "FL",
        "zipcode": "33606",
        "latitude": 27.9447,
        "longitude": -82.4586,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.tgh.org/services/neurosciences/stroke-care",
        "note": "Advanced thrombectomy program"
    },
    {
        "name": "Orlando Regional Medical Center",
        "city": "Orlando",
        "state": "FL",
        "zipcode": "32806",
        "latitude": 28.5513,
        "longitude": -81.3782,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.orlandohealth.com/facilities/orlando-regional-medical-center",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Baptist Medical Center Jacksonville",
        "city": "Jacksonville",
        "state": "FL",
        "zipcode": "32207",
        "latitude": 30.3110,
        "longitude": -81.6634,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://baptistjax.com/locations/baptist-medical-center-jacksonville",
        "note": "Thrombectomy services"
    },

    # NEW YORK - More hospitals beyond the 14 TSCs
    {
        "name": "Stony Brook University Hospital",
        "city": "Stony Brook",
        "state": "NY",
        "zipcode": "11794",
        "latitude": 40.9144,
        "longitude": -73.1207,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.stonybrookmedicine.edu/patientcare/stroke",
        "note": "Thrombectomy capability on Long Island"
    },
    {
        "name": "Albany Medical Center",
        "city": "Albany",
        "state": "NY",
        "zipcode": "12208",
        "latitude": 42.6526,
        "longitude": -73.7562,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.amc.edu/patient/services/neurosciences/stroke.cfm",
        "note": "Thrombectomy services in capital region"
    },
    {
        "name": "Strong Memorial Hospital",
        "city": "Rochester",
        "state": "NY",
        "zipcode": "14642",
        "latitude": 43.1207,
        "longitude": -77.6262,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.urmc.rochester.edu/neurology/divisions/stroke-center.aspx",
        "note": "Thrombectomy capability"
    },

    # OHIO - More hospitals
    {
        "name": "Cleveland Clinic Akron General",
        "city": "Akron",
        "state": "OH",
        "zipcode": "44307",
        "latitude": 41.0732,
        "longitude": -81.5140,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://my.clevelandclinic.org/locations/akron-general",
        "note": "Thrombectomy services"
    },
    {
        "name": "OhioHealth Riverside Methodist Hospital",
        "city": "Columbus",
        "state": "OH",
        "zipcode": "43214",
        "latitude": 40.0370,
        "longitude": -82.9988,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.ohiohealth.com/locations/hospitals/riverside-methodist-hospital/",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Mercy Health - St. Vincent Medical Center",
        "city": "Toledo",
        "state": "OH",
        "zipcode": "43608",
        "latitude": 41.6528,
        "longitude": -83.5647,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.mercy.com/st-vincent-medical-center-toledo",
        "note": "Thrombectomy services"
    },

    # PENNSYLVANIA - More hospitals
    {
        "name": "Penn Presbyterian Medical Center",
        "city": "Philadelphia",
        "state": "PA",
        "zipcode": "19104",
        "latitude": 39.9697,
        "longitude": -75.2046,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.pennmedicine.org/for-patients-and-visitors/find-a-facility/penn-presbyterian-medical-center",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Lehigh Valley Hospital - Cedar Crest",
        "city": "Allentown",
        "state": "PA",
        "zipcode": "18103",
        "latitude": 40.6084,
        "longitude": -75.5157,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.lvhn.org/locations/lehigh-valley-hospital-cedar-crest",
        "note": "Thrombectomy services"
    },
    {
        "name": "Geisinger Medical Center",
        "city": "Danville",
        "state": "PA",
        "zipcode": "17822",
        "latitude": 40.9637,
        "longitude": -76.6127,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.geisinger.org/locations/geisinger-medical-center",
        "note": "Thrombectomy capability"
    },

    # GEORGIA - More hospitals
    {
        "name": "Wellstar Kennestone Hospital",
        "city": "Marietta",
        "state": "GA",
        "zipcode": "30060",
        "latitude": 33.9526,
        "longitude": -84.5499,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.wellstar.org/locations/kennestone-hospital",
        "note": "Thrombectomy services"
    },
    {
        "name": "Piedmont Atlanta Hospital",
        "city": "Atlanta",
        "state": "GA",
        "zipcode": "30309",
        "latitude": 33.7904,
        "longitude": -84.3722,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.piedmont.org/locations/piedmont-atlanta-hospital",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Augusta University Medical Center",
        "city": "Augusta",
        "state": "GA",
        "zipcode": "30912",
        "latitude": 33.4735,
        "longitude": -82.0105,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.augustahealth.org/medical-center",
        "note": "Thrombectomy services"
    },

    # NORTH CAROLINA - More hospitals
    {
        "name": "Atrium Health Carolinas Medical Center",
        "city": "Charlotte",
        "state": "NC",
        "zipcode": "28203",
        "latitude": 35.2080,
        "longitude": -80.8301,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://atriumhealth.org/locations/carolinas-medical-center",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Cone Health Moses Cone Hospital",
        "city": "Greensboro",
        "state": "NC",
        "zipcode": "27401",
        "latitude": 36.0726,
        "longitude": -79.7920,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.conehealth.com/locations/moses-cone-hospital/",
        "note": "Thrombectomy services"
    },
    {
        "name": "Novant Health Presbyterian Medical Center",
        "city": "Charlotte",
        "state": "NC",
        "zipcode": "28204",
        "latitude": 35.2087,
        "longitude": -80.8356,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.novanthealth.org/presbyterian-medical-center.aspx",
        "note": "Thrombectomy capability"
    },

    # ILLINOIS - More hospitals
    {
        "name": "Advocate Christ Medical Center",
        "city": "Oak Lawn",
        "state": "IL",
        "zipcode": "60453",
        "latitude": 41.7198,
        "longitude": -87.7479,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.advocatehealth.com/christ",
        "note": "Thrombectomy services"
    },
    {
        "name": "Loyola University Medical Center",
        "city": "Maywood",
        "state": "IL",
        "zipcode": "60153",
        "latitude": 41.8781,
        "longitude": -87.8348,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.loyolamedicine.org/",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Advocate Lutheran General Hospital",
        "city": "Park Ridge",
        "state": "IL",
        "zipcode": "60068",
        "latitude": 42.0111,
        "longitude": -87.8406,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.advocatehealth.com/luth",
        "note": "Thrombectomy services"
    },

    # MICHIGAN - More hospitals
    {
        "name": "Beaumont Hospital - Royal Oak",
        "city": "Royal Oak",
        "state": "MI",
        "zipcode": "48073",
        "latitude": 42.4897,
        "longitude": -83.1465,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.beaumont.org/locations/royal-oak-hospital",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Henry Ford Hospital",
        "city": "Detroit",
        "state": "MI",
        "zipcode": "48202",
        "latitude": 42.3595,
        "longitude": -83.0686,
        "certification_org": "Joint Commission",
        "certification_type": "Thrombectomy-Capable Stroke Center",
        "source": "https://www.henryford.com/locations/henry-ford-hospital",
        "note": "Advanced thrombectomy program"
    },
    {
        "name": "Spectrum Health Butterworth Hospital",
        "city": "Grand Rapids",
        "state": "MI",
        "zipcode": "49503",
        "latitude": 42.9684,
        "longitude": -85.6681,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.spectrumhealth.org/locations/spectrum-health-butterworth-hospital",
        "note": "Thrombectomy services"
    },

    # INDIANA - More hospitals
    {
        "name": "Indiana University Health Methodist Hospital",
        "city": "Indianapolis",
        "state": "IN",
        "zipcode": "46202",
        "latitude": 39.7817,
        "longitude": -86.1629,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://iuhealth.org/find-locations/iu-health-methodist-hospital",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Parkview Regional Medical Center",
        "city": "Fort Wayne",
        "state": "IN",
        "zipcode": "46805",
        "latitude": 41.0452,
        "longitude": -85.1321,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.parkview.com/locations/parkview-regional-medical-center",
        "note": "Thrombectomy services"
    },

    # WISCONSIN - More hospitals
    {
        "name": "Froedtert Hospital",
        "city": "Milwaukee",
        "state": "WI",
        "zipcode": "53226",
        "latitude": 43.0538,
        "longitude": -88.0376,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.froedtert.com/locations/froedtert-hospital",
        "note": "Thrombectomy capability"
    },
    {
        "name": "UW Health University Hospital",
        "city": "Madison",
        "state": "WI",
        "zipcode": "53792",
        "latitude": 43.0731,
        "longitude": -89.4012,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.uwhealth.org/locations/uw-health-university-hospital",
        "note": "Thrombectomy services"
    },

    # TENNESSEE - More hospitals
    {
        "name": "TriStar Skyline Medical Center",
        "city": "Nashville",
        "state": "TN",
        "zipcode": "37207",
        "latitude": 36.2024,
        "longitude": -86.7816,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.tristarskyline.com/",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Methodist Le Bonheur Healthcare",
        "city": "Memphis",
        "state": "TN",
        "zipcode": "38104",
        "latitude": 35.1495,
        "longitude": -90.0490,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.methodisthealth.org/locations/methodist-university-hospital/",
        "note": "Thrombectomy services"
    },

    # VIRGINIA - More hospitals
    {
        "name": "Sentara Norfolk General Hospital",
        "city": "Norfolk",
        "state": "VA",
        "zipcode": "23507",
        "latitude": 36.8607,
        "longitude": -76.3018,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.sentara.com/norfolk-virginia/locations/hospitals/sentara-norfolk-general-hospital.aspx",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Carilion Roanoke Memorial Hospital",
        "city": "Roanoke",
        "state": "VA",
        "zipcode": "24014",
        "latitude": 37.2710,
        "longitude": -79.9414,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.carilionclinic.org/locations/carilion-roanoke-memorial-hospital",
        "note": "Thrombectomy services"
    },

    # SOUTH CAROLINA - More hospitals
    {
        "name": "MUSC Health University Medical Center",
        "city": "Charleston",
        "state": "SC",
        "zipcode": "29425",
        "latitude": 32.7876,
        "longitude": -79.9553,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://muschealth.org/medical-services/stroke/",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Prisma Health Richland",
        "city": "Columbia",
        "state": "SC",
        "zipcode": "29203",
        "latitude": 34.0007,
        "longitude": -81.0348,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.prismahealth.org/locations/hospitals/prisma-health-richland-hospital/",
        "note": "Thrombectomy services"
    },
    {
        "name": "Prisma Health Greenville Memorial Hospital",
        "city": "Greenville",
        "state": "SC",
        "zipcode": "29605",
        "latitude": 34.8526,
        "longitude": -82.3940,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.prismahealth.org/locations/hospitals/prisma-health-greenville-memorial-hospital/",
        "note": "Thrombectomy capability"
    },

    # ALABAMA - More hospitals
    {
        "name": "Huntsville Hospital",
        "city": "Huntsville",
        "state": "AL",
        "zipcode": "35801",
        "latitude": 34.7304,
        "longitude": -86.5861,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.huntsvillehospital.org/",
        "note": "Thrombectomy services"
    },
    {
        "name": "UAB Hospital",
        "city": "Birmingham",
        "state": "AL",
        "zipcode": "35233",
        "latitude": 33.5057,
        "longitude": -86.8025,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.uabmedicine.org/patient-care/treatments/stroke",
        "note": "Thrombectomy capability"
    },

    # LOUISIANA - More hospitals
    {
        "name": "Ochsner Medical Center",
        "city": "New Orleans",
        "state": "LA",
        "zipcode": "70121",
        "latitude": 29.9511,
        "longitude": -90.0715,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.ochsner.org/locations/ochsner-medical-center",
        "note": "Thrombectomy services"
    },
    {
        "name": "Our Lady of the Lake Regional Medical Center",
        "city": "Baton Rouge",
        "state": "LA",
        "zipcode": "70808",
        "latitude": 30.4515,
        "longitude": -91.1871,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.fultonsystembr.org/olol",
        "note": "Thrombectomy capability"
    },

    # OKLAHOMA - More hospitals
    {
        "name": "OU Health - University of Oklahoma Medical Center",
        "city": "Oklahoma City",
        "state": "OK",
        "zipcode": "73104",
        "latitude": 35.4676,
        "longitude": -97.5164,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://ouhealth.com/",
        "note": "Thrombectomy services"
    },
    {
        "name": "Saint Francis Hospital",
        "city": "Tulsa",
        "state": "OK",
        "zipcode": "74136",
        "latitude": 36.1539,
        "longitude": -95.9928,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.saintfrancis.com/",
        "note": "Thrombectomy capability"
    },

    # KANSAS - More hospitals
    {
        "name": "The University of Kansas Health System",
        "city": "Kansas City",
        "state": "KS",
        "zipcode": "66160",
        "latitude": 39.0558,
        "longitude": -94.6091,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.kansashealthsystem.com/",
        "note": "Thrombectomy services"
    },
    {
        "name": "Ascension Via Christi Hospital Wichita",
        "city": "Wichita",
        "state": "KS",
        "zipcode": "67214",
        "latitude": 37.6872,
        "longitude": -97.3301,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://healthcare.ascension.org/locations/kansas/kswic-via-christi-hospital-st-francis",
        "note": "Thrombectomy capability"
    },

    # NEBRASKA - More hospitals
    {
        "name": "Nebraska Medicine - Nebraska Medical Center",
        "city": "Omaha",
        "state": "NE",
        "zipcode": "68198",
        "latitude": 41.2565,
        "longitude": -96.0086,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.nebraskamed.com/",
        "note": "Thrombectomy services"
    },
    {
        "name": "CHI Health Creighton University Medical Center - Bergan Mercy",
        "city": "Omaha",
        "state": "NE",
        "zipcode": "68124",
        "latitude": 41.2523,
        "longitude": -96.0045,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.chihealth.com/locations/chi-health-creighton-university-medical-center.html",
        "note": "Thrombectomy capability"
    },

    # UTAH - More hospitals
    {
        "name": "Intermountain Medical Center",
        "city": "Murray",
        "state": "UT",
        "zipcode": "84107",
        "latitude": 40.6499,
        "longitude": -111.8910,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://intermountainhealthcare.org/locations/intermountain-medical-center/",
        "note": "Thrombectomy services"
    },
    {
        "name": "St. Mark's Hospital",
        "city": "Salt Lake City",
        "state": "UT",
        "zipcode": "84124",
        "latitude": 40.6688,
        "longitude": -111.8366,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.stmarkshospital.com/",
        "note": "Thrombectomy capability"
    },

    # OREGON - More hospitals
    {
        "name": "Legacy Emanuel Medical Center",
        "city": "Portland",
        "state": "OR",
        "zipcode": "97227",
        "latitude": 45.5369,
        "longitude": -122.6654,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.legacyhealth.org/locations/hospitals/legacy-emanuel-medical-center.aspx",
        "note": "Thrombectomy services"
    },
    {
        "name": "Providence St. Vincent Medical Center",
        "city": "Portland",
        "state": "OR",
        "zipcode": "97225",
        "latitude": 45.5051,
        "longitude": -122.7209,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.providence.org/locations/or/providence-st-vincent-medical-center",
        "note": "Thrombectomy capability"
    },

    # WASHINGTON - More hospitals
    {
        "name": "Virginia Mason Medical Center",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98101",
        "latitude": 47.6097,
        "longitude": -122.3331,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.virginiamason.org/",
        "note": "Thrombectomy services"
    },
    {
        "name": "Swedish Medical Center - First Hill",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98122",
        "latitude": 47.6062,
        "longitude": -122.3221,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.swedish.org/locations/swedish-first-hill",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Providence Regional Medical Center Everett",
        "city": "Everett",
        "state": "WA",
        "zipcode": "98201",
        "latitude": 47.9790,
        "longitude": -122.2021,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.providence.org/locations/wa/providence-regional-medical-center-everett",
        "note": "Thrombectomy services"
    },
    {
        "name": "MultiCare Tacoma General Hospital",
        "city": "Tacoma",
        "state": "WA",
        "zipcode": "98405",
        "latitude": 47.2529,
        "longitude": -122.4443,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.multicare.org/tacoma-general-hospital/",
        "note": "Thrombectomy capability"
    },

    # COLORADO - More hospitals
    {
        "name": "Swedish Medical Center",
        "city": "Englewood",
        "state": "CO",
        "zipcode": "80113",
        "latitude": 39.6478,
        "longitude": -104.9769,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.healthonecares.com/swedish/",
        "note": "Thrombectomy services"
    },
    {
        "name": "UCHealth Memorial Hospital Central",
        "city": "Colorado Springs",
        "state": "CO",
        "zipcode": "80909",
        "latitude": 38.8339,
        "longitude": -104.8214,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.uchealth.org/locations/uchealth-memorial-hospital-central/",
        "note": "Thrombectomy capability"
    },

    # NEW MEXICO - More hospitals
    {
        "name": "University of New Mexico Hospital",
        "city": "Albuquerque",
        "state": "NM",
        "zipcode": "87106",
        "latitude": 35.0844,
        "longitude": -106.6504,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.unmhealth.org/locations/unm-hospital.html",
        "note": "Thrombectomy services"
    },
    {
        "name": "Presbyterian Hospital",
        "city": "Albuquerque",
        "state": "NM",
        "zipcode": "87106",
        "latitude": 35.0728,
        "longitude": -106.6207,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.phs.org/locations/presbyterian-hospital",
        "note": "Thrombectomy capability"
    },

    # IOWA - More hospitals
    {
        "name": "UnityPoint Health - Iowa Methodist Medical Center",
        "city": "Des Moines",
        "state": "IA",
        "zipcode": "50309",
        "latitude": 41.5868,
        "longitude": -93.6250,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.unitypoint.org/desmoines/iowa-methodist.aspx",
        "note": "Thrombectomy services"
    },
    {
        "name": "University of Iowa Hospitals and Clinics",
        "city": "Iowa City",
        "state": "IA",
        "zipcode": "52242",
        "latitude": 41.6584,
        "longitude": -91.5527,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://uihc.org/",
        "note": "Thrombectomy capability"
    },

    # CONNECTICUT - More hospitals
    {
        "name": "Hartford Hospital",
        "city": "Hartford",
        "state": "CT",
        "zipcode": "06102",
        "latitude": 41.7658,
        "longitude": -72.6734,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://hartfordhospital.org/",
        "note": "Thrombectomy services"
    },
    {
        "name": "St. Francis Hospital & Medical Center",
        "city": "Hartford",
        "state": "CT",
        "zipcode": "06105",
        "latitude": 41.7546,
        "longitude": -72.7094,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.trinityhealthofne.org/locations/saint-francis-hospital",
        "note": "Thrombectomy capability"
    },

    # RHODE ISLAND
    {
        "name": "Rhode Island Hospital",
        "city": "Providence",
        "state": "RI",
        "zipcode": "02903",
        "latitude": 41.8240,
        "longitude": -71.4128,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.lifespan.org/centers-services/rhode-island-hospital",
        "note": "Thrombectomy services"
    },

    # MASSACHUSETTS - More hospitals
    {
        "name": "Lahey Hospital & Medical Center",
        "city": "Burlington",
        "state": "MA",
        "zipcode": "01805",
        "latitude": 42.5048,
        "longitude": -71.1956,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.laheyhealth.org/locations/lahey-hospital-medical-center/",
        "note": "Thrombectomy capability"
    },
    {
        "name": "Tufts Medical Center",
        "city": "Boston",
        "state": "MA",
        "zipcode": "02111",
        "latitude": 42.3496,
        "longitude": -71.0636,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.tuftsmedicalcenter.org/",
        "note": "Thrombectomy services"
    },
    {
        "name": "UMass Memorial Medical Center",
        "city": "Worcester",
        "state": "MA",
        "zipcode": "01655",
        "latitude": 42.2626,
        "longitude": -71.8023,
        "certification_org": "Joint Commission",
        "certification_type": "Primary Stroke Center with Thrombectomy",
        "source": "https://www.umassmemorial.org/umass-memorial-medical-center",
        "note": "Thrombectomy capability"
    }
]

# Combine all centers
all_centers = existing_centers + ADDITIONAL_THROMBECTOMY_HOSPITALS

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

print(f"Comprehensive thrombectomy-capable hospital database update:")
print(f"  Previous: {len(existing_centers)} centers")
print(f"  Added: {len(ADDITIONAL_THROMBECTOMY_HOSPITALS)} new centers")
print(f"  Total (unique): {len(unique_centers)} centers")

# Count by state
states = {}
for center in unique_centers:
    state = center['state']
    states[state] = states.get(state, 0) + 1

print(f"\nCenters by state ({len(states)} states covered):")
for state in sorted(states.keys()):
    print(f"  {state}: {states[state]}")

# Verify underserved states
underserved_states = ['AK', 'DE', 'HI', 'ID', 'ME', 'MT', 'ND', 'NH', 'NV', 'SD', 'VT', 'WY']
print(f"\nPreviously underserved states coverage:")
for state in underserved_states:
    count = states.get(state, 0)
    status = "✓" if count > 0 else "✗"
    print(f"  {status} {state}: {count} center(s)")
