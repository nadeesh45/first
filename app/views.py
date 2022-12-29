from django.shortcuts import render
import HTTPRESPONSE from django.http

# Create your views here.
def index(request):
    return HTTPRESPONSE("iam project K"),