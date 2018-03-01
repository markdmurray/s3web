from django.db import models
#from .forms import ListAwsRegions

# Create your models here.
#region_list = ListAwsRegions().region_list()

list_regions = (('Sydney','ap-southeast-2'),
                ('Virginia', 'us-east-1'))

class ListRegions(models.Model):
    regions = models.CharField(max_length=20, choices=list_regions, default='test')
