from django import forms
from catalogos.models import Categoria, SubCategoria, Producto

class CategoriaFroms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion','activo']
        labels = {'descripcion': "Descriocion de la Categoria",
                  'activo': "Estado"}
        widgets = {'descripcion': forms.TextInput()}
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class SubCategoriaFroms(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(activo= True).order_by('descripcion')
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion','activo']
        labels = { 'categoria': "Categoria",'descripcion': "Descriocion de la Categoria",'activo': "Estado"}
        widgets = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoría"

class ProductoForms(forms.ModelForm):
    subcategoria = forms.ModelChoiceField(
        queryset = SubCategoria.objects.filter(activo=True).order_by('categoria__descripcion','descripcion'),
        empty_label="Seleccione Sub Categoria"
    )
    class Meta:
        model= Producto
        fields = '__all__' #INDICA QUE SE USARAN TODOS LOS CAMPOS DISPONIBLES DEL FORMULARIO Y NO UNA LISTA

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
