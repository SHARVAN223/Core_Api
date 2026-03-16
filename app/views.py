from django.shortcuts import render
from django.http import HttpResponse
from app.models import Api
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json

@csrf_exempt
def all_data(req):
    if req.method == "POST":
        data = req.body
        print(data)
        print(type(data))
        p_data = json.loads(data)
        print(p_data)
        print(type(p_data))
        n=p_data.get('Name')
        a=p_data.get('Age')
        c=p_data.get('City')
        co=p_data.get('Contact')
        if 'Name' in p_data and 'Age' in p_data and 'City' in p_data and 'Contact' in p_data:
            Api.objects.create(Name=n,Age=a,City=c,Contact=co)
            p_data={"msg":"Object Created"}
            return HttpResponse(json.dumps(p_data),content_type='application/json')
        else:
            if not 'Name' in p_data:
                p_data={'msg':"Name field are missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            if not 'Age' in p_data:
                p_data={'msg':"Age field are missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            if not 'City' in p_data:
                p_data={'msg':"City field are missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            if not 'Contact' in p_data: 
                p_data={'msg':"contact field are missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')

    # data = Api.objects.all()
    # print(data.values())
    # p_data = list(data.values())
    # print(p_data)
    # j_data = json.dumps(p_data)
    
    # print(j_data)
    # return HttpResponse(j_data,content_type='application/json')




def single_data(req,pk):
    data = Api.objects.get(id=pk)
    print(data)
    print(type(data))
    p_data=model_to_dict(data)
    print(p_data)
    print(type(p_data))
    return HttpResponse(p_data,content_type='application/json')
