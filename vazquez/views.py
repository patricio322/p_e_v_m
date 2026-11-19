from django.shortcuts import render

def inicio (request):
    return render (request, "vazquez/inicio.html")

def registro (request) :
    return render (request, "vazquez/formregistro.html")