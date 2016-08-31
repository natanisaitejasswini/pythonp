from django.shortcuts import render,redirect, HttpResponse
from .models import Userlog
from ..pythonapp.models import Pokes
from django.contrib import messages
from datetime import datetime
import bcrypt
from django.db.models import Count, Sum

def index(request):
	return render(request,'loginapp/index.html')
def success(request):
	context = {
		'user_ses': Userlog.objects.get(id=request.session['user']),
		'yours': Pokes.objects.filter(user=request.session['user']).order_by('-poked'),
		'other_pokes': Userlog.objects.exclude(id=request.session['user']).annotate(counter=Sum("user2__poked")),
		'total': Pokes.objects.filter(user=request.session['user'])
	}
	print context['total']
 	return render(request,'pythonapp/success.html',context)
def user(request):
	errors = False
	check1 = Userlog.UserManager.first_name(request.POST['name'])
	check2 = Userlog.UserManager.user_name(request.POST['alias'])
	check3 = Userlog.UserManager.password(request.POST['password'])
	check3_char = Userlog.UserManager.password_charcheck(request.POST['password'])
	print request.POST['password'] 
	print bcrypt.gensalt()  
	check4 = Userlog.UserManager.confirm_password(request.POST['password'],request.POST['confirm_password'])
	check5 = Userlog.UserManager.birthday(request.POST['birthday'])
	check6 = Userlog.UserManager.reg_email(request.POST['email'])
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid name", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Invalid username", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid password", extra_tags="regtag")
		print check4[1]
		errors = True
	if check3_char[0] == False:
		messages.add_message(request, messages.INFO, "Invalid characters in password", extra_tags="regtag")
		errors = True
	if check4[0] == False:
		messages.add_message(request, messages.INFO, "Please confirm your password correctly", extra_tags="regtag")
		errors = True
	if check5[0] == False:
		messages.add_message(request, messages.INFO, "Please give birthday correctly", extra_tags="regtag")
		errors = True	
	if check6[0] == False:
		messages.add_message(request, messages.INFO, "Please provide email correctly", extra_tags="regtag")
		errors = True	    
	if Userlog.objects.filter(email = request.POST['email']):
	    messages.add_message(request, messages.INFO, "This username already existed!", extra_tags="regtag")
	# Errors Route
	if errors == True:
		return redirect('/main')
	elif (check1[0] == True & check2[0] == True  & check3[0] == True & check5[0] == True & check6[0] == True):
		user = Userlog.UserManager.create(name=check1[1], alias=check2[1], password=check3[1], birthday=check5[1], email=check6[1])
		request.session['user'] = user.id
		print 
		return redirect('/pokes')

def login(request):
	check7 = Userlog.UserManager.log(request.POST['email'], request.POST['password'])
	if check7[0] == False:
		messages.add_message(request, messages.INFO, check7[1], extra_tags='logtag')
		return redirect('/main')
	else:
		request.session['user'] = check7[1].id
		return redirect('/pokes')

def logout(request):
	try:
		request.session.clear()
	except:
		pass
	return redirect('/main')







