from django.shortcuts import render,redirect
from  .models import Userprofile




def home(request):
    if request.method=='GET':
        return render(request,'home.html')
    if request.method=='POST':

        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phno=request.POST['phno']
        gender=request.POST['gender']
        user = Userprofile.objects.create_user( email=email, first_name=fname, last_name=lname,phone_no=phno,gender=gender)
        user.save()

        return render(request, 'home.html')

def log_in(request):
    if request.method=='POST':
        email=request.POST['email']

        try:
            profile=Userprofile.objects.get(email=email)
            return render(request,'home2.html',{'profile':profile,'message':"user found"})

        except Userprofile.DoesNotExist:
            return render(request, 'home2.html', { 'message':"user not  found"})
    else:
        return render(request,'home1.html')