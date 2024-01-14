from django.contrib import admin
from myapp.models import Division, District, Upazila, PostCode

# Register your models here.
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)
admin.site.register(PostCode)