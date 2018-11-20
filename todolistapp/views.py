from django.shortcuts import render
from .forms import ToDoListForm
from .models import Todolist
import datetime
from django.http import HttpResponse,HttpResponseRedirect
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

def index(request):
    if request.method == "POST":
        tdl = Todolist(title=request.POST.get("title"),
                       description=request.POST.get("description"),
                       status=request.POST.get("status"))
        tdl.save()
    obj=Todolist.objects.filter(valid=True)
    return render(request,'index.html',{'obj':obj})

def update(request):
    id=request.GET.get('id',-1)
    if int(id) >= 0:
        Todolist.objects.filter(id=int(id)).update(title=request.POST.get("title"),
                                                description=request.POST.get("description"),
                                                status=request.POST.get("status"))

    return HttpResponseRedirect("/app/index/")

def remove(request):
    id = request.GET.get('id', -1)
    if int(id) >= 0:
        Todolist.objects.filter(id=int(id)).update(valid=False)

    return HttpResponseRedirect("/app/index/")


def edit(request):
    print (request.GET)
    id = request.GET.get('id',-1)
    data = None
    obj = Todolist.objects.filter(valid=True)
    if int(id) >= 0:
        data = Todolist.objects.get(id=int(id))
    return render(request,'edit.html',{'data':data,'obj':obj})

def api(request):
    # obj=Todolist.objects.all()
    templist=[]
    id=request.GET.get('id',-1)
    if int(id)>= 0:
        data=Todolist.objects.get(id=int(id))
        obj = json.dumps(
            data.getDict(),
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )
    else:
        for obj in Todolist.objects.all():
            templist.append(obj.getDict())
        obj=json.dumps(
            templist,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )

    return HttpResponse(obj)

