from django.shortcuts import render

def painel_atleta(request):
    return render(request, "gestao_treinos/painel_atleta.html")
