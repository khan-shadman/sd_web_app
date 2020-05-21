from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.conf import settings
import json
from datetime import date
import pandas as pd 
from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen
from cwift_data.serializers import CWIFTSerializer
from cwift_data.models import CWIFT
from rest_framework import generics 

from django.conf import settings 
import os

# Create your views here.

class CWIFTALLView(APIView):
    # serializer_class = CWIFTSerializer
    # queryset = CWIFT.objects.all()


    # @api_view(["POST"])
    def get(self, request):

        filePath = 'CWIFT2015_LEA1314.txt'

        try:
            # attributes = request.GET.get('attributes', ['ALL'])
            # year = request.GET.get('year', date.today().year)

            # resp = urlopen("https://nces.ed.gov/programs/edge/data/EDGE_ACS_CWIFT2015.zip")
            # f = ZipFile(BytesIO(resp.read())).extract('CWIFT2015_LEA1314.txt')

            # myzipfile = zipfile.ZipFile(StringIO(get_zip_data()))

            # for name in myzipfile.namelist():
            #     if str(name).find("LEAID") != -1:
            #         cwift_df = pd.read_csv(name, delimiter=' ')

            filePath = 'CWIFT2015_LEA1314.txt'
            filePath = open(os.path.join(settings.BASE_DIR, 'cwift_data\\static\\'+filePath))
            cwift_df = pd.read_csv(filePath, delimiter='\t')[['LEAID', 'LEA_NAME', 'LEA_CWIFTEST']]
            cwift_df = cwift_df.rename(columns={'LEA_CWIFTEST': 'CWIFT'})
            return HttpResponse(cwift_df.to_html())
            # return JsonResponse(cwift_df.to_json(orient='records'),safe=False)

        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def cwift_json(request):

    try:
        filePath = 'CWIFT2015_LEA1314.txt'
        filePath = open(os.path.join(settings.BASE_DIR, 'cwift_data\\static\\'+filePath))
        cwift_df = pd.read_csv(filePath, delimiter='\t')
        return JsonResponse(cwift_df.to_json(orient='records'), safe=False)
    except ValueError as e:
        data = [{}]

    return JsonResponse(data, safe=False)

def cwift_table(request):

    try:
        filePath = 'CWIFT2015_LEA1314.txt'
        filePath = open(os.path.join(settings.BASE_DIR, 'cwift_data\\static\\'+filePath))
        cwift_df = pd.read_csv(filePath, delimiter='\t')
        return HttpResponse(cwift_df.to_html())

    except ValueError as e:
        data = [{}]

    return JsonResponse(data, safe=False)

def table(request):
    return render(request, os.path.join(settings.BASE_DIR, 'cwift_data\\templates\\table.html'))

def sample_render(request):
    return render(request, os.path.join(settings.BASE_DIR, 'cwift_data\\templates\\sample.html'))

def scatter(request):
    return render(request, os.path.join(settings.BASE_DIR, 'cwift_data\\templates\\scatter.html'))

def bar(request):
    return render(request,os.path.join(settings.BASE_DIR, 'cwift_data\\templates\\bar.html') )