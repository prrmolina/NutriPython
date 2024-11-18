from django.shortcuts import render, redirect
from .forms import PratoForm
from .models import Prato
from .forms import CadastroForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import IMCForm
from .models import IMC
from django.contrib.auth.decorators import login_required


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


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['senha'])
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')  # Redirecionar para a página inicial ou outra
    else:
        form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})



@login_required
def calcular_imc(request):
    if request.method == 'POST':
        form = IMCForm(request.POST)
        if form.is_valid():
            peso = form.cleaned_data['peso']
            altura = form.cleaned_data['altura']
            imc = peso / (altura ** 2)
            peso_ideal_min = 18.5 * (altura ** 2)
            peso_ideal_max = 24.9 * (altura ** 2)

            # Salvar no banco de dados
            imc_record = IMC(
                usuario=request.user,
                peso=peso,
                altura=altura,
                imc=imc,
                peso_ideal_min=peso_ideal_min,
                peso_ideal_max=peso_ideal_max
            )
            imc_record.save()

            return render(request, 'imc_app/calcular_imc.html', {
                'form': form,
                'resultado': f'Seu IMC é: {imc:.2f} - Peso ideal: entre {peso_ideal_min:.2f} kg e {peso_ideal_max:.2f} kg.'
            })
    else:
        form = IMCForm()

    return render(request, 'imc_app/calcular_imc.html', {'form': form})