from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import user

# Create your views here.

def valid_account_logged_in(request):
    try:
        if request.session['user_status'].get('isLoggedIn') == True:
            if user.objects.filter(username = request.session['user_status'].get('username'), userid = request.session['user_status'].get('userid')).exists():
                #Logged in with valid credentials
                return True
            else:
                return False
        else:
            return False  
    except:
        return False  

def index(request):
    if valid_account_logged_in(request):
        user_details = user.objects.filter(username = request.session['user_status'].get('username'), userid = request.session['user_status'].get('userid') ).first()
        context = {
            'username': user_details.username,
            'gender': user_details.gender,
            'current_education': user_details.current_education,
            'stream': user_details.stream,
            'educational_institution': user_details.username,
            'target_exam': user_details.target_exam,
            'pincode': user_details.pincode,
            'city': user_details.city,
            'address': user_details.address,
            'state': user_details.state,
            'phone': user_details.phone,
            'email': user_details.email,
            'userid': user_details.userid,
        }
        return render(request, 'profile.html', {'context' : context})
    else:
        return redirect('login')

def subscriptions(request):
    if valid_account_logged_in(request):
        return render(request, 'subscriptions.html')
    else:
        return redirect('login')    

def updateAccount(request, update_key):
    if valid_account_logged_in(request):

        return HttpResponse(update_key)
    else:
        return redirect('login')    