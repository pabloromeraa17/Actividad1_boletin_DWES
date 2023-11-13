from django.shortcuts import render
from .forms import Formulario1
# Create your views here.
def index(request):
    valido = None
    if request.method == 'POST':
        form = Formulario1(request.POST)
        if form.is_valid():
            valido = "Valido el FORMULARIO"
    else:
        form = Formulario1()
    return render(request, 'index.html', {
        'form': form, 'valido': valido
    })