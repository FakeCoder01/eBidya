import json
from optparse import Values
import django
from django.forms import JSONField
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from requests import request
from account.models import user
import random
from django.utils.crypto import get_random_string
import datetime
import json
from course.models import jee, neet, cat, psu, boards, upsc, progm, comment, likes

from django.core.serializers import serialize
from django.db.models import Q 


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

    context = {

        'jee_videos_math' : jee.objects.filter(sub='MATH'),
        'jee_videos_physics' : jee.objects.filter(sub='PHYSICS'),
        'jee_videos_chemistry' : jee.objects.filter(sub='CHEMISTRY'),


        'neet_videos_biology' : neet.objects.filter(sub='BIOLOGY'),
        'neet_videos_physics' : neet.objects.filter(sub='PHYSICS'),
        'neet_videos_chemistry' : neet.objects.filter(sub='CHEMISTRY'),

        'cat_videos' : cat.objects.all(),
        'psu_videos' : psu.objects.all(),
        'boards_videos' : boards.objects.all(),
        'upsc_videos' : upsc.objects.all(),
        'progm_videos' : progm.objects.all(),
    }

    return render(request, 'index.html', {'context' : context})


def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword :
            gender = request.POST.get('gender')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            current_education = request.POST.get('current_education')
            stream =  request.POST.get('stream')
            educational_institution = request.POST.get('educational_institution')
            target_exam = request.POST.get('target_exam')

            #ADDRESS
            pincode = request.POST.get('pincode')
            
            city = request.POST.get('city')
            address = request.POST.get('address')
            state = request.POST.get('state')

            #CONTACT
            phone = request.POST.get('phone')
            email  = request.POST.get('email')

            if  user.objects.filter(email=email).exists():
                return render(request, 'signup.html',{'msg' : "Email already registered"})
            else:
                if  user.objects.filter(phone=phone).exists():
                    return render(request, 'signup.html',{'msg' : "Phone number already registered"})
                else:                        
                    #USERNAME
                    username = fname +  ' ' + lname
                    
                    #SYSTEM
                    userid = get_random_string(8)
                    otp = random.randint(100000, 999999)

                    password_hash = password
                    hash =  str(random.randint(100000, 999999))
                    created_on = datetime.datetime.now()
                    mobile_verify = 'pending'
                    email_verify = 'pending' 
                    token = '-'

                    #SUBSCRIPTION
                    jee_subid = '-'
                    neet_subid = '-'
                    board_subid = '-'
                    upsc_subid = '-'
                    cat_subid = '-'
                    progm_subid = '-'
                    psu_subid = '-'

                    save_user = user(gender = gender, username = username, current_education=current_education, stream=stream, educational_institution=educational_institution, target_exam=target_exam, pincode=pincode, city=city, address=address, state=state, phone=phone, email=email, userid=userid, otp=otp, password_hash=password_hash, hash=hash, created_on=created_on, mobile_verify=mobile_verify, email_verify=email_verify, token=token, jee_subid=jee_subid, neet_subid=neet_subid, board_subid=board_subid, upsc_subid=upsc_subid, cat_subid=cat_subid, progm_subid=progm_subid, psu_subid=psu_subid)

                    save_user.save()
                    return redirect('/course')
        else:
            return render(request, 'signup.html',{'msg' : "Password not match"})
    else:
        return render(request, 'signup.html',{'msg' : "Server Error"})

def signup(request):
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password_hash = request.POST.get('password')

        if  user.objects.filter(email=email).exists():
            if  user.objects.filter(password_hash=password_hash).exists():

                user_details = user.objects.get(email=email, password_hash=password_hash)

                request.session['user_status'] = {
                    'isLoggedIn' : True,
                    'username' : user_details.username,
                    'userid' : user_details.userid
                }
                    
                return redirect('/')
            else:
                return render(request, 'login.html', {'msg': "wrong email or password"})
        else:
            return render(request, 'login.html', {'msg': "wrong email or password"})
    else:   
        return render(request, 'login.html')

def logout(request):
    del request.session['user_status']
    return redirect('/')

def cart(request):
    return HttpResponse('<h1>CART</h1>')


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        context = {
            'jee_search' :  jee.objects.filter(Q(title__icontains=query) | Q(chapter_name__icontains=query) |  Q(description__icontains=query) | Q(topic__icontains=query)),
            'neet_search' :  neet.objects.filter(Q(title__icontains=query) | Q(chapter_name__icontains=query) |  Q(description__icontains=query) | Q(topic__icontains=query)),
            'boards_search' :  boards.objects.filter(Q(title__icontains=query) | Q(chapter_name__icontains=query) |  Q(description__icontains=query) | Q(topic__icontains=query)),
            'cat_search' :  cat.objects.filter(Q(title__icontains=query) | Q(chapter_name__icontains=query) |  Q(description__icontains=query) | Q(topic__icontains=query)),
            'upsc_search' :  upsc.objects.filter(Q(title__icontains=query) | Q(chapter_name__icontains=query) |  Q(description__icontains=query) | Q(topic__icontains=query)),
            'psu_search' :  psu.objects.filter(Q(title__icontains=query) | Q(chapter_name__icontains=query) |  Q(description__icontains=query) | Q(topic__icontains=query)),
            'progm_search' :  progm.objects.filter(Q(title__icontains=query) | Q(chapter_name__icontains=query) |  Q(description__icontains=query) | Q(topic__icontains=query)),
            'search_query' : query
        }
        return render( request, 'search.html', {'context' : context})
    else :
        return redirect('/')

