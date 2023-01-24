from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def menu(request):
    return render(request,"menu.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    
    data={}
    try:
        if request.method=='POST':
            n1=(request.POST['name'])
            n2=(request.POST['email'])
            n3=(request.POST['contact'])
            n4=(request.POST['msg'])
            

            
            data={
                "n1":n1,
                "n2":n2,
                "n3":n3,
                "n4":n4
                
            }
        
            return HttpResponseRedirect('/services/')
    except:
        pass    
    return render(request,"contact.html",data)
