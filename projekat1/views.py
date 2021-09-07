from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import math
import json
from collections import deque


# Create your views here.



def home(request):
    return render(request, 'projekat1/home.html')


def index(request):
    return render(request, 'projekat1/index.html')

