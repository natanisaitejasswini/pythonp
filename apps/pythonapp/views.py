from django.shortcuts import render,redirect, HttpResponse
from ..loginapp.models import Userlog
from django.core.urlresolvers import reverse
from django.contrib import messages 
from .models import Pokes
from django.db.models import F
import bcrypt
def poke(request, id):
	if request.method == "POST":
		try: 
			user1 = Userlog.objects.get( user1 = request.session['user'])
			user2 = Userlog.objects.get( user2 = id)
			if user1 and user2:
				Pokes.objects.get( user = user1[0], userpoked=user2[0])[0].update( poked = F('poked') + 1 )
				user1.save()
				user2.save()
				return redirect('/pokes')
		except:
			Pokes.objects.create(user = Userlog.objects.get(id=request.session['user']), userpoked = Userlog.objects.get( id = id))
			return redirect('/pokes')
	else:
		return HttpResponse('error')

def check(request):
	user = Userlog.objects.get(id = request.session['user'])
	return redirect('/pokes')
