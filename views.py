from django.shortcuts import render, redirect
from django.views.generic import View
import numpy as np
from django.contrib.sessions.models import Session
from django.http import HttpResponse

def intro(request):
    return render(request, "intro.html")

def clue_2(request):
    return render(request, "clue_2.html")

def clue_3(request):
    return render(request, "clue_3.html")