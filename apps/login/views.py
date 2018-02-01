from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, "login/index.html", {'status':True})


def processReg(request):
    confirm = request.POST['confirm']
    response = User.objects.validate(request.POST)
    if not response['status']:
        return render(request, "login/index.html", response)
    request.session['user_id'] = response['user'].id
    return redirect(reverse('dashboard:landing')) # named routing

def processLog(request):
    request.session['user_id'] = User.objects.get(email=request.POST['email']).id
    return redirect('/dashboard/')

def logout(request):
    request.session.flush()
    return redirect('/')