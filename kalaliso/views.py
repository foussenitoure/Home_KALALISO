from django.shortcuts import render
# from .models import Person
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from kalaliso.models import Person
# Mesure
# from kalaliso.form import PersonForm
# MesureForm


# Create your views here.

# def loop(request):
#     template = loader.get_template('folders_html/index.html')
#     return HttpResponse(template.render({}, request))

def look(request):
    return render(request, 'folders_html/home.html')

def indexpage(request):
    return render(request, 'folders_html/index.html')

# def newPage(request):
#
#     sta  = request.POST.get("radio1")
#     pre  = request.POST.get("prenom1")
#     no   = request.POST.get("nom1")
#     se   = request.POST.get("radio")
#     cont = request.POST.get("Contact")
#
#     data = Person(status=sta, prenom=pre, nom=no, sex=se, contact_1=cont)
#     data.save()
#     return HttpResponse(request, {})


def command_client(request):
    return render(request, 'folders_html/command.html')


def mesure_client(request):
    return render(request, 'folders_html/mesure.html')

def thanks(request):
    return HttpResponse('Thanks, your form has been processed')

def get_form_data(request):
    if request.method == 'POST':

            sta  = request.POST.get("status")
            se   = request.POST.get("sex")
            pre  = request.POST.get("prenom")
            no   = request.POST.get("nom")
            cont = request.POST.get("contact_1")
            ema = request.POST.get("email")

            data = Person(status=sta, prenom=pre, nom=no, sex=se, contact_1=cont, email=ema)
            data.save()

       # if form.is_valid():
       #       sta = form.cleaned_data['status']
       #       se = form.cleaned_data['sex']
       #       pre = form.cleaned_data["prenom"]
       #       pre = form.cleaned_data["prenom"]
       #       no = form.cleaned_data["nom"]
       #       cont = form.cleaned_data["contact_1"]
       #       ema = form.cleaned_data["email"]

    #         return HttpResponseRedirect(reverse('thanks'))
    # else:
    #    form = PersonForm()
    # return render(request, '../templates/form.html', {'form':form})

def list_person(request):
     model = Person
     list_p = Person.objects.all()

# context = {'year': year, 'article_list': a_list}
     return render(request, '../templates/list_person.html')


# def merci(request):
#     return HttpResponse('Thanks, your messure had well added')
#
# def mesure_data(request):
#     if request.method == 'POST':
#             coud  = request.POST.get("coude")
#             epau   = request.POST.get("epaule")
#             ma = request.POST.get("manche")
#             to_ma   = request.POST.get("tour_manche")
#             tail   = request.POST.get("taille")
#             poitr = request.POST.get("pointrine")
#             lo_bo = request.POST.get("longueur_boubou")
#             lo_pa = request.POST.get("longueur_patanlon")
#             fes = request.POST.get("fesse")
#             cei = request.POST.get("ceinture")
#             cui = request.POST.get("cuisse")
#             pat = request.POST.get("patte")
#
#
#             data = Mesure(coude=coud, epaule=epau, manche=ma,
#                           tour_manche=to_ma, taille=tail,
#                           poitrine=poitr, longueur_boubou=lo_bo,
#                           longueur_patanlon=lo_pa, fesse=fes,
#                           ceinture=cei, cuisse=cui, patte=pat,)
#             data.save()
#             return HttpResponseRedirect(reverse('merci'))
#     else:
#        form = MesureForm()
#     return render(request, 'folders_html/mesur.html', {'form':form})

