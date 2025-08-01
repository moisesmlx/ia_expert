from django.shortcuts import render, HttpResponse
from ia_expert import expert_em_cifras
from time import sleep
import os
import expert.settings
from random import randint, choice


# Create your views here.
n_cifra = ''
original = ''
mudado = ''
textarea = '' 
cifra_pronta = expert.settings.MEDIA_ROOT
decode_cifra = ''


def index(request):
    global n_cifra, original, mudado, textarea, cifra_pronta, decode_cifra
    if request.method == 'POST':
        n_cifra = request.POST.get('nome')
        original = request.POST.get('original') 
        textarea = request.POST.get('textarea') 
        mudado = request.POST.get('new')
        
        if original != '' and mudado.upper() == 'AUTO':
            return cifra(request)
        
        elif original != '' and mudado != '':
            return cifra_unidade(request)
        
        if original != 'A' or original != 'A#' or original != 'B'\
            or original != 'C' or original != 'C#' or original != 'D' or original != 'D#'\
            or original != 'E' or original != 'F' or original != 'F#' or original != 'G'\
            or original != 'G#'\
            or original != 'Am' or original != 'A#m' or original != 'Bm'\
            or original != 'Cm' or original != 'C#m' or original != 'Dm' or original != 'D#m'\
            or original != 'Em' or original != 'Fm' or original != 'F#m' or original != 'Gm'\
            or original != 'G#m':
            return render(request, 'info/info.html')
    
    else:
        return render(request, 'main/index.html')


def cifra(request):
    global n_cifra, original, mudado, textarea, cifra_pronta, decode_cifra
    
    if original != '' or original == 'A' or original == 'A#' or original == 'B'\
        or original == 'C' or original == 'C#' or original == 'D' or original == 'D#'\
        or original == 'E' or original == 'F' or original == 'F#' or original == 'G'\
        or original == 'G#'\
        or original == 'Am' or original == 'A#m' or original == 'Bm'\
        or original == 'Cm' or original == 'C#m' or original == 'Dm' or original == 'D#m'\
        or original == 'Em' or original == 'Fm' or original == 'F#m' or original == 'Gm'\
        or original == 'G#m' and mudado.upper() == 'A':
        
        alfa = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        code = f'{choice(alfa)}{randint(0, 100)}'
        code = f'{randint(0, 100)}{choice(alfa)}'
        code = f'{choice(alfa)}{randint(0, 100)}'
            
        decode_cifra = f'{str(code)}{str(code)}{str(code)}_'
    
    expert_em_cifras.translate_auto(original, mudado,n_cifra,textarea, decode_cifra)
    n_cifra = ''
    original = ''
    mudado = ''
    textarea = '' 
    cifra_pronta = expert.settings.MEDIA_ROOT
    decode_cifra = ''
    return render(request, 'info/cifra.html', {'n_cifra': n_cifra, 'textarea': textarea})

def cifra_unidade(request):
    global n_cifra, original, mudado, textarea, cifra_pronta, decode_cifra
    if original != '' and mudado != '' or original == 'A' or original == 'A#' or original == 'B'\
        or original == 'C' or original == 'C#' or original == 'D' or original == 'D#'\
        or original == 'E' or original == 'F' or original == 'F#' or original == 'G'\
        or original == 'G#'\
        or original == 'Am' or original == 'A#m' or original == 'Bm'\
        or original == 'Cm' or original == 'C#m' or original == 'Dm' or original == 'D#m'\
        or original == 'Em' or original == 'Fm' or original == 'F#m' or original == 'Gm'\
        or original == 'G#m'\
        or mudado != '' and mudado == 'A' or mudado == 'A#' or mudado == 'B'\
        or mudado == 'C' or mudado == 'C#' or mudado == 'D' or mudado == 'D#'\
        or mudado == 'E' or mudado == 'F' or mudado == 'F#' or mudado == 'G'\
        or mudado == 'G#'\
        or mudado == 'Am' or mudado == 'A#m' or mudado == 'Bm'\
        or mudado == 'Cm' or mudado == 'C#m' or mudado == 'Dm' or mudado == 'D#m'\
        or mudado == 'Em' or mudado == 'Fm' or mudado == 'F#m' or mudado == 'Gm'\
        or mudado == 'G#m':
            
        alfa = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        code1 = f'{choice(alfa)}{randint(0, 100)}'
        code2 = f'{randint(0, 100)}{choice(alfa)}'
        code3 = f'{choice(alfa)}{randint(0, 100)}'
            
        decode_cifra = f'{str(code1)}{str(code2)}{str(code3)}_'
    
    expert_em_cifras.translate(original, mudado,n_cifra,textarea, decode_cifra)
    n_cifra = ''
    original = ''
    mudado = ''
    textarea = '' 
    cifra_pronta = expert.settings.MEDIA_ROOT
    decode_cifra = ''
    return render(request, 'info/cifra_unidade.html', {'n_cifra': n_cifra, 'textarea': textarea})

def info(request):
    return render(request, 'info/info.html')

def download(request):
    return render(request, 'info/cifra.html')
        