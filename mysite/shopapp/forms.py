from django import forms


from .models import Product
from django.contrib.auth.models import Group

from django import forms

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=1000000, decimal_places=2)
#     description = forms.CharField(
#         label="Product description",
#         widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}),
#         validators=[validators.RegexValidator(r'^[a-z0-9\s]+$',message='Only lowercase letters and numbers are allowed.')],
#         )

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "name", "price", "description", "discount", "preview"
    
#     images = forms.ImageField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}),

#     )



class ProductForm(forms.ModelForm):
    images = MultipleFileField(required=False)  # Используйте MultipleFileField для загрузки нескольких файлов

    class Meta:
        model = Product
        fields = ["name", "price", "description", "discount", "preview", "images"]



class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name",) 
    