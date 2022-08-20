from pdb import post_mortem
from django import forms
from polls.models import Bienvenue

class EmailForm(forms.ModelForm):
    mail = forms.EmailField(required=True, max_length=254)
    class Meta:
        model = Bienvenue
        fields=('mail',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mail'].widget.attrs['placeholder'] = 'Email' 
        self.fields['mail'].widget.attrs['class'] = 'form-control' 
        

    
           

       
        