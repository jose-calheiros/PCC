from django.shortcuts import render, redirect
from .forms import UsuarioForms


def register(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioForms()
    return render(request, 'registration/register.html', {'form': form})
