from django.shortcuts import render
from myapp.models import Division, District, Upazila, PostCode
from django.http import HttpResponse, HttpResponseRedirect 

# Create your views here.
def test(request):
    district = PostCode.objects.filter(district = 2)

    print("--------------------")
    print("district =", district)
    print("--------------------")
    return HttpResponse()