from django.db import models


class User(models.Model):
    AVAILABLE = 'available',
    UNAVAILABLE = 'unavailable',
    STATUS = [
        ('available', ('Disponible')),
        ('unavailable', ('Indisponible'))
    ]

    us_id = models.IntegerField()
    us_firstnamee = models.CharField(verbose_name="Nom ", max_length=50)
    us_lastname = models.CharField(verbose_name="Prenom ", max_length=50)
    us_email = models.EmailField(verbose_name="Email ")
    us_phone_number = models.CharField(verbose_name="Telephone ", max_length=16)
    us_birth_date = models.DateField(verbose_name="Date de naissance")
    us_password = models.CharField(verbose_name="Mot de passe ", max_length=32)
    us_status = models.CharField(verbose_name="Statut ", max_length=32, choices=STATUS, default=AVAILABLE)
    us_city = models.CharField(verbose_name="Localité ", max_length=30)


    def __str__(self):
        return ('{} {}', self.us_firstnamee, self.us_lastname)


class Hospital(models.Model):

    hos_id = models.IntegerField()
    hos_name = models.CharField(verbose_name="Nom de l'Hôpital ", max_length=100)
    hos_email = models.EmailField(verbose_name="Email ")
    hos_phone_number = models.CharField(verbose_name="Telephone ", max_length=16)
    hos_cell_number = models.CharField(verbose_name="Cellulaire ", max_length=16)
    hos_location = models.CharField(verbose_name="Localisation ", max_length=60)
    hos_password = models.CharField(verbose_name="Password ", max_length=32)
    hos_description = models.TextField(verbose_name="Description ", max_length=255)

    def __str__(self):
        return self.hos_name;


class Pharmacy(models.Model):
    AVAILABLE = 'available',
    UNAVAILABLE = 'unavailable'

    STATUS = [
        ('available', 'Pas de garde'),
        ('unavailable', 'De garde')
    ]

    pha_id = models.IntegerField()
    pha_name = models.CharField(verbose_name="Nom de la Pharmacie ", max_length=100)
    pha_email = models.EmailField(verbose_name="Email ")
    pha_phone_number = models.CharField(verbose_name="Telephone ", max_length=16)
    pha_cell_number = models.CharField(verbose_name="Cellulaire ", max_length=16)
    pha_location = models.CharField(verbose_name="Localisation ", max_length=100)
    pha_password = models.CharField(verbose_name="Mot de passe ", max_length=32)
    pha_description = models.TextField(verbose_name="Description :", max_length=255)
    pha_status = models.CharField(verbose_name="Statut ", max_length=32, choices=STATUS, default=AVAILABLE)

    def __str__(self):
        return self.pha_name
