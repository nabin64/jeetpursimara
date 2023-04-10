from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def HOME(request):
    return render(request, 'Local/home.html')
