from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
            'query': 'Query',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-warning rounded-0" 
