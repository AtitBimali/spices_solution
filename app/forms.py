from django import forms
from . import models

class IndustryBaseForm(forms.ModelForm): #creating custom Form to pass attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control d-inline-flex flex-row align-items-center'
            visible.field.widget.attrs['placeholder'] = 'Enter Your Industry Type'
            
class CompanyBaseForm(forms.ModelForm): #creating custom Form to pass attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-group d-inline-flex flex-row align-items-center'

class Industry(IndustryBaseForm):
    class Meta:
        model=models.Industry
        fields=['industry_type',]

class Company(CompanyBaseForm):
    class Meta:
        model=models.Company
        fields=['company_name','owner_name','address','email','contact','industry_type']

