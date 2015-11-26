# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from myweb.models import UserProfile, Team, Plan
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import Count
import datetime
from django import forms

class ImgForm(forms.Form):
    img = forms.ImageField()

@login_required
def main(request):
    username = request.session.get('username', '')
    userid = request.session.get('userid', '')
    plans = Plan.objects.filter(start_time__gte=datetime.date.today())
    userprofiles = UserProfile.objects.annotate(num_teams=Count('master')).order_by('-num_teams')
    if plans.count()>5: plans = plans[:5]
    if userprofiles.count()>5: userprofiles[:5]

    content = {'username':username, "userid":userid, 'plans':plans, 'userprofiles':userprofiles}
    return render(request, "main.html", content)

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
                        request.session['userid'] = user.id
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
def showProfile(request, UID):
    current_time = datetime.date.today()
    username = request.session.get('username', '')
    userid = UID
    user = User.objects.get(id=userid)
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

    content = {"username":username, "userid":userid, "user":user, "userprofile":userprofile,
                "used_plans":used_plans, "using_plans":using_plans}
    return render(request, "profile.html", content)

@login_required
def editProfile(request):
    current_time = datetime.date.today()
    username = request.session.get('username', '')
    userid = request.session.get('userid', '')
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
  #  teams = chain(Team.objects.filter(master=userprofile), Team.objects.filter(participant=userprofile)).distinct()
    teams = Team.objects.filter(master=userprofile) | Team.objects.filter(participant=userprofile)
    teams.distinct()
    used_plans = []
    using_plans = []
    for team in teams:
        p = team.plan
        if p.start_time < current_time:
            used_plans.append(p)
        else:
            using_plans.append(p)

    age = current_time.year-userprofile.birthday.year

    if request.POST:
        userprofile.sex = request.POST.get('new_sex', '')
        userprofile.location = request.POST.get('new_location', '')
        userprofile.birthday = request.POST.get('new_birthday', '9999-12-31')
        if request.FILES:
            userprofile.avatar = request.FILES['img']
        userprofile.save()
        return HttpResponseRedirect('/showProfile/'+str(userid))


    content = {"username":username, "userid":userid, "user":user, "userprofile":userprofile,\
                "used_plans":used_plans, "using_plans":using_plans, "age":age}
    return render(request, "edit_profile.html", content)

@login_required
def addPlan(request):
    status = ''
    username = request.session.get('username', '')
    userid = request.session.get('userid', '')
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    if request.POST:
        post = request.POST
        newplan = Plan(title=post.get('title', ''),\
                    description=post.get('description', ''),\
                    starting=post.get('starting', ''),\
                    destination=post.get('destination', ''),\
                    total_person=post.get('total_person', ''),\
                    start_time=post.get('start_time', ''),\
                    end_time=post.get('end_time', ''))
        newplan.save()
        newteam = Team(master=userprofile, plan=newplan)
        newteam.save()
#        newteam.participant.add(userprofile)
        status = "success"
    content = {"status":status, "username":username, "userid":userid}
    return render(request, "add_plan.html", content)

@login_required
def showPlan(request, ID):
    username = request.session.get('username', '')
    userid = request.session.get('userid', '')
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    plan = Plan.objects.get(id=ID)
    team = Team.objects.get(plan=plan)
    travelers = team.participant
    mastername = team.master.user.username
    if mastername==username or userprofile in team.participant.all():
        disable = True
    else:
        disable = False
    current_person = travelers.count() + 1
########untested#############
    status = ''
    if request.POST:
        if current_person<plan.total_person:
            status = 'too_many'
        status = 'success'
        team.participant.add(userprofile)
        current_person = travelers.count() + 1
#############################
    content = {"username":username, "userid":userid, "plan":plan, \
            "current_person":current_person, "disable":disable, \
            "status":status}
    return render(request, "plan.html", content)

@login_required
def showTeam(request, ID):
    username = request.session.get('username', '')
    userid = request.session.get('userid', '')
    plan = Plan.objects.get(id=ID)
    team = Team.objects.get(plan=plan)
    travelers = team.participant.all()
    master = team.master.user
    print travelers
    content = {"username":username, "userid":userid, "master":master,\
            "travelers":travelers, "plantitle":plan.title, "teamid":team.id}
    return render(request, "team.html", content)

@login_required
def kick(request, TID, UID):
    team = Team.objects.get(id=TID)
    kicked_person = UserProfile.objects.get(id=UID)
    team.participant.remove(kicked_person)
    return HttpResponseRedirect('/showTeam/'+str(team.plan.id))