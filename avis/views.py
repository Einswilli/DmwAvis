from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    
    # b=UserType.objects.create(
    #     name="POSTEUR",
    #     description="Pour les posteurs rémunirés",
    #     acces="POST"
    # )
    # c=UserType.objects.create(
    #     name="CONTROLLEUR",
    #     description="Pour les controlleurs",
    #     acces="CONTROL"
    # )
    # a=UserType.objects.create(
    #     name="SUPER_ADMIN",
    #     description="SuperAdmins",
    #     acces="ALL"
    # )
    # User.objects.create(
    #     fname="Einswilli",
    #     lname="DotPy",
    #     email="einswilligoeh@gmail.com",
    #     telephone="+22898490524",
    #     passwd="frido015",
    #     type=a,
    # )
    # User.objects.create(
    #     fname="Julienoh",
    #     lname="DotPy",
    #     email="adenovijulien@gmail.com",
    #     telephone="+22893764317",
    #     passwd="password",
    #     type=a,
    # )
    return render(request, 'index.html')

def poster_register(request):
    return render(request,'register.html')

def poster_save(request):
    # ENREGISTRE SEULEMENT LES POSTEURS

    User.objects.create(
        fname=request.POST.get('fname'),
        lname=request.POST.get('lname'),
        email=request.POST.get('email'),
        telephone=request.POST.get('telephone'),
        passwd=request.POST.get('passwd'),
        type=UserType.objects.get(id=int(request.POST.get('type'))),
    )

def login(request):
    e=request.POST.get('email')
    p=request.POST.get('mdp')
    try:
        u=User.objects.get(email=e)
        if u.passwd==p:
            usr={
                'id':u.id,
                'lname':u.lname,
                'fname':u.fname,
                'email':u.email,
                'phone':u.telephone,
                'passwd':u.passwd,
                'type':{
                    'id':u.type.id,
                    'name':u.type.name,
                    'description':u.type.description,
                    'acces':u.type.acces,
                }
            }
            request.session['user']=usr
            request.session.modified=True
            return redirect('dashboard')
    except:return render(request,'index.html',{'msg':'E-mail ou mot de passe invalide!'})

def dashboard(request):
    return render(request,'dashboard/index.html')


