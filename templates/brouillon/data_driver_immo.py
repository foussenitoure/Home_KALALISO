from django.db import models

# Create your models here.


# ===============     MODELISATION DATABASE DRIVER    ============

# class Person(models.Model):
#     STATUS = (
#             ('Customer', 'CUSTOMER'),
#             ('Proprietaire', 'PROPRIETAIRE'),
#             ('Driver', 'DRIVER'),
#
#     status        = models.CharField(max_length=50, choices=STATUS, default='CUSTOMER')
#     First_name    = models.CharField(max_length=100, blank=True, null=True)
#     Last_name     = models.CharField(max_length=100, blank=True, null=True)
#     numero        = models.IntegerField()
#     url           = models.URLField()
#     photo         = models.ImageField(upload_to=static/img_person)
#     email         = models.EmailField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return

# class Course(models.Model):
#     customer      = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Nom Client',)
#     price         = models.IntegerField()
#     remise        = models.IntegerField()
#     total         = models.IntegerField()
#     start_course  = models.TimeField(auto_now_add=True)
#     end_course    = models.models.TimeField(auto_now_add=True)
#     during        = models.DurationField(aut)
#
#     def __str__(self):
#         return

# class Moto(models.Model):
#     driver        = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Chauffeur',)
#     proprietaire  = models.ManyToManyField('Person')
#     photo         = models.ImageField(upload_to=static/img_moto)
#     type          = models.CharField(max_length=100, blank=True, null=True)
#     disponible    = models.BooleanField(default=True)
#     marque        = models.CharField(max_length=100, blank=True, null=True)
#     numero_chasis = models.IntegerField()

#     def __str__(self):
#         return


# ===============     MODELISATION DATABASE IMMOBILIERE    ============