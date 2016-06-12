# -*-coding:utf8 -*-
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.sessions.models import Session
from models import User
import json
def here(request):
	return HttpResponse("幹FQQQQ！")
def index(request):
	return render_to_response('bootstrap_index.html',locals())
def ad(request):
	return render_to_response('bootstrap_advertisement.html',locals())
def center(request):
	return render_to_response('bootstrap_center.html',locals())
def deal(request):
	return render_to_response('bootstrap_deal.html',locals())
def deal_build(request):
	return render_to_response('bootstrap_deal_build.html',locals())
def deal_map(request):
	return render_to_response('bootstrap_deal_map.html',locals())
def dispute(request):
	return render_to_response('bootstrap_dispute.html',locals())
def center(request):
	return render_to_response('bootstrap_center.html',locals())

def login(request):

	if 'user' in request.session:
		print(request.session['user'])
		return HttpResponseRedirect('/index')

	if request.POST:
		account = request.POST['account']
		password = request.POST['password']
		user = User.objects.filter(account = account)
		if len(user)>0:
			if password == user[0].password:
				request.session['user'] = user[0].uid
				return HttpResponseRedirect('/index')
			else:
				return render_to_response('bootstrap_login.html',RequestContext(request, locals()))
		else:
			user = User.objects.filter(mail = account)
			if len(user)>0:
				if password == user[0].password:
					request.session['user'] = user[0].uid
					return HttpResponseRedirect('/index')
			else:
				return render_to_response('bootstrap_login.html',RequestContext(request, locals()))
	
	else:
		return render_to_response('bootstrap_login.html',RequestContext(request, locals()))

def logout(request):
	del request.session['user']
	return HttpResponseRedirect('/index')


def register(request):
	
	if request.POST:
		account = request.POST.get('mobile','')
		password = request.POST.get('password','')
		email = request.POST.get('mail','')
		uname = request.POST.get('uname','')
		u1 = User(uname = uname, account = account, mail = email, password = password, point=0)
		print(u1)
		u1.save()
		return HttpResponseRedirect('/index')
	else:
		return render_to_response('bootstrap_signup.html',RequestContext(request, locals()))