from django.shortcuts import render
from django.http import HttpResponse
from app.models import Api
# Create your views here.
import json

def all_data(req):
    data = Api.objects.all()
    print(data.values())
    p_data = list(data.values())
    print(p_data)
    j_data = json.dumps(p_data)
    
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')