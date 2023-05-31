from django import forms
from .models import Career
from .models import ContactNumber


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['points_headline_1'].widget.attrs.update({'style': 'background-color:#04d0603a;'})
        self.fields['points_headline_2'].widget.attrs.update({'style': 'background-color:#04d0603a;'})
        self.fields['points_headline_3'].widget.attrs.update({'style': 'background-color:#04d0603a;'})
      




class ContactNumberAdminForm(forms.ModelForm):
    number = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'ex.+91 0000 0000'}))
    footernumber = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'ex.+91 0000 0000'}))

   

    class Meta:
        model = ContactNumber
        fields = '__all__'


