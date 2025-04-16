from django.shortcuts import render
from .models import Client,Chambre #
def liste_clients(request):
    clients = Client.objects.all() #
    return render(request,'clients.html',{'clients': clients}) #
def liste_chambre(request):
    chambre = Chambre.objects.all() #
    return render(request,'chambre/liste_chambre.html',{'chambre': chambre}) #
def ajouter_chambre(request):
    if request.method == 'POST' :
        form = chambreFrom(resquest.POST)
    if form.is_valid():
        form.save() #
        return redirect('liste_chambre') #
    else:
        form = ChambreForm()
        return render(request, 'chambre/ajouter_chambre.html',{'form':form})
def modifier_chambre(request, pk):
    chambre = get_objet_or_404(chambre, pk=pk)
    if request.method == 'POST':
        form = Chambreform(request.POST,instance=chambre)
    if form.is_valid():
      form.save()
      return redirect('detail_chambre',pk=chambre.pk)
    else:
        form = Chambreform(instance=chambre)
        return render(request,'chambre/modifier_chambre.html',{'form:form'})
def supprimer_chambre(request, pk):
    chambre = get_object_or_404(chambre,pk)
    if request.method == 'POST':
        Chambre.delete() #
        return redirect('liste_chambre') #
    return render(request,'chambre/supprimer_chambre.html',{'chambre':chambre})

def mon_formulaire(request):
    return render(request,'gestChambre/formulaire.html')



      

# Create your views here.













