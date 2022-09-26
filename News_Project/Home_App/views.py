from email.message import Message
from unicodedata import category
from django.shortcuts import render,redirect
from Home_App.models import *
from date_time import today
from News_App.models import News
from Category_App.models import News_Category
from Sub_Category_App.models import Sub_Category
from django.contrib.auth import login,logout,authenticate


# Create your views here.

#Home Views
def home(request):
    news = News.objects.all().order_by('-pk')
    category = News_Category.objects.all()
    sub_category = Sub_Category.objects.all()

    return render(request,'front/Home/home.html',{'news':news,'category':category,'sub_category':sub_category})

#Contact Views
def contact(request):
    Added_date = today()
    #get form Data
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('msg')

        if name != "" and email != "" and message != "" and subject != "":
            contact_data = Contact(Name = name, Email = email, Subject  = subject, Message = message, Added_date = Added_date) 
            contact_data.save()
            return redirect('home')

        else:
            pass

    return render(request,'front/Home/contact.html')

#About Views
def about(request):
    return render(request,'front/Home/about.html')

#Login Views
def login(request):
    if request.method=='POST':
        
        u_user = request.POST.get('username')
        u_pass = request.POST.get('password')
        
        if u_user != "" and u_pass != "" :
            user = authenticate(username=u_user, password=u_pass)
            
            if user != None :
                login(request,user)
                return redirect('panel')

    return render(request, 'front/Home/login.html')


#Log_out Views
def log_out(request):
    logout(request)
    return redirect('my_login')

#error
def error(request):
    return render(request,'front/error.html')

#Panel Views
def panel(request):
    # login check start
    #if not request.user.is_authenticated :
    #    return redirect('my_login')
    # login check end
    return render(request,'back/Home/home.html')
    #return render(request,'back/main.html')
