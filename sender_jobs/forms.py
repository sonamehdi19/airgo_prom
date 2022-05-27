from django import forms
from .models import CarrierJobs, SenderJobs


class SenderForm(forms.ModelForm):
    location=forms.CharField(max_length=200, required=True)
    destination=forms.CharField(required=True)
    due_date=forms.DateField(required=True)
    contact_number=forms.CharField(required=True)
    add_image=forms.ImageField()
    additional_note=forms.CharField()

    class Meta:
        model=SenderJobs
        fields=['location', 'destination', 'due_date','contact_number',
'add_image','additional_note'] 


class CarrierForm(forms.ModelForm):
    location=forms.CharField(max_length=200, required=True)
    departure_date=forms.DateField(required=True)
    destination=forms.CharField(max_length=200, required=True)
    arrival_date=forms.DateField(required=True)
    contact_number=forms.CharField(required=True)
    additional_note=forms.CharField()

    class Meta:
        model=CarrierJobs
        fields=['location', 'departure_date', 'destination','arrival_date',
'contact_number','additional_note'] 
