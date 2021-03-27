from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'us_firstname', 
            'us_lastname', 
            'us_email', 
            'us_number',
            'us_birthday',
            'us_status',
            'us_city',
            "us_password",
        )


class PharmacieSerializer(ModelSerializer):
    class Meta:
        model= Pharmacie
        fields= (
            'id',
            'pha_name',
            'pha_email',
            'pha_number',
            'pha_location',
            'pha_status',
            'pha_garde'
        )

class PharmacieAllInfoSerializer(ModelSerializer):
    class Meta:
        model= Pharmacie
        fields=(
            'pha_name',
            'pha_email',
            'pha_number',
            'pha_location',
            'pha_status',
            'pha_garde'
        )


class HospitalSerializer(ModelSerializer):
    class Meta:
        model= Hospital
        fields= (
            'hos_name',
            'hos_email',
            'hos_number',
            'hos_location',
            'hos_password',
            'user'
        )

class MedicamentSerializer(ModelSerializer):
    class Meta:
        model= Medicament
        fields= '__all__'

class OrdonnanceSerializer(ModelSerializer):
    class Meta:
        model= Ordonnance
        fields= (
            'medicament',
            'user',
            "hospital",
            'ord_date',
            'ord_status'
        )