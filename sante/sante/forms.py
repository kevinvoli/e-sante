from django import forms

from sante.models import User, Pharmacy, Hospital

class UserProfileForm(forms.ModelForm):
    class Meta :
        model = User
        exclude = ('us_id', )


class HospitalProfileForm(forms.ModelForm):
    class Meta :
        model = Hospital
        exclude = ('hos_id', )

class PharmacyProfileForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        exclude = ('pha_id', )