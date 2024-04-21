from unittest import loader
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from sistema.form import ExperimentoForm
from sistema.models import Experimento
from django.template import loader

@login_required
def read (request):
 
    tudo = Experimento.objects.all()  
    template = loader.get_template("lista.html")  
    return HttpResponse(template.render({'experimentos': tudo}, request))  
    
@login_required
def add (request):
    if request.method == 'POST':
        print("Cadastrado")
        form = ExperimentoForm(request.POST)
        form.save()
        return HttpResponseRedirect('/sistema/')
    else:
        form = ExperimentoForm()
    return render(request, "add.html", {'form': form})

@login_required
def delete(request, experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
    experimento.delete()
    return HttpResponseRedirect('/sistema/')

@login_required
def confdelete(request, experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
    return render(request, "delete.html", {'experimento': experimento})


@login_required
def update(request, experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)

    if request.method == 'POST':
        form = ExperimentoForm(request.POST, instance=experimento)
        form.save()
        return HttpResponseRedirect('/sistema/')
    else:
        form = ExperimentoForm(instance=experimento)
        
    return render(request, "update.html", {'form': form, 'id': experimento_id})
