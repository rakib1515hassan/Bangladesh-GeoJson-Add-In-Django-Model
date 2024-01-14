import os
import sys
import django
import json

# Set the Django settings module for the script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "address.settings")  # Assuming your project is named 'address'

# Ensure Django is correctly configured
django.setup()

# Now you can import your models
from myapp.models import Division

# Get the absolute path to the 'Data' directory
data_directory = os.path.abspath(os.path.dirname(__file__))

# Construct the absolute path to the 'division.json' file
json_file_path = os.path.join(data_directory, 'division.json')

with open(json_file_path, 'r') as file:
    data = json.load(file)

for division_data in data['divisions']:
    division = Division(
        id=int(division_data['id']),
        name=division_data['name'],
        bn_name=division_data['bn_name'],
        lat=float(division_data['lat']),
        long=float(division_data['long'])
    )
    division.save()

print("Data inserted successfully.")
