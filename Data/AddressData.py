import os
import sys
import django
import json
from django.conf import settings

""" NOTE:- Run this command to load data on Model

    >> python -m Data.AddressData

"""

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "address.settings")

# Initialize Django
django.setup()

# Now you can import your models
from myapp.models import Division, District, Upazila, PostCode


# Get the absolute path to the 'Data' directory
division_data_directory   = settings.BASE_DIR / 'Data' / 'division.json'

district_data_directory   = settings.BASE_DIR / 'Data' / 'districts.json'

upazila_data_directory    = settings.BASE_DIR / 'Data' / 'upazilas.json'

postalcode_data_directory = settings.BASE_DIR / 'Data' / 'postcodes.json'




## NOTE:- Load Division Data
with open(division_data_directory, 'r', encoding='utf-8') as file:
    div_data = json.load(file)

for division_data in div_data['divisions']:
    division = Division(
        id      = int(division_data['id']),
        name    = division_data['name'],
        bn_name = division_data['bn_name'],
        lat     = float(division_data['lat']),
        long    = float(division_data['long'])
    )
    division.save()



## NOTE:- Load Districts Data
with open(district_data_directory, 'r', encoding='utf-8') as file:
    dis_data = json.load(file)

for district_data in dis_data['districts']:
    division_id = int(district_data['division_id'])
    division = Division.objects.get(id=division_id)
    
    district = District(
        division = division,
        id       = int(district_data['id']),

        name     = district_data['name'],
        bn_name  = district_data['bn_name'],
        lat      = float(district_data['lat']),
        long     = float(district_data['long'])
    )
    district.save()




## NOTE:- Load Upazilas Data
with open(upazila_data_directory, 'r', encoding='utf-8') as file:
    upa_data = json.load(file)

for upazila_data in upa_data['upazilas']:
    district_id = int(upazila_data['district_id'])
    district = District.objects.get(id=district_id)

    # Check if 'lat' and 'long' keys are present in the dictionary
    # lat = float(upazila_data.get('lat', 0.0))  # Default to 0.0 if 'lat' is not present
    # long = float(upazila_data.get('long', 0.0))  # Default to 0.0 if 'long' is not present
    
    upazila = Upazila(
        district = district,
        id       = int(upazila_data['id']),

        name     = upazila_data['name'],
        bn_name  = upazila_data['bn_name'],
        # lat      = float(upazila_data['lat']),
        lat      = float(0.0),
        # long     = float(upazila_data['long'])
        long     = float(0.0)
    )
    upazila.save()


## NOTE:- Load Post Code Data
with open(postalcode_data_directory, 'r', encoding='utf-8') as file:
    post_data = json.load(file)

for postcode_data in post_data['postcodes']:
    division_id = int(postcode_data['division_id'])
    district_id = int(postcode_data['district_id'])
    
    division = Division.objects.get(id=division_id)
    district = District.objects.get(id=district_id)
    
    postcode = PostCode(
        division   = division,
        district   = district,

        upazila    = postcode_data['upazila'],
        postOffice = postcode_data['postOffice'],
        postCode   = float(postcode_data['postCode'])
    )
    postcode.save()



print("Data inserted successfully.")
