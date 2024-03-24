from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,CustomerForm
from .models import Customer
# Create your views here.
def home(request):
    Customers=Customer.objects.all()

    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been  logged In")
            return redirect('home')
        else:
            messages.success(request,"Oops Problem logging In")
            return redirect('home')
    else:
        return render(request, 'home.html',{ 'Customers':Customers})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, 'you have successfully registered')
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html', {'form': form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Customer.objects.get(id=pk)
        return render(request, 'customer_record.html', {'Customer_record': customer_record})
    else:
        messages.success(request, 'You must be logged in to view that page')
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record=Customer.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Record Deleted Successfully')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to do that')
        return redirect('home')

def add_customer(request):
    form=CustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_customer=form.save()
                messages.success(request, 'Customer added')
                return redirect('home')

        return render(request, 'add_customer.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in to do that')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record=Customer.objects.get(id=pk)
        form=CustomerForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that')
        return redirect('home')
