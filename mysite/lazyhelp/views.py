# -*-coding:utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import template
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