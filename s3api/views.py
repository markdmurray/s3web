from django.shortcuts import render
import boto3

# Create your views here.
def index(request):
    client = boto3.client('s3')
    list_buckets = client.list_buckets()
    output = list_buckets['Buckets']

    return render(
        request,
        'index.html',
        context={'list_of_buckets':output},
    )