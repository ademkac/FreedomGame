from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import math
import json
import logging
from collections import deque


# Create your views here.



def home(request):
    return render(request, 'projekat1/home.html')


def index(request):
    return render(request, 'projekat1/index.html')

def sendstate(request):

    indexOfX = request.GET.get("indexOfX", "None")
    indexOfY = request.GET.get("indexOfY", "None")
    poteziBelog = request.GET.getlist("poteziBelogIgraca[]")
    poteziCrnog = request.GET.getlist("poteziCrnogIgraca[]") 
    logging.warn("potezibelog: " + poteziBelog)

    print(poteziBelog)
    
    data = {
        'x': indexOfX,
        'y': 3
    } 

    return JsonResponse(data)

def sendstate1(request):

    """ vrstaIgre = request.GET.get("vrstaIgre", "None")
    logging.warn("Nacin igre: " + vrstaIgre) """

    return JsonResponse(""" data """)