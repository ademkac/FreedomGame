from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import math
import json
import logging
from collections import deque

# Create your views here.
from projekat1.minmaxutils import generate_next_move, generate_move, generate_random_move

vrstaIgre = None


def home(request):
    return render(request, 'projekat1/home.html')


def index(request):
    return render(request, 'projekat1/index.html')


""" ovde je teski nivo """


def sendstate(request):
    my_positions = request.GET.getlist("poteziCrnogIgraca[]", [])

    oponents_positions = request.GET.getlist("poteziBelogIgraca[]", "None")

    oponents_positions = [[int(oponents_positions[i + 1]), int(oponents_positions[i])] for i in
                          range(0, len(oponents_positions), 2)]
    my_positions = [[int(my_positions[i + 1]), int(my_positions[i])] for i in range(0, len(my_positions), 2)]

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
    my_positions = request.GET.getlist("poteziCrnogIgraca[]", [])

    oponents_positions = request.GET.getlist("poteziBelogIgraca[]", "None")

    oponents_positions = [[int(oponents_positions[i + 1]), int(oponents_positions[i])] for i in
                          range(0, len(oponents_positions), 2)]
    my_positions = [[int(my_positions[i + 1]), int(my_positions[i])] for i in range(0, len(my_positions), 2)]

    x = request.GET.get("indexOfX", "None")
    y = request.GET.get("indexOfY", "None")
    last_move = [int(y), int(x)]

    print("pozicije bijelog ", oponents_positions)
    print("pozicije crnog ", my_positions)
    print("poslednji potez ", last_move)
    move = generate_move(my_positions, oponents_positions, last_move)
    data = {
        'x': move[1],
        'y': move[0]
    }
    print("DATAA ", data)

    return JsonResponse(data)



""" ovde je kompjuter protiv kompjutera """


def sendstate2(request):
    koIgra = request.GET.get("comp1ORcomp2", "None")
    indX = request.GET.get("indexOfX", "None")
    indY = request.GET.get("indexOfY", "None")

    pozicijeCrnog = request.GET.getlist("poteziCrnogIgraca[]", [])
    pozicijeBelog = request.GET.getlist("poteziBelogIgraca[]", [])

    print(indX)
    print(indY)
    print(koIgra)
    print(pozicijeCrnog)
    print(pozicijeBelog)

    if int(koIgra) == 2:
        my_positions = request.GET.getlist("poteziCrnogIgraca[]", [])

        oponents_positions = request.GET.getlist("poteziBelogIgraca[]", "None")

        oponents_positions = [[int(oponents_positions[i + 1]), int(oponents_positions[i])] for i in
                              range(0, len(oponents_positions), 2)]
        my_positions = [[int(my_positions[i + 1]), int(my_positions[i])] for i in range(0, len(my_positions), 2)]

        x = request.GET.get("indexOfX", "None")
        y = request.GET.get("indexOfY", "None")
        last_move = [int(y), int(x)]
        print("pozicije bijelog ", oponents_positions)
        print("pozicije crnog ", my_positions)
        print("poslednji potez ", last_move)
        move = generate_next_move(my_positions, oponents_positions, last_move)
        data = {
            'x': move[1],
            'y': move[0]
        }
        print("DATAA ", data)

        return JsonResponse(data)

    else:
        my_positions = request.GET.getlist("poteziBelogIgraca[]", [])

        oponents_positions = request.GET.getlist("poteziCrnogIgraca[]", [])

        if len(my_positions) == 0:
            data = {
                'x': random.randint(0, 9),
                'y': random.randint(0, 9)
            }
            return JsonResponse(data)

        oponents_positions = [[int(oponents_positions[i + 1]), int(oponents_positions[i])] for i in
                              range(0, len(oponents_positions), 2)]
        my_positions = [[int(my_positions[i + 1]), int(my_positions[i])] for i in range(0, len(my_positions), 2)]

        x = request.GET.get("indexOfX", "None")
        y = request.GET.get("indexOfY", "None")
        last_move = [int(y), int(x)]
        print("pozicije crnog ", my_positions)
        print("pozicije bijelog ", oponents_positions)
        print("poslednji potez ", last_move)
        move = generate_next_move(my_positions, oponents_positions, last_move)
        data = {
            'x': move[1],
            'y': move[0]
        }

        return JsonResponse(data)


""" ovde je laki nivo """


def sendstate3(request):
    my_positions = request.GET.getlist("poteziCrnogIgraca[]", [])

    oponents_positions = request.GET.getlist("poteziBelogIgraca[]", [])
    print(oponents_positions)
    oponents_positions2 = [[int(oponents_positions[i + 1]), int(oponents_positions[i])] for i in
                          range(0, len(oponents_positions), 2)]
    my_positions2 = [[int(my_positions[i + 1]), int(my_positions[i])] for i in range(0, len(my_positions), 2)]

    x = request.GET.get("indexOfX", "None")
    y = request.GET.get("indexOfY", "None")
    last_move = [int(y), int(x)]

    my_positions = []
    for i in my_positions2:
        if i not in my_positions:
            my_positions.append(i)

    oponents_positions = []
    for i in oponents_positions2:
        if i not in oponents_positions:
            oponents_positions.append(i)
    #my_positions = list(dict.fromkeys(my_positions))
    print(my_positions)
    print(oponents_positions)
    #oponents_positions = list(dict.fromkeys(oponents_positions))
    print(last_move)
    move = generate_random_move(my_positions, oponents_positions, last_move)
    data = {
        'x': move[1],
        'y': move[0]
    }

    return JsonResponse(data)
