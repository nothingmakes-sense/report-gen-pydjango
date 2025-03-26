from django import forms
from .models import Patient, Provider, User

class PatientForm(forms.ModelForm):  # Corrected to ModelForm
    class Meta:
        model = Patient
        fields = ['name', 'id_number', 'med_number', 'dob', 'service', 'support_plan', 'provider']
class ProviderForm(forms.ModelForm):  # Corrected to ModelForm
    class Meta:
        model = Provider
        fields = '__all__'

class CreateUserForm(forms.ModelForm):  # Corrected to ModelForm
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser']

class ReportGenerationForm(forms.Form):
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.Select(attrs={'class': 'select2'})
    )
    provider = forms.ModelChoiceField(
        queryset=Provider.objects.all(),
        widget=forms.Select(attrs={'class': 'select2'})
        
    )
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date cannot be after end date.")
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("Start time must be before end time.")
        return cleaned_data