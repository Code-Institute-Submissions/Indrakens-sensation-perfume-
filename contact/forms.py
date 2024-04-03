from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
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
        for field_name, fields in self.fields.items():
            fields.widget.attrs["class"] = "border-warning rounded-0" 
