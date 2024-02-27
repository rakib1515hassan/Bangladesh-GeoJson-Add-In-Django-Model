from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class Division(TimestampedModel):
    name    = models.CharField(max_length=250, null=True, blank=True)
    bn_name = models.CharField(max_length=250, null=True, blank=True)
    lat     = models.DecimalField(max_digits=11, decimal_places=7, null=True,blank=True)
    long    = models.DecimalField(max_digits=11, decimal_places=7, null=True,blank=True)

    def __str__(self):
        return self.name
    

class District(TimestampedModel):
    division = models.ForeignKey(Division, related_name = 'district', on_delete=models.CASCADE)

    name    = models.CharField(max_length=250, null=True, blank=True)
    bn_name = models.CharField(max_length=250, null=True, blank=True)
    lat     = models.DecimalField(max_digits=11, decimal_places=7, null=True,blank=True)
    long    = models.DecimalField(max_digits=11, decimal_places=7, null=True,blank=True)

    def __str__(self):
        return f"{self.name}, {self.division.name}"
    


class Upazila(TimestampedModel):
    district = models.ForeignKey(District, related_name = 'upazila', on_delete=models.CASCADE)

    name    = models.CharField(max_length=250, null=True, blank=True)
    bn_name = models.CharField(max_length=250, null=True, blank=True)
    lat     = models.DecimalField(max_digits=11, decimal_places=7, null=True,blank=True)
    long    = models.DecimalField(max_digits=11, decimal_places=7, null=True,blank=True)

    def __str__(self):
        return f"{self.name}, {self.district.name}, {self.district.division.name}"
    


class PostCode(TimestampedModel):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)

    upazila    = models.CharField(max_length=250, null=True, blank=True)
    postOffice = models.CharField(max_length=250, null=True, blank=True)
    postCode     = models.DecimalField(max_digits=11, decimal_places=7, null=True,blank=True)

    def __str__(self):
        return f"""
                Upazila = {self.upazila}, 
                PostOffice = {self.postOffice}, 
                PostCode = {self.postCode}, 
                District = {self.district.name}, 
                Division = {self.division.name},
            """