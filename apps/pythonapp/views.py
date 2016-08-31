from django.shortcuts import render,redirect, HttpResponse
from ..loginapp.models import Userlog
from django.contrib import messages 
from .models import Pokes
from django.db.models import Count, Sum
import bcrypt
def poke(request):
	user_id = Userlog.objects.get(id=request.session['user'])
	userpoked_id = Userlog.objects.get(id=request.POST['userpoked'])
	poke_check = Pokes.objects.filter(user=user_id, userpoked=userpoked_id)
	if not poke_check:
		Pokes.objects.create(user=user_id, userpoked=userpoked_id, poked=1)
		print poke_check
		return redirect('/pokes')
	else:
		poke_check[0].poked += 1
		poke_check[0].save()
		return redirect('/pokes')
