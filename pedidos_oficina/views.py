from django.shortcuts import render

def renderizandoReact(request):                                                             #essa funcao eh responsavel por renderizar o index.html base no react
    return render(request, 'index.html')
