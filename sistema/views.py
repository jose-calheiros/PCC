from unittest import loader
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required, user_passes_test
from sistema.form import ExperimentoForm
from sistema.models import Experimento
from django.template import loader



#FUNÇÃO DE ADICIONAR
@login_required
def add(request):
    if request.user.tipo == 'aluno':
        return HttpResponse("Apenas professores podem acessar esta página.")
    else:
        if request.method == 'POST':
            form = ExperimentoForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/sistema/')
            else:
                return render(request, "add.html", {'form': form})
        else:
            form = ExperimentoForm()
            return render(request, "add.html", {'form': form})



#FUNÇÃO DE LER
@login_required
def read (request):
 
    tudo = Experimento.objects.all()  
    template = loader.get_template("lista.html")  
    return HttpResponse(template.render({'experimentos': tudo}, request))  


#FUNÇÃO UPDATE
@login_required
def update(request, experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
    if request.user.tipo == 'aluno':
        return HttpResponse("Apenas professores podem acessar esta página.")
    else:
        if request.method == 'POST':
            form = ExperimentoForm(request.POST, instance=experimento)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/sistema/')
            else:
                return render(request, "update.html", {'form': form, 'id': experimento_id})
        else:
            form = ExperimentoForm(instance=experimento)
            return render(request, "update.html", {'form': form, 'id': experimento_id})


#FUNCÇOES DE DELETAR
@login_required
def delete(request, experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
    if request.user.tipo == 'aluno':
        return HttpResponse("Apenas professores podem acessar esta página.")
    else:
        experimento.delete()
        return HttpResponseRedirect('/sistema/')


@login_required
def confdelete(request,  experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
    if request.user.tipo == 'aluno':
        return HttpResponse("Apenas professores podem acessar esta página.")
    else:
        return render(request, "delete.html", {'experimento': experimento})
