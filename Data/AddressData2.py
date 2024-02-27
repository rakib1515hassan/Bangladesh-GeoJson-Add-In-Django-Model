import os
import sys
import django
import json
from django.conf import settings


""" NOTE:- Run this command to load data on Model

    >> python -m Data.AddressData2

"""




# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "address.settings")

# Initialize Django
django.setup()

# Now you can import your models
from myapp.models import Division, District, Upazila, PostCode

# Get the absolute path to the 'Data' directory
data_directory = os.path.join(settings.BASE_DIR, 'Data')

division_data_directory = os.path.join(data_directory, 'division.json')
district_data_directory = os.path.join(data_directory, 'districts.json')
upazila_data_directory  = os.path.join(data_directory, 'upazilas.json')
postalcode_data_directory = os.path.join(data_directory, 'postcodes.json')

# Load Division Data
with open(division_data_directory, 'r', encoding='utf-8') as file:
    div_data = json.load(file)

for division_data in div_data['divisions']:
    division = Division(
        id      = int(division_data.get('id', 0)),  # Default to 0 if 'id' is missing
        name    = division_data.get('name', ''),
        bn_name = division_data.get('bn_name', ''),
        lat     = float(division_data.get('lat', 0.0)),  # Default to 0.0 if 'lat' is missing
        long    = float(division_data.get('long', 0.0))  # Default to 0.0 if 'long' is missing
    )
    division.save()

# Load Districts Data
with open(district_data_directory, 'r', encoding='utf-8') as file:
    dis_data = json.load(file)

for district_data in dis_data['districts']:
    division_id = int(district_data.get('division_id', 0))  # Default to 0 if 'division_id' is missing
    division = Division.objects.get(id=division_id)
    
    district = District(
        division = division,
        id       = int(district_data.get('id', 0)),  # Default to 0 if 'id' is missing

        name     = district_data.get('name', ''),
        bn_name  = district_data.get('bn_name', ''),
        lat      = float(district_data.get('lat', 0.0)),  # Default to 0.0 if 'lat' is missing
        long     = float(district_data.get('long', 0.0))  # Default to 0.0 if 'long' is missing
    )
    district.save()

# Load Upazilas Data
with open(upazila_data_directory, 'r', encoding='utf-8') as file:
    upa_data = json.load(file)

for upazila_data in upa_data['upazilas']:
    district_id = int(upazila_data.get('district_id', 0))  # Default to 0 if 'district_id' is missing
    district = District.objects.get(id=district_id)

    upazila = Upazila(
        district = district,
        id       = int(upazila_data.get('id', 0)),  # Default to 0 if 'id' is missing

        name     = upazila_data.get('name', ''),
        bn_name  = upazila_data.get('bn_name', ''),
        lat      = float(upazila_data.get('lat', 0.0)),  # Default to 0.0 if 'lat' is missing
        long     = float(upazila_data.get('long', 0.0))  # Default to 0.0 if 'long' is missing
    )
    upazila.save()




# Load Post Code Data
with open(postalcode_data_directory, 'r', encoding='utf-8') as file:
    post_data = json.load(file)

for postcode_data in post_data['postcodes']:
    division_id = int(postcode_data.get('division_id', 0))  # Default to 0 if 'division_id' is missing
    district_id = int(postcode_data.get('district_id', 0))  # Default to 0 if 'district_id' is missing

    
    try:
        division = Division.objects.get(id=division_id)
    except Division.DoesNotExist:
        print(f"Division with ID {division_id} does not exist.")
        continue  # Move to the next iteration of the loop
    
    try:
        if district_id:
            district = District.objects.get(id=district_id)
        else:
            print("-----------------------------")
            print("Post Office =", postcode_data.get('postOffice'))
            print("-----------------------------")
            district = None
    except District.DoesNotExist:
        print("-----------------------------")
        print("Post Office =", postcode_data.get('postOffice'))
        print(f"District with ID {district_id} does not exist.")
        print("-----------------------------")
        continue  # Move to the next iteration of the loop
    
    postcode = PostCode(
        division   = division,
        district   = district,
        upazila    = postcode_data.get('upazila', ''),
        postOffice = postcode_data.get('postOffice', ''),
        postCode   = float(postcode_data.get('postCode', 0.0))  # Default to 0.0 if 'postCode' is missing
    )
    postcode.save()


print("Data inserted successfully.")
