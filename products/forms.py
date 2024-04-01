from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Genders


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
        gender = Genders.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        gender_names = [(g.id, g.get_friendly_name()) for g in gender]

        self.fields["category"].choices = friendly_names
        self.fields["gender"].choices = gender_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-warning rounded-0"   
