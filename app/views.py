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
    data = Api.objects.all()
    print(data.values())
    p_data = list(data.values())
    print(p_data)
    j_data = json.dumps(p_data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')



@csrf_exempt
def single_data(req,pk):
    user=Api.objects.filter(id=pk)
    if not user:
        p_data={'msg':"Enter id not present in db"}
        return HttpResponse(json.dumps(p_data),content_type='application/json')
    else:
        if req.method == 'PUT':
            data = req.body
            print(data)
            print(type(data))
            p_data = json.loads(data)
            print(p_data)
            print(type(p_data))
            if 'Name' in p_data and 'Age' in p_data and 'City' in p_data and 'Contact' in p_data:
                n=p_data.get('Name')
                a=p_data.get('Age')
                c=p_data.get('City')
                co=p_data.get('Contact')
                old_data=Api.objects.get(id=pk)
                old_data.Name=n
                old_data.Age=a
                old_data.City=c
                old_data.Contact=co
                old_data.save()
                p_data={'msg':'object created'}
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
        elif req.method == 'PATCH':
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
            if p_data:
                n=p_data.get('Name')
                a=p_data.get('Age')
                c=p_data.get('City')
                co=p_data.get('Contact')
                old_data = Api.objects.get(id=pk)
                if n:
                    old_data.Name = n
                if a:
                    old_data.Age=a
                if c:
                    old_data.City=c
                if co:
                    old_data.Contact=co
                old_data.save()
                p_data={'msg':"object partially updated"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            else:
                p_data={'msg':"object values are missing"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            
        elif req.method == 'DELETE':
            user= Api.objects.get(id=pk)  
            user.delete()
            p_data={'msg':"object deleted"}
            return HttpResponse(json.dumps(p_data),content_type='application/json')

        data = Api.objects.get(id=pk)
        print(data)
        print(type(data))
        p_data=model_to_dict(data)
        print(p_data)
        print(type(p_data))
        return HttpResponse(json.dumps(p_data),content_type='application/json')
    
@csrf_exempt
def single_url(req):
    data = req.body
    print(data)
    print(type(data))
    if data:
        p_data = json.loads(data)
        print(p_data)
        print(type(p_data))
        if 'id' in p_data:
            pk = p_data[id]
            if req.method == 'PUT':
                data = req.body
                print(data)
                print(type(data))
                p_data = json.loads(data)
                print(p_data)
                print(type(p_data))
                if 'Name' in p_data and 'Age' in p_data and 'City' in p_data and 'Contact' in p_data:
                    n=p_data.get('Name')
                    a=p_data.get('Age')
                    c=p_data.get('City')
                    co=p_data.get('Contact')
                    old_data=Api.objects.get(id=pk)
                    old_data.Name=n
                    old_data.Age=a
                    old_data.City=c
                    old_data.Contact=co
                    old_data.save()
                    p_data={'msg':'object created'}
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
            elif req.method == 'PATCH':
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
                if p_data:
                    n=p_data.get('Name')
                    a=p_data.get('Age')
                    c=p_data.get('City')
                    co=p_data.get('Contact')
                    old_data = Api.objects.get(id=pk)
                    if n:
                        old_data.Name = n
                    if a:
                        old_data.Age=a
                    if c:
                        old_data.City=c
                    if co:
                        old_data.Contact=co
                    old_data.save()
                    p_data={'msg':"object partially updated"}
                    return HttpResponse(json.dumps(p_data),content_type='application/json')
                else:
                    p_data={'msg':"object values are missing"}
                    return HttpResponse(json.dumps(p_data),content_type='application/json')
                
            elif req.method == 'DELETE':
                user= Api.objects.get(id=pk)  
                user.delete()
                p_data={'msg':"object deleted"}
                return HttpResponse(json.dumps(p_data),content_type='application/json')
            data = Api.objects.get(id=pk)
            print(data)
            print(type(data))
            p_data=model_to_dict(data)
            print(p_data)
            print(type(p_data))
            j_data=json.dumps(p_data)
            print(j_data)
            return HttpResponse(json.dumps(p_data),content_type='application/json')
        else:
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
            data = Api.objects.all()
            print(data.values())
            p_data = list(data.values())
            print(p_data)
            j_data = json.dumps(p_data)
            print(j_data)
            return HttpResponse(j_data,content_type='application/json')
            
    else:
        p_data={'msg':'atleast provide one empty dict'}
        j_data=json.dumps(p_data)
        print(j_data)
        return HttpResponse(j_data,content_type='application/JSON')  
                      
    # return HttpResponse(p_data,content_type='application/JSON')

            


    
    
            


