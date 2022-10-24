from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt

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

def logout(request):
    del request.session['user']
    request.session.modified=True
    return redirect('login')

def get_current_session():
    return Session.objects.all().order_by('-id').first()

def get_objects(request):
    return{
        'users':User.objects.all(),
        'usertypes':UserType.objects.all(),
        'posters':User.objects.filter(type=1),
        'posts':Post.objects.all().order_by('-id'),
        'texts':Content.objects.all().order_by('-id'),
        'accounts':Account.objects.all().order_by('-id'),
        'unassigned_accounts':Account.objects.filter(isOccupy=False),
        'current_session':Session.objects.all().order_by('-id').first(),
        'session_posts':Post.objects.filter(session=get_current_session().id),
        'user_posts':Post.objects.filter(user=int(request.session['user']['id'])),
        'user_texts':Content.objects.filter(user=int(request.session['user']['id'])),
        'user_accounts':Account.objects.filter(assignedTo=int(request.session['user']['id'])),
        'unassigned_texts':Content.objects.filter(isUsed=False,session=get_current_session().id),
    }

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
        type=UserType.objects.get(id=1),
    )
    return redirect('dashboard')

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
        return render(request,'index.html',{'msg':'E-mail ou mot de passe invalide!'})
    except:return render(request,'index.html',{'msg':'E-mail ou mot de passe invalide!'})

def dashboard(request):
    # Session.objects.create(
    #     startDate=datetime.date.today()
    # )
    if 'user' not in request.session.keys():
        return redirect('login')
    return render(request,'dashboard/index.html',get_objects(request))

def acounts(request):
    if 'user' not in request.session.keys():
        return redirect('login')
    return render(request,'dashboard/comptes.html',get_objects(request))

############################    CONTENTS

def contents(request):
    if 'user' not in request.session.keys():
        return redirect('login')
    return render(request,'dashboard/textes.html',get_objects(request))

def save_content(request):
    Content.objects.create(
        ContentText=request.POST.get('text'),
        stars=int(request.POST.get('stars')),
        session=get_current_session()
        #gender=request.POST.get('gender')
    )
    return redirect('contents')

@csrf_exempt
def assign_content(request):
    c=Content.objects.get(id=int(request.POST.get('id')))
    c.assignTo(request.session['user']['id'])
    return HttpResponse("ok")


####################    ACCOUNTS

def account_save(request):
    Account.objects.create(
        fullName=request.POST.get('fullname'),
        passwd=request.POST.get('passwd'),
        country=request.POST.get('country'),
    )
    return redirect('accounts')

@csrf_exempt
def assign_account(request):
    a=Account.objects.get(id=int(request.POST.get('id')))
    a.assign_user(request.session['user']['id'])
    return HttpResponse("ok")

######################      POSTES

def posts(request):
    if 'user' not in request.session.keys():
        return redirect('login')
    return render(request,'dashboard/postes.html',get_objects(request))

def save_post(request):
    
    Post.objects.create(
        user=User.objects.get(id=request.session['user']['id']),
        content=Content.objects.get(id=int(request.POST.get('content'))),
        account=Account.objects.get(id=int(request.POST.get('account'))),
        session=get_current_session(),
        shot=request.FILES.get('shot')
    )
    return redirect('posts')


def save_user(request):
    User.objects.create(
        lname=request.POST.get('lname'),
        fname=request.POST.get('fname'),
        email=request.POST.get('email'),
        telephone=request.POST.get('phone'),
        passwd=request.POST.get('mdp'),
        type=UserType.objects.get(id=1),
    )
    return redirect('login')
@csrf_exempt
def validate_post(request,id):
    p=Post.objects.get(id=id).validate()
    return redirect('posts')

@csrf_exempt
def reject_post(request,id):
    p=Post.objects.get(id=id).validate()
    return redirect('posts')
