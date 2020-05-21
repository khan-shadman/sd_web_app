from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.http import HttpResponse
import json
import os
import pandas as pd
# import nces

# Create your views here.

def nces_json(request):
    # type in year
    try:
        filePath = 'rawCCD.csv'
        filePath = open(os.path.join(settings.BASE_DIR, 'nces_data_api\\static\\'+filePath))
        nces_df = pd.read_csv(filePath, delimiter=',')
        return JsonResponse(nces_df.to_json(orient='records'), safe=False)
    except ValueError as e:
        data = [{}]

    return JsonResponse(data, safe=False)

def nces_table(request):
    return render(request, os.path.join(settings.BASE_DIR, 'nces_data_api\\templates\\table.html'))