from django.shortcuts import render
import boto3
from .forms import ListAwsRegions

# Create your views here.
def index(request):
    #client = boto3.client('s3')
    #list_buckets = client.list_buckets()
    #output = list_buckets['Buckets']

    form = ListAwsRegions()
    #return render(
    #    request,
    #    'index.html',
    #    context={'list_of_buckets':output},
    #)
    return render(
        request,
        'index.html',
        context={'form':form}
    )

''' from django.views.generic import CreateView
from .models import ListRegions
from .forms import ListAwsRegions

class RegionListView(CreateView):
    model = ListRegions
    #template_name = 'index.html'
    form_class = ListAwsRegions '''