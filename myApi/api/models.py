from django.db import models

# Create your models here.
class User(models.Model) :
    us_firstname = models.CharField(max_length=50)
    us_lastname = models.CharField(max_length=50)
    us_email = models.EmailField(max_length=50)
    us_number = models.IntegerField()
    us_birthday = models.DateField()
    us_password = models.CharField(max_length=50)
    us_status = models.CharField(max_length=50)
    us_city = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.us_firstname)

class Pharmacie(models.Model):
    pha_name = models.CharField(max_length=50)
    pha_email = models.CharField(max_length=50)
    pha_number = models.IntegerField()
    pha_location = models.CharField(max_length=50)
    pha_password= models.CharField(max_length=50)
    pha_status= models.CharField(max_length=50)
    pha_garde= models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.pha_name)

class Commande(models.Model):
    pharmacie= models.ForeignKey(Pharmacie,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    com_date= models.DateField()
    com_status=models.CharField(max_length=50)


class Hospital(models.Model):
    hos_name = models.CharField(max_length=50)
    hos_email = models.EmailField()
    hos_number = models.IntegerField()
    hos_location= models.CharField(max_length=50)
    hos_password= models.CharField(max_length=50)
    user = models.ManyToManyField(User,related_name='hospital', through='Rdv')

    def __str__(self):
        return "{0}".format(self.hos_name)

class Rdv(models.Model):
    hospital= models.ForeignKey(Hospital,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    rdv_date= models.DateField()
    rdv_status=models.CharField(max_length=50)


class Medicament(models.Model):
    med_nom = models.CharField(max_length=50)

    def __str__(self):
        return self.med_nom


class Ordonnance(models.Model):
    ord_date= models.DateField()
    ord_status= models.CharField(max_length=50)
    hospital = models.OneToOneField(Hospital,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    medicament = models.ManyToManyField(Medicament,related_name='ordonnance', blank=True,db_table='constitue')


    def __str__(self):
        return "{0}".format(self.ord_date)

