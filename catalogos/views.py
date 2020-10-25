from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from catalogos.models import Categoria,SubCategoria, Producto
from catalogos.forms import CategoriaFroms, SubCategoriaFroms, ProductoForms
from generales.views import SinPrivilegios

from django.http import HttpResponse
# Create your views here.


class CategoriaView(LoginRequiredMixin, generic.ListView, SinPrivilegios):
    permission_required = "catalogos.view_categoria"
    model = Categoria
    template_name = "catalogos/categoria_list.html"
    context_object_name = "obj"
    #form_class = CategoriaFroms
    #success_url = reverse_lazy("catalogos:categoria_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso

class CategoriaNew(SuccessMessageMixin,LoginRequiredMixin,PermissionRequiredMixin, generic.CreateView):
    permission_required = "catalogos.add_categoria"
    model=Categoria
    template_name = "catalogos/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaFroms
    success_url = reverse_lazy("catalogos:categoria_list") #redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Categoria Creada Satisfactoriamente"

class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView, SinPrivilegios):
    permission_required = "catalogos.change_categoria"
    model = Categoria
    template_name = "catalogos/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaFroms
    success_url = reverse_lazy("catalogos:categoria_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Categoria Editada Satisfactoriamente"

class CategoriaDel(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView,SinPrivilegios):
    permission_required = "catalogos.delete_categoria"
    model = Categoria
    template_name = "catalogos/Catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:categoria_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    #login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Categoria Eliminada Satisfactoriamente"

class SubCategoriaView(LoginRequiredMixin, generic.ListView, SinPrivilegios):
    permission_required = "catalogos.view_subcategoria"
    model = SubCategoria
    template_name = "catalogos/subcategoria_list.html"
    context_object_name = "obj"
    #form_class = CategoriaFroms
    #success_url = reverse_lazy("catalogos:categoria_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso

class SubCategoriaNew(SuccessMessageMixin,LoginRequiredMixin,PermissionRequiredMixin, generic.CreateView):
    permission_required = "catalogos.add_subcategoria"
    model=SubCategoria
    template_name = "catalogos/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaFroms
    success_url = reverse_lazy("catalogos:subcategoria_list") #redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Sub Categoria Creada Satisfactoriamente"

class SubCategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView, SinPrivilegios):
    permission_required = "catalogos.change_subcategoria"
    model = SubCategoria
    template_name = "catalogos/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaFroms
    success_url = reverse_lazy("catalogos:subcategoria_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Sub Categoria Editada Satisfactoriamente"


class SubCategoriaDel(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView,SinPrivilegios):
    permission_required = "catalogos.delete_subcategoria"
    model = SubCategoria
    template_name = "catalogos/Subcatalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:subcategoria_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    #login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Sub Categoria Eliminada Satisfactoriamente"

class ProductoView(LoginRequiredMixin, generic.ListView, SinPrivilegios):
    permission_required = "catalogos.view_producto"
    model = Producto
    template_name = "catalogos/producto_list.html"
    context_object_name = "obj"
    #form_class = CategoriaFroms
    #success_url = reverse_lazy("catalogos:categoria_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso

class ProductoNew(SuccessMessageMixin,LoginRequiredMixin,PermissionRequiredMixin, generic.CreateView):
    permission_required = "catalogos.add_producto"
    model=Producto
    template_name = "catalogos/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForms
    success_url = reverse_lazy("catalogos:producto_list") #redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Producto Creado Satisfacotriamente"

class ProductoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView, SinPrivilegios):
    permission_required = "catalogos.change_producto"
    model = Producto
    template_name = "catalogos/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForms
    success_url = reverse_lazy("catalogos:producto_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Producto Editado Satisfactoriamente"

class ProductoDel(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView,SinPrivilegios):
    permission_required = "catalogos.delete_producto"
    model = Producto
    template_name = "catalogos/Producto_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:producto_list")  # redireccion a la ruta una vez se ejecute la insercion del registro
    #login_url = 'generales:login'       #sin credenciales de acceso
    success_message = "Producto Eliminado Satisfactoriamente"


def categoria_print(self, pk=None):
    from io import BytesIO
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter


    response = HttpResponse(content_type='application/pdf')
    buff= BytesIO()
    doc=SimpleDocTemplate(buff, pagesize=letter, righMargin=40,leftMargin=40,topMargin=60,bottomMargin=18,)

    categorias=[]
    styles=getSampleStyleSheet()
    header=Paragraph("Listado de Categorias", styles['Heading1'])
    categorias.append(header)
    headings=('Id','Descripcion','Activo','Creacion')
    if not pk:
        registros=[ (p.id, p.descripcion,p.activo, p.creado)
                   for p in Categoria.objects.all().order_by('pk')
                   ]
    else:
        registros = [ (p.id, p.descripcion, p.activo, p.creado)
                     for p in Categoria.objects.filter(id=pk).order_by('pk')
                     ]
    t = Table([headings]+registros)
    t.setStyle(TableStyle([
        ('GRID',(0,0),(3,-1),1,colors.dodgerblue),
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
        ('BACKGROUND', (0, 0), (-1, 0),  colors.dodgerblue),
    ]))

    categorias.append(t)
    doc.build(categorias)
    response.write(buff.getvalue())
    buff.close()
    return response


