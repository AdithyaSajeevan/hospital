
from django import forms
from .models import Doctor,Patient




class PatientForm(forms.ModelForm):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    DOCTOR_CHOICES = [('Dr.Aparna', 'Dr.Aparna'), ('Dr.Archana', 'Dr.Archana'), ('Dr.Amal', 'Dr.Amal')]
   

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    disease = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    doctor = forms.ChoiceField(choices=DOCTOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
   
    class Meta:
        model = Patient
        fields = ['name', 'age', 'mobile', 'gender', 'disease', 'doctor']

class DocForms(forms.ModelForm):
    dr_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    specialisation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Doctor
        fields = ['dr_name', 'specialisation','image' ]
    