from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
#from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
#from weasyprint import HTML, CSS
from django.conf import settings
import os
from clientes.models import Cliente
from productos.models import Producto
from .models import Egreso, ProductosEgreso
from .forms import AnadirClienteForm, EditarClienteForm, AnadirProductoForm, EditarProductoForm




def index(request):
    return render(request, 'portada.html')

#Clientes Vistas #######################################
def clientesv(request):
    clients = Cliente.objects.all()
    formulariocv = AnadirClienteForm()
    formularioev = EditarClienteForm()
    context ={
        'Cli':clients, 
        'formcv':formulariocv,
        'formev':formularioev,
    }
    return render(request, 'clientest.html', context)

def anadircv(request):
    if request.POST:
        formulariocv = AnadirClienteForm(request.POST, request.FILES)
        if formulariocv.is_valid():
            try:
                formulariocv.save()
            except:
                messages(request, "Error al guardar los datos del cliente")                
                return redirect(clientesv) 
    return redirect(clientesv) 

def editarcv(request):
    if request.POST:
       clients = Cliente.objects.get(pk=request.POST.get("id_personal_editar"))
       formularioev = EditarClienteForm(request.POST, request.FILES, instance=clients)
       if formularioev.is_valid():
            try:
              formularioev.save()
            except:
                messages(request, "Error al guardar los datos del cliente")                
                return redirect(clientesv) 
    return redirect(clientesv)  

def borrarcv(request):
    if request.POST:
        clients=Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        clients.delete()
    return redirect(clientesv) 

#Productos Vistas #######################################
def productosv(request):
    products = Producto.objects.all()
    formularioapv = AnadirProductoForm()
    formularioepv = EditarProductoForm()
    context ={
        'Pro':products, 
        'formapv':formularioapv,
        'formepv':formularioepv,
    }
    return render(request, 'productest.html', context)

def anadirpv(request):
    if request.POST:
        formularioapv = AnadirProductoForm(request.POST, request.FILES)
        if formularioapv.is_valid():
            try:
                formularioapv.save()
            except:
                messages(request, "Error al guardar los datos del producto")                
                return redirect(productosv) 
    return redirect(productosv) 

def editarpv(request):
    if request.POST:
       products = Producto.objects.get(pk=request.POST.get("id_producto_editar"))
       formularioepv = EditarProductoForm(request.POST, request.FILES, instance=products)
       if formularioepv.is_valid():
            try:
              formularioepv.save()
            except:
                messages(request, "Error al guardar los datos del producto")                
                return redirect(productosv) 
    return redirect(productosv)  

def borrarpv(request):
    if request.POST:
        products=Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        products.delete()
    return redirect(productosv) 

#POS Vistas #######################################

class add_ventas(ListView):
    template_name = 'add_ventas.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos_lista"] = Producto.objects.all()
        context["clientes_lista"] = Cliente.objects.all()

        return context

def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta = Egreso.objects.get(pk=float(id))
    datos = ProductosEgreso.objects.filter(egreso=venta)
    for i in datos:
        subtotal = subtotal + float(i.subtotal)
        iva_suma = iva_suma + float(i.iva)

    empresa = "Genericos de Farmacia C.A."
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta.fecha_pedido,
        'cliente': venta.cliente.nombre,
        'items': datos, 
        'total': venta.total, 
        'empresa': empresa,
        'comentarios': venta.comentarios,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
    }
    html_template = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; ticket.pdf"
    #css_url = os.path.join(settings.BASE_DIR,'index\static\index\css/bootstrap.min.css')
    #HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])
   
    #font_config = FontConfiguration()
    #HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(target=response, font_config=font_config,stylesheets=[CSS(css_url)])

    return response










