from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)

        try:
            # This queries the database to find a Customer object where the email matches the user-provided email.
            customer = Customer.objects.get(email=email) 
            # This compares the password stored in the database (customer.password) with the password entered by the user. 
            if customer.password == password:  
                request.session['customer_id'] = customer.id  # Store session data
                
                return redirect('dashboard')  # Redirect to home page   
            else:
                messages.error(request, "Invalid credentials!")
                return redirect('login')
        except Customer.DoesNotExist:
            messages.error(request, "User not found!")
            return redirect('login')

    return render(request, 'analysis/login.html') 

def forgot_password(request):
    return render(request, 'analysis/forgot-password.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['passwd1']
        password2 = request.POST['passwd2']

        print(fname, lname, email, password1, password2)

        if password1 != password2:
            messages.warning(request, "Passwords do not match!")
            return redirect('register')

        # Check if email already exists
        if Customer.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Please use a different one!")
            return redirect('register')

        if fname and email and lname and password1:
            customer = Customer(first_name=fname, email=email, last_name=lname, password=password1)
            customer.save()
            messages.success(request, "Account created successfully! You can now log in.")
        else:
            messages.warning(request, "All fields are required!")
            return redirect('register')

    return render(request, "analysis/register.html")

