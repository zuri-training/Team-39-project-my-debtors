from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .decorators import not_user,users
# from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.forms import UserCreationForm
from .models import School,Debtors,Debt, Article, Account,MyAccountManager
# from Deudoras import debtors
from django.template import Context
# Create your views here.
def user_try(request):
    form = NewUserForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request,'debtors/test.html',context)


def parentprofile(request):
    return render(request,'debtors/dashboard_profile.html')
def Landing(request):
    return render(request, "debtors/index.html")
    
def SchoolSignup(request):
    
    # if form._
    if request.method == "POST":
        school_name = request.POST.get('SchoolName')
        email = request.POST.get('SchoolEmail')
        location = request.POST.get('SchoolAddress')
        lga = request.POST.get('LGA')
        cac = request.POST.get('SchoolCAC')
        password = request.POST.get('Password')
        print(email)
        # if location != 'gbagada':
    #         messages.error(request, "School is outside our jurisdiction.")
    #         return redirect('home')
    #     if User.objects.filter(email=email.exists()):
    # #         messages.error(request, "Email Already Registered! Try Login Instead")
    # #         return redirect('home')
    #     if password != confirm_password:
    # #         messages.error(request, "Passwords didn't matched!!")
    # #         return redirect('home')
        # account = MyAccountManager.create_user(email=email,name=school_name,password=password)
        acc=Account.objects.create(email=email,name =school_name, password =password)

        myuser = School.objects.create(account= Account.objects.get(email =email,name =school_name,password= password),location =location, CAC =cac, Local_government =lga)
        group = Group.objects.get(name ='Schools')
        acc.groups.add(group)
        # School.objects.create(user)
        
        myuser.is_active = True
        

        messages.success(request, 'Your account has been succesfully created')

        return redirect("Sclogin")

    return render(request,"debtors/signup_school.html")
def add_debtor(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('Email')
        location = request.POST.get('Address')
        contact = request.POST.get('contact')
        
        
       
        acc=Account.objects.create(email=email,name =name, password ='0000')

        myuser = Debtors.objects.create(account= Account.objects.get(email =email,name =name,password= '0000')
        ,address =location, contact =contact)
        group = Group.objects.get(name ='Student')
        acc.groups.add(group)
        # School.objects.create(user)
        
        myuser.is_active = True
        

        messages.success(request, 'Your account has been succesfully created')

        return redirect("Sclogin")
    return render(request,'debtors/add_debtor.html')
def need_help(request):
    return render(request,'debtors/need_help.html')


def about_us(request):
    
    return render(request,'debtors/about us.html')

def SchoolSignin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print('done')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            
            school_name =user.name
            id = user.id
            
            login(request, user)
            # context= {'name':name,'id' :id} 
            return redirect( "SchoolHome")

        else:
            messages.error(request, "Bad credentials!!")
            

        

    return render(request, "debtors/login/login-school.html")

def dispute(request):
    return render(request,'debtors/dispute.html')
def UserSignin(request):

    if request.method == 'POST':
        print('done')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            
            username =user.username
            login(request, user)
            return redirect( "UserHome")

        else:
            messages.error(request, "Bad credentials!!")

        return redirect('landing')


    return render(request, "debtors/login/login-students.html")


@login_required
def debt_by_debtor(request,pk):
    debt = Debt.objects.get(debtors_id = pk)
    return render(request,"debtors/debts.html",{'debts':debt})

    








def loginStudents(request):
    return render(request,'debtors/login/login-students.html')

def loginUser(request):
    return render(request,'debtors/login/login-users.html')


def signupuser1(request):
    return render(request, 'debtors/SignUpNormalUser1.html')

def signupuser2(request):
    return render(request, 'debtors/SignUpNormalUser2.html')







def signout(request):
    logout(request)
    messages.success(request, "logged out succesfully")
    return redirect( 'home' )









# @users(allowed_roles=['school'])

def SchoolHome(request):
    
    user = request.user.id
    ob = Debt.objects.filter(School_id =user)
    sum = 0
    for i in ob:
        sum+= i.amount
    schools =School.objects.all()
    n_schools = len(schools)
    print( n_schools )
    # print(user)
    # sc = Debtors.objects.filter(school_id =user.id).order_by('-id')[:10:-1]
#    'sc':sc
    context ={'ns':n_schools,'sum':sum}
    # print(context['ns'])
    
    return  render(request, 'debtors/school_dashboard.html',context)









def Debtors(request,pk):
    debtor = Debtors.objects.get(School_id = pk )
    return render(request, 'debtors/debtors_list.html',{'debtors': debtor})
def Schools(request):
    schools = School.objects.all()
    return render(request,'debtors/school_list.html',{'schools': schools})
def debt_by_school(request,pk):
    debt = Debt.objects.get(school_id = pk)
    return render(request,"debtors/debtors.html",{'debts':debt})

def Articles(request):
    articles = Article.objects.all()
    return render(request,'debtors/articles.html',{'articles': articles})






def Contactus(request):
    return render (request,'debtors/contact.html')


def forgot(request):
    return render(request, 'debtors/forgot.html')



# @users(allowed_roles=['student'])

def UserHome(request):
    # , pk
    # user = Debtors.objects.get(id = pk)
    # debt = request.user.Debt.all()
    # ,{'debt':debt,'user':user}
    return render(request,'debtors/dashboard_parents.html')



    #     
        
    #     
        
    #     
        









    







=======
>>>>>>> origin/psyche-complete
