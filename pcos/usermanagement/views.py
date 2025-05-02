from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib import auth
from datetime import datetime
import datetime
from .forms import *
# def home(request):
#     return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def register(request):
    if request.method=='POST':
        # fname=request.POST['firstname']
        # lname=request.POST['lname']
        # phno=request.POST['phno']
        # email=request.POST['email']
        # pword=request.POST['pword']
        # print(fname)
        # print(lname)
        # print(phno)
        # print(email) 
        # print(pword)  

        # Register.objects.create_user(username=fname,email=email,last_name=lname,contact=phno,password=pword,userType="user")
        # message sucess redirection
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Access request for login has been submitted.")
        #return redirect('view_request_users')
            return redirect('/login')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

def sigin(request):
    print(request.method=='POST')
    if request.method=='POST':
        form=LoginForm(request.POST)
        uname=request.POST['username']
        pword=request.POST['password']
        user=authenticate(request,username=uname,password=pword)
        if user is None:
            messages.error(request,"inavlid username,password")
        login(request,user)
        request.session['uid']=user.id
        request.session['ut']=user.userType
        messages.success(request,"login successfully",extra_tags='login')
        return redirect('/')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})




def prediction(request):
    return render(request,'prediction.html')




def image_upload(request):
    return render(request,'image_upload.html')


def user(request):
    return render(request,'user.html')



def Resources(request):
    return render(request,'Resources.html')


def chat(request):
    return render(request,'chat.html')

def view_user(request):
    users = Register.objects.filter(userType="user")
    return render(request,'view_user.html',{'users':users})




def feed_back(request):
    if request.method=='POST':
        # experience=request.POST['experience']
        # comments=request.POST['comments']
        # print( experience)
        # print( comments)
        # Feedback.objects.create(experience=experience,comments=comments,Date_submitted=datetime.datetime.today())
        form = FeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            feedback=form.save(commit=False)
            feedback.user_id = Register.objects.get(id=request.user.id)
            feedback.save()
            messages.success(request,'Thank you for your feedback !',extra_tags='feedback')
            return redirect('/')
    else:
        form=FeedbackForm()
    return render(request,'feed_back.html',{'form':form})


def view_feedback(request):
    feedback=Feedback.objects.all().order_by('-Date_submitted')
    return render(request,'view_feedback.html',{'feedbacks':feedback})
         


def do_logout(request):
    auth.logout(request)
    return redirect('/')





# another template integration

def index(request):
    return render(request,'index.html')
