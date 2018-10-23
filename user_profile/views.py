from django import forms
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from .classification import classify
from .models import zonal_tweets
# Create your views here.
def login_view(request):
	
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		return redirect('/')
	return render(request,"login.html",{"form":form})

def home_page_view(request):
	data_dict = classify()
	for data in data_dict:
		z = zonal_tweets(tag=data,tweet=data_dict[data])
		z.save()
	return render(request,"home.html")

def feedback_1(request):
	queryset = zonal_tweets.objects.filter(tag='NR')
	context = {
		"title"		  : "Northern Railway",
		"object_list" : queryset
	}
	return render(request,"f1.html",context)

def feedback_2(request):
	return render(request,"f1.html")

def feedback_3(request):
	return render(request,"feedback-3.html")

def feedback_4(request):
	return render(request,"feedback-4.html")

def feedback_5(request):
	return render(request,"feedback-5.html")

def feedback_6(request):
	return render(request,"feedback-6.html")

def feedback_7(request):
	return render(request,"feedback-7.html")

def feedback_8(request):
	return render(request,"feedback-8.html")

def feedback_9(request):
	return render(request,"feedback-9.html")

def feedback_10(request):
	return render(request,"feedback-10.html")

def feedback_11(request):
	return render(request,"feedback-11.html")

def feedback_12(request):
	return render(request,"feedback-12.html")

def feedback_13(request):
	return render(request,"feedback-13.html")

def feedback_14(request):
	return render(request,"feedback-14.html")

def feedback_15(request):
	return render(request,"feedback-15.html")

def feedback_16(request):
	return render(request,"feedback-16.html")


def feedback_a(request):
	return render(request,"feedback-a.html")

def feedback_b(request):
	return render(request,"feedback-b.html")

def feedback_c(request):
	return render(request,"feedback-c.html")

def feedback_d(request):
	return render(request,"feedback-d.html")

def feedback_e(request):
	return render(request,"feedback-e.html")

def feedback_f(request):
	return render(request,"feedback-f.html")

def feedback_g(request):
	return render(request,"feedback-g.html")

def feedback_h(request):
	return render(request,"feedback-h.html")

def feedback_i(request):
	return render(request,"feedback-i.html")

def feedback_j(request):
	return render(request,"feedback-j.html")

def feedback_k(request):
	return render(request,"feedback-k.html")

def feedback_l(request):
	return render(request,"feedback-l.html")