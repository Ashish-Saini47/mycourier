from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from myapp.models import Contact
from myapp.models import Courier_detail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
# Create your views here.
def logoutuser(request):
    logout(request)
    return redirect("/")



def index(request):

    return render(request, "index.html")

def about(request):
   # return HttpResponse("This is about about")
    return render(request, "about.html")
def service(request):
    #return HttpResponse("This is about service")
    return render(request, "service.html")
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        print(name)
        contact = Contact(name = name, email = email, phone = phone, query = query, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent. We contact you shortly!')
    #return HttpResponse("This is about contact")
    return render(request, "contact.html")
def loginuser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username= username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, "login.html")
        #return HttpResponse("This is about login")
    return render(request, "login.html")

def amount(request):
    print(request.user)
    if request.method=="POST":
        name = request.POST.get("name")
        contact_no=request.POST.get("contact")
        p_address=request.POST.get("p_address")
        pincode=request.POST.get("pincode")
        p_type=request.POST.get("p_type")
        t_weight=request.POST.get("weight")
        p_decs=request.POST.get("desc")
        p_time=request.POST.get("p_time")
        p_n_time=request.POST.get("time")
        r_name=request.POST.get("r_name")
        r_contact_no=request.POST.get("r_contact")
        d_address=request.POST.get("d_address")
        d_pincode=request.POST.get("d_pincode")
        
        courier_detail = Courier_detail(name = name, contact_no=contact_no, p_address=p_address, pincode=pincode,
        p_type=p_type, t_weight=t_weight, p_decs=p_decs, p_time=p_time, p_n_time=p_n_time, r_name=r_name, r_contact_no=r_contact_no, d_address=d_address,
        d_pincode=d_pincode, date = datetime.today())
        courier_detail.save()
    dict1={"weight":t_weight,
            "user": request.user}
    return render(request, "amount.html",dict1)

def register(request):
    return render(request, 'register.html')

def payment(request):
    if request.method=="POST":
        dict2={"t_amount":request.POST.get("t_amount")}

    return render(request, 'payment.html',dict2)