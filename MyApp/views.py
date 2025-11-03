# from email.mime import message
# from pyexpat import model
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Car, Order, Contact

def index(request):
	return render(request,'index.html')

def about(request):
    return render(request,'about.html ')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).first():
            messages.error(request,"Username already taken")
            return redirect('register')
        if User.objects.filter(email = email).first():
            messages.error(request,"Email already taken")
            return redirect('register')

        if password != password2:
            messages.error(request,"Passwords do not match")
            return redirect('register')

        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.name = name
        myuser.save()
        messages.success(request,"Your account has been successfully created!")
        return redirect('signin')


    else:
        print("error")
        return render(request,'register.html')
    

def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request,"Successfully logged in!")
            return redirect('vehicles')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')

    else:
        print("error")
        return render(request,'login.html')

def signout(request):
        logout(request)
        # messages.success(request,"Successfully logged out!")
        return redirect('home')
    
    # return HttpResponse('signout')

def vehicles(request):
    cars = Car.objects.filter(vehicle_type='car')
    # print(cars)
    params = {'car':cars}
    return render(request,'vehicles.html ',params)

def bill(request):
    cars = Car.objects.filter(vehicle_type='car')
    params = {'cars':cars}
    return render(request,'bill.html',params)

def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        billcity = request.POST.get('billcity','')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss','')
        date = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')
        # print(request.POST['cars11'])
        
        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,city=billcity,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect('home')
    else:
        # Redirect to bill page if accessed via GET
        return redirect('bill')

@login_required
def manage_cars(request):
    # Get all orders for the current user
    orders = Order.objects.filter(email=request.user.email)
    return render(request, 'manage_cars.html', {'orders': orders})

@login_required
def report_issue(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    
    # Verify that the order belongs to the current user
    if order.email != request.user.email:
        messages.error(request, "You don't have permission to report an issue for this order.")
        return redirect('manage_cars')
    
    if request.method == "POST":
        issue = request.POST.get('issue', '')
        order.issue_reported = issue
        order.save()
        messages.success(request, "Issue reported successfully.")
    
    return redirect('manage_cars')

@user_passes_test(lambda u: u.is_staff)
def manage_orders(request):
    # Get all orders for admin to manage
    orders = Order.objects.all().order_by('-order_id')
    return render(request, 'manage_orders.html', {'orders': orders})

@user_passes_test(lambda u: u.is_staff)
def update_order_status(request, order_id, status):
    order = get_object_or_404(Order, order_id=order_id)
    
    if status in ['pending', 'approved', 'declined']:
        order.status = status
        order.save()
        messages.success(request, f"Order #{order_id} status updated to {status}.")
    else:
        messages.error(request, "Invalid status provided.")
    
    return redirect('manage_orders')

def bill(request):
    cars = Car.objects.all()
    params = {'cars':cars}
    return render(request,'bill.html',params)

def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname','')
        contactemail = request.POST.get('contactemail','')
        contactnumber = request.POST.get('contactnumber','')
        contactmsg = request.POST.get('contactmsg','')

        contact = Contact(name = contactname, email = contactemail, phone_number = contactnumber,message = contactmsg)
        contact.save()
    return render(request,'contact.html ')
