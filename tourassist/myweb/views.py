# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from myweb.models import UserProfile, Team, Plan
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from itertools import chain
import datetime

@login_required
def main(request):
    username = request.session.get('username', '')
    return render(request, "main.html", {'username':username})

@login_required
def userLogout(request):
    auth.logout(request)
    return HttpResponseRedirect("/loginAndRegister/")#

 
def loginAndRegister(request):
    if request.session.get('username', ''):
        return HttpResponseRedirect('/')
    status = ''
    username = ''
    if request.POST:
        post = request.POST
        if request.POST.has_key("register"):
            password =  post['new_password']
            repassword = post['new_repassword']
            if password!=repassword:
                status = "re_err"
            else:
                if User.objects.filter(username=post['new_username']):
                    status = 'user_exist'
                else:
                    newuser = User.objects.create_user(username=post['new_username'],\
                                                        password=post['new_password'],\
                                                        email=post['new_email'])           
                    newuser.save()
                    profile = UserProfile(user=newuser,\
                                        sex=post.get('new_sex', ''),\
                                        location=post.get('new_location', ''),\
                                        birthday=post.get('new_birthday', ''))
                    profile.save()
                    status = 'success'
        elif request.POST.has_key("login"):
            username = post['username']
            password = post['password']
            if User.objects.filter(username=username):
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        request.session['username'] = username
                        return HttpResponseRedirect('/')
                    else:
                        status = 'not_active'
                else:
                    status = 'pwd_err'
            else:
                status = 'not_exist'
    content = {'status':status}
    return render(request, 'sign_in.html', content)

@login_required
def showProfile(request):
    current_time = datetime.date.today()
    username = request.session.get('username', '')
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    teams = chain(Team.objects.filter(master=userprofile), Team.objects.filter(participant=userprofile))
    used_plans = []
    using_plans = []
    print userprofile.sex
    print type(userprofile.sex)
    for team in teams:
        p = team.plan
        if p.start_time<current_time:
            used_plans.append(p)
        else:
            using_plans.append(p)

    age =current_time.year-userprofile.birthday.year

    content = {"username":username, "user":user, "userprofile":userprofile,
                "used_plans":used_plans, "using_plans":using_plans, "age":age}
    return render(request, "profile.html", content)

@login_required
def editProfile(request):
    current_time = datetime.date.today()
    username = request.session.get('username', '')
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    teams = chain(Team.objects.filter(master=userprofile), Team.objects.filter(participant=userprofile))
    used_plans = []
    using_plans = []
    for team in teams:
        p = team.plan
        if p.start_time<current_time:
            used_plans.append(p)
        else:
            using_plans.append(p)

    age =current_time.year-userprofile.birthday.year

    if request.POST:
        userprofile.sex = request.POST.get('new_sex', '')
        userprofile.location = request.POST.get('new_location', '')
        userprofile.birthday = request.POST.get('new_birthday', '9999-12-31')
        print userprofile.birthday
        userprofile.save()
        return HttpResponseRedirect('/showProfile/')


    content = {"username":username, "user":user, "userprofile":userprofile,
                "used_plans":used_plans, "using_plans":using_plans, "age":age}
    return render(request, "edit_profile.html", content)