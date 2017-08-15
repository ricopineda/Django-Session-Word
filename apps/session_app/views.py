# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
	if not 'list' in request.session:
		request.session['list'] = []
	return render(request,'session_app/index.html')


def process(request):

	request.session['list'] += [{
		"word": request.POST['word'],
		"color": request.POST['color'],
		"font": request.POST['font'],
		"time": strftime("%Y-%m-%d %I:%M %p", gmtime())

	}]	
	
	return redirect('/')



	# if request.method == "POST":
	# 	context = {
	# 		"word" : "request.POST['word']",
	# 		"red" : "request.POST['red']",
	# 		"green" : "request.POST['green']",
	# 		"blue" : "request.POST['']",
	# 		"font" : "request.POST['font']"
	# 	}
	# 	print request.POST