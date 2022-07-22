from django import forms
from .models import GOAL22
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class GOAL22Q1Form(forms.ModelForm):

    class Meta():
        model = GOAL22
        fields = ('GOAL22A1','GOAL22AP','GOAL22B1','GOAL22BP','GOAL22C1','GOAL22CP','GOAL22D1','GOAL22DP','GOAL22E1','GOAL22EP','GOAL22F1','GOAL22FP','GOAL22G1','GOAL22GP')
        labels = {'GOAL22A1':"meta1",'GOAL22B1':"meta2",'GOAL22C1':"meta3",'GOAL22D1':"meta4",'GOAL22E1':"meta5",'GOAL22F1':"meta6",'GOAL22G1':"meta7",'GOAL22AP':"peso% de meta1",'GOAL22BP':"peso% de meta2",'GOAL22CP':"peso% de meta3",'GOAL22DP':"peso% de meta4",'GOAL22EP':"peso% de meta5",'GOAL22FP':"peso de meta6",'GOAL22GP':"peso% de meta7"}

class GOAL22Q2Form(forms.ModelForm):

    class Meta():
        model = GOAL22
        fields = ('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2')
        labels = {'GOAL22A2':"meta1",'GOAL22B2':"meta2",'GOAL22C2':"meta3",'GOAL22D2':"meta4",'GOAL22E2':"meta5",'GOAL22F2':"meta6",'GOAL22G2':"meta7"}
        
class GOAL22Q3Form(forms.ModelForm):

    class Meta():
        model = GOAL22
        fields = ('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3')
        labels = {'GOAL22A3':"meta1",'GOAL22B3':"meta2",'GOAL22C3':"meta3",'GOAL22D3':"meta4",'GOAL22E3':"meta5",'GOAL22F3':"meta6",'GOAL22G3':"meta7"}
        