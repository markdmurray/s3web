from django import forms
import boto3
from .models import ListRegions
from django.forms import ModelForm

''' class ListAwsRegions(forms.Form):
    def list_regions(self):
        region_list = ['test']
        client = boto3.client('ec2')
        response = client.describe_regions()
        region = response['Regions']
        description = forms.CharField(max_length=9)
        form_list = forms.MultipleChoiceField(required=False,widget=forms.Select,choices=region_list)

        for x in region:
            region_list.append(x['RegionName'])
        return form_list '''

class ListAwsRegions(ModelForm):
    class Meta:
        model = ListRegions
        fields = ['regions']



