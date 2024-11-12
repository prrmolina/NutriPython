from django.shortcuts import render, redirect
from .forms import PratoForm
from .models import Prato

def cadastrar_prato(request):
    if request.method == 'POST':
        form = PratoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_prato')
    else:
        form = PratoForm()

    # Buscar todos os pratos cadastrados
    pratos = Prato.objects.all()
    return render(request, 'cadastrar_prato.html', {'form': form, 'pratos': pratos})