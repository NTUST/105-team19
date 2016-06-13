# -*-coding:utf8 -*-
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.sessions.models import Session
from models import User, Order
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
	if request.POST:

		saler = User.objects.get(uid = request.session['user'])
		title = request.POST.get('title','')
		context = request.POST.get('context','')
		cash = request.POST.get('cash','')
		deadline = request.POST.get('deadline','')
		address = request.POST.get('address','')
		o1 = Order(title = title, detail = context, address = address, price = cash,
				deadline = deadline, saler = saler, buyer = saler, pic1 = None,
				point_to_s = 0, point_to_b = 0, status = 0)
		o1.save()
		resp = {'res':'alert("建立成功");window.location.assign("/index");'}
		return render_to_response('bootstrap_deal_build.html',RequestContext(request, resp))

	else:
		return render_to_response('bootstrap_deal_build.html',RequestContext(request, locals()))
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
				resp = {'res':'alert("登錄成功");window.location.assign("/index");'}
				return render_to_response('bootstrap_login.html',RequestContext(request, resp))
			else:
				resp = {'res':'alert("帳號或密碼錯誤")'}
				return render_to_response('bootstrap_login.html',RequestContext(request, resp))
		else:
			user = User.objects.filter(mail = account)
			if len(user)>0:
				if password == user[0].password:
					request.session['user'] = user[0].uid
					resp = {'res':'alert("登錄成功");window.location.assign("/index");'}
					return render_to_response('bootstrap_login.html',RequestContext(request, resp))
			else:
				resp = {'res':'alert("帳號或密碼錯誤")'}
				return render_to_response('bootstrap_login.html',RequestContext(request, resp))
	
	else:
		return render_to_response('bootstrap_login.html',RequestContext(request, locals()))

def logout(request):
	del request.session['user']
	return HttpResponseRedirect('/login')


def register(request):
	
	if request.POST:
		account = request.POST.get('mobile','')
		password = request.POST.get('password','')
		email = request.POST.get('mail','')
		uname = request.POST.get('uname','')
		u1 = User(uname = uname, account = account, mail = email, password = password, point=0)
		print(u1)
		u1.save()
		resp = {'res':'alert("註冊成功，請使用手機或信箱登入");window.location.assign("/login");'}
		return render_to_response('bootstrap_signup.html',RequestContext(request, resp))
	else:
		return render_to_response('bootstrap_signup.html',RequestContext(request, locals()))