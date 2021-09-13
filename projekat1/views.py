from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import math
import json
import logging
from collections import deque


# Create your views here.
from projekat1.minmaxutils import generate_next_move

vrstaIgre = None

def home(request):
    return render(request, 'projekat1/home.html')


def index(request):
    return render(request, 'projekat1/index.html')

""" ovde je teski nivo """
def sendstate(request):
    
    my_positions = request.GET.getlist("poteziCrnogIgraca[]", [])

    oponents_positions = request.GET.getlist("poteziBelogIgraca[]", "None")


    oponents_positions = [[int(oponents_positions[i+1]), int(oponents_positions[i])] for i in range(0, len(oponents_positions), 2)]
    my_positions = [[int(my_positions[i+1]), int(my_positions[i])] for i in range(0, len(my_positions), 2)]


    x = request.GET.get("indexOfX", "None")
    y = request.GET.get("indexOfY", "None")
    last_move = [int(y), int(x)]
    """print("pozicije bijelog ", oponents_positions)
    print("pozicije crnog ", my_positions)
    print("poslednji potez ", last_move)"""
    move = generate_next_move(my_positions, oponents_positions, last_move)

    data = {
        'x': move[1],
        'y': move[0]
    }

    return JsonResponse(data)

""" ovde je srednji nivo """
def sendstate1(request):
    data = {
        'x': 1,
        'y': 1
    }

    return JsonResponse( data )

""" ovde je kompjuter protiv kompjutera """
def sendstate2(request):
    koIgra= request.GET.get("comp1ORcomp2", "None")
    print(koIgra)
    if vrstaIgre == "cvsc":
        print("vrsta igre je cvsc")
    elif vrstaIgre == "ivsi":
        print("vrsta igre je ivsi") 
    print(vrstaIgre)
    data = {
        "x": 0,
        "y": 1
    }

    return JsonResponse(data)

""" ovde je laki nivo """
def sendstate3(request):
    data={
        'x': 1,
        'y': 0
    }
    return JsonResponse( data)