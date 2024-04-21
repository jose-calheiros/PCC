from unittest import loader
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

  
def register(request):
 
 if request.method == "GET":
  return render(request, 'registration/register.html')
 else:
   nome = request.POST.get('username')
   email = request.POST.get('email')
   senha = request.POST.get('password')

   user = User.objects.filter(email=email).first()

   if user: 
    raise ValidationError('Este endereço de e-mail já está em uso.')
    
   user = User.objects.create_user(username=nome, email=email, password=senha)
   user.save()

 return redirect('/accounts/login')
