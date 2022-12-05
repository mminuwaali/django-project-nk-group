from . import models
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Contact
        
        
class SubscribeForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Subscribe
