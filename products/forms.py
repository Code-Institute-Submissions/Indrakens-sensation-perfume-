from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Brand, Genders


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        genders = Genders.objects.all()
        
        brand_friendly_names = [(b.id, b.get_brand_friendly_name()) for b in brands]
        gender_friendly_names = [(g.id, g.get_gender_friendly_name()) for g in genders]

        self.fields["brand"].choices = brand_friendly_names
        self.fields["gender"].choices = gender_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-warning rounded-0"   
