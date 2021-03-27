from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import *
from rest_framework import permissions
from django.http import Http404
from api.models import User,Pharmacie,Hospital,Medicament,Ordonnance
# from api.permission import IsOwner

# Create your views here.

class PharmacieList(ListCreateAPIView):

    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer
    # permissions=(permissions.IsAuthenticated)
    
    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
      
 
class PharmacieDetailViews(RetrieveUpdateDestroyAPIView):

    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer
    # permissions=(permissions.IsAuthenticated,IsOwner,)
    
    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class UserListViews(ListCreateAPIView):
   
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permissions=(permissions.IsAuthenticated)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class UserDetailViews(RetrieveUpdateDestroyAPIView):
   
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permissions=(permissions.IsAuthenticated,IsOwner,)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class HospitalListViews(ListCreateAPIView):
    
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    # permissions=(permissions.IsAuthenticated)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class HospitalDetailViews(RetrieveUpdateDestroyAPIView):
    
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    # permissions=(permissions.IsAuthenticated,IsOwner,)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class MedicamentListviews(ListCreateAPIView):

    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    # permissions=(permissions.IsAuthenticated)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class MedicamentDetailviews(RetrieveUpdateDestroyAPIView):

    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    # permissions=(permissions.IsAuthenticated,IsOwner,)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class OrdonnanceListViews(ListCreateAPIView):

    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer
    # permissions=(permissions.IsAuthenticated)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

class OrdonnanceDetailViews(RetrieveUpdateDestroyAPIView):

    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer
    # permissions=(permissions.IsAuthenticated,IsOwner,)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
        