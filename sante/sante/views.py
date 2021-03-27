from sante.forms import UserProfileForm, HospitalProfileForm, PharmacyProfileForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def welcome(request):
    return HttpResponse('<html><body>Bievenu sur E-santé</body></html>')

def home(request):
    return render(request, 'base.html')

def register(request):
    if len(request.GET )> 0 and 'profileType' in request.GET:
        userForm = UserProfileForm(prefix="us")
        hospitalForm = HospitalProfileForm(prefix="hos")
        pharmacyForm = PharmacyProfileForm(prefix="pha")

        if request.GET['profileType'] == 'user':
            userForm = UserProfileForm(request.GET, prefix="us")
            if userForm.is_valid():
                userForm.save()
                return redirect('/login')
        elif request.GET['profileType'] == 'hospital':
            hospitalForm = HospitalProfileForm(request.GET, prefix="hos")
            if hospitalForm.is_valid():
                hospitalForm.save()
                return redirect('/login')
        elif request.GET['profileType'] == 'pharmacy':
            pharmacyForm = PharmacyProfileForm(request.GET, prefix="pha")
            if pharmacyForm.is_valid():
                pharmacyForm.save()
                return redirect('/login')
        return render(request, 'register.html', {'userForm': userForm,
                                                 'hospitalForm': hospitalForm,
                                                 'pharmacyForm': pharmacyForm})
    else:
        userForm = UserProfileForm(prefix="us")
        hospitalForm = HospitalProfileForm(prefix="hos")
        pharmacyForm = PharmacyProfileForm(prefix="pha")
        return render(request, 'register.html', {'userForm': userForm,
                                                 'hospitalForm': hospitalForm,
                                                 'pharmacyForm': pharmacyForm})