def watch(request, exam_name, video_id):
    context = {
        'title' : 'Courses',
        'video_url' : 'watch?v=dfhjdfg'
    }
    if exam_name == 'jee':
        context = jee.objects.filter(video_id = video_id).first()
    elif exam_name == 'neet':
        context = neet.objects.filter(video_id = video_id).first()
    elif exam_name == 'boards':
        context = boards.objects.filter(video_id = video_id).first()
    elif exam_name == 'cat':
        context = cat.objects.filter(video_id = video_id).first()
    elif exam_name == 'psu':
        context = psu.objects.filter(video_id = video_id).first()  
    elif exam_name == 'progm':
        context = progm.objects.filter(video_id = video_id).first()
    elif exam_name == 'upsc':
        context = upsc.objects.filter(video_id = video_id).first()
    else:
        context = {
            'title' : 'error',
            'video_url' : 'watch?v=dfhjdfg',
        }   
    return render(request, 'watch.html', {'context': context, 'exam_name' : exam_name})

def comment_video(request):

    if valid_account_logged_in(request):

        if request.method == 'POST':
            comment_text = request.POST.get('text')
            comment_id = request.POST.get('comment_id')
            username = request.POST.get('user_name')
            userid = request.POST.get('user_id')
            video_id = comment_id


            created_on = datetime.datetime.now()

            save_comment = comment(video_id=video_id, comment_id=comment_id, userid=userid, username=username, comment_text=comment_text, created_on=created_on)
            save_comment.save()

            return JsonResponse(json.dumps({'res':'commented'}), safe=False)
        else:
            return redirect('/')    

    else:
            return redirect('/')    


def like_video(request):

    if valid_account_logged_in(request):

        if request.method == 'POST':

            video_id = request.POST.get('video_id')
            user_name = request.POST.get('user_name')
            user_id = request.POST.get('user_id')
            stream = request.POST.get('exam_name')

            if stream == 'jee':
                lks = jee.objects.filter(video_id=video_id).first()
                if likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).exists():
                    lks = lks.likes - 1
                    likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).delete()
                else:
                    lks = lks.likes + 1
                    save_like = likes(video_id=video_id, userid=user_id, username=user_name)
                    save_like.save() 
                jee.objects.filter(video_id=video_id).update(likes=lks)

            elif stream == 'neet':
                lks = neet.objects.filter(video_id=video_id).first()
                if likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).exists():
                    lks = lks.likes - 1
                    likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).delete()
                else:
                    lks = lks.likes + 1
                    save_like = likes(video_id=video_id, userid=user_id, username=user_name)
                    save_like.save() 
                neet.objects.filter(video_id=video_id).update(likes=lks)

            elif stream == 'psu':
                lks = psu.objects.filter(video_id=video_id).first()
                if likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).exists():
                    lks = lks.likes - 1
                    likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).delete()
                else:
                    lks = lks.likes + 1
                    save_like = likes(video_id=video_id, userid=user_id, username=user_name)
                    save_like.save() 
                psu.objects.filter(video_id=video_id).update(likes=lks)

            elif stream == 'cat':
                lks = cat.objects.filter(video_id=video_id).first()
                if likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).exists():
                    lks = lks.likes - 1
                    likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).delete()
                else:
                    lks = lks.likes + 1
                    save_like = likes(video_id=video_id, userid=user_id, username=user_name)
                    save_like.save() 
                cat.objects.filter(video_id=video_id).update(likes=lks)

            elif stream == 'upsc':
                lks = upsc.objects.filter(video_id=video_id).first()
                if likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).exists():
                    lks = lks.likes - 1
                    likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).delete()
                else:
                    lks = lks.likes + 1
                    save_like = likes(video_id=video_id, userid=user_id, username=user_name)
                    save_like.save() 
                upsc.objects.filter(video_id=video_id).update(likes=lks)

            elif stream == 'progm':
                lks = progm.objects.filter(video_id=video_id).first()
                if likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).exists():
                    lks = lks.likes - 1
                    likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).delete()
                else:
                    lks = lks.likes + 1
                    save_like = likes(video_id=video_id, userid=user_id, username=user_name)
                    save_like.save()  
                progm.objects.filter(video_id=video_id).update(likes=lks)

            elif stream == 'boards':
                lks = boards.objects.filter(video_id=video_id).first()
                if likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).exists():
                    lks = lks.likes - 1
                    likes.objects.filter(video_id=video_id, userid=user_id, username=user_name).delete()
                else:
                    lks = lks.likes + 1 
                    save_like = likes(video_id=video_id, userid=user_id, username=user_name)
                    save_like.save() 
                boards.objects.filter(video_id=video_id).update(likes=lks)

            else:
                lks=0   
            return JsonResponse(json.dumps({'liked_value': lks}), safe=False)             
        else:
            return redirect('/')    
    else:
            return redirect('/')    


def loadComments(request):

    if request.method == 'GET':
        video_id = request.GET.get('comment_id')

        allComments = comment.objects.filter(video_id = video_id)
        return JsonResponse({"comments" : list(allComments.values())})
    else:
        return redirect('/')
    

