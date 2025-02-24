from django import forms
from .models import Property, Client, Agent

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms', 'is_available','mage']
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']
        
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'email', 'phone']