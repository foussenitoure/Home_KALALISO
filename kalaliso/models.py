from django.db import models

# Create your models here.
# !/usr/bin/python
#  -*- coding: latin-1 -*-

# reload(sys)
# sys.setdefaultencoding('utf-8')
# import os, sys

from imp import reload
from django.db.models import FloatField
# from django.utils.encoding import python_2_unicode_compatible
from functools import update_wrapper
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.base import ModelBase
from django.views.decorators.cache import never_cache
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import utc
from django.db.models import Avg
import psycopg2
import datetime
import sys

class Person(models.Model):

    STATUS = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),)

    status = models.CharField(max_length=20, choices=STATUS, default='CLIENT')

    SEX = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),
    )
    sex = models.CharField(max_length=20, choices=SEX, default='Homme')
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    contact_1 = models.IntegerField()
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return'{}{}'.format(self.prenom, self.nom)

class Mesure(models.Model):
    person = models.OneToOneField('Person', on_delete=models.DO_NOTHING, verbose_name='Nom client',)
    coude = models.FloatField()
    epaule = models.FloatField()
    manche = models.FloatField(null=True, blank=True)
    tour_manche = models.FloatField(null=True, blank=True)
    taille = models.FloatField(null=True, blank=True)
    poitrine = models.FloatField(null=True, blank=True)
    longueur_boubou = models.FloatField(null=True, blank=True)
    longueur_patanlon = models.FloatField(null=True, blank=True)
    fesse = models.FloatField(null=True, blank=True)
    ceinture = models.FloatField(null=True, blank=True)
    cuisse = models.FloatField(null=True, blank=True)
    patte = models.FloatField(null=True, blank=True)

    def __str__(self):
        return'{}'.format(self.person)

class Produit(models.Model):
    MODELE = (
        ('Boubou', 'Boubou'),
        ('Grand Boubou', 'Grand Boubou'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Complet', 'Pagne Complet'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),
        ('AUTRES', 'AUTRES'),
    )
    modele = models.CharField(max_length=25, choices=MODELE, default='Boubou')
    def __str__(self):
            return'{}'.format(self.modele,)


class Commande(models.Model):
    COUTURE = (
        ('BRODERIE', 'Broderie'),
        ('COUTURE SIMPLE', 'Couture simple'),
        ('COUTURE A MAIN', 'Couture a main'),
        ('REPARATION', 'Reparation'),
    )
    couture = models.CharField(max_length=25, choices=COUTURE, default='Broderie')
    TISSU = (
        ('BAZIN GETZNER', 'BAZIN GETZNER'),
        ('BAZIN RICHE', 'BAZIN RICHE'),
        ('BAZIN MOYEN', 'BAZIN MOYEN'),
        ('WAX', 'WAX'),
        ('TISSU', 'TISSU'),
        ('LEGER', 'LEGER'),
        ('BRODE', 'BRODE'),
        ('PERCALE', 'PERCALE'),
        ('VOILE', 'VOILE'),
        ('BOGOLAN', 'BOGOLAN'),
        ('AUTRES', 'AUTRES'),
    )
    tissu = models.CharField(max_length=25, choices=TISSU, default='BAZIN GETZNER')
    COULOIR = (
        ('BLANCHE', 'BLANCHE'),
        ('ROUGE SANG', 'ROUGE SANG'),
        ('BLEU', 'BLEU'),
        ('ORANGE', 'ORANGE'),
        ('ROSE', 'ROSE'),
        ('VERT', 'VERT'),
        ('GRIS', 'GRIS'),
        ('GRIS CLAIR', 'GRIS CLAIR'),
        ('VIOLET', 'VIOLET'),
        ('MARON', 'MARON'),
        ('MARON CLAIR', 'MARON CLAIR'),
        ('TURGUOISE', 'TURGUOISE'),
        ('JAUNE', 'JAUNE'),
        ('JAUNE COUSIN', 'JAUNE COUSIN'),
        ('NOIR', 'NOIR'),
        ('BAGA', 'BAGA'),
        ('BAGA CLAIR', 'BAGA CLAIR'),
        ('DEUX TONS', 'DEUX TONS'),
        ('MULTICOLOR', 'MULTICOLOR'),
    )

    couloir = models.CharField(max_length=25, choices=COULOIR, default='BLANCHE')
    command_person = models.ForeignKey('Person',  on_delete=models.CASCADE, verbose_name='Titulaire command',)
    produit = models.ManyToManyField('Produit', verbose_name='Nouveau produit',)
    quantite = models.PositiveSmallIntegerField()
    metrage = models.FloatField()
    prix_unitaire = models.FloatField()
    montant_total = models.FloatField()
    avance = models.FloatField()
    reliquat = models.FloatField()
    remise = models.FloatField(default=0)
    reception = models.DateTimeField(auto_now_add=True)
    rendez_vous = models.DateField()
    livre = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
          ordering = ('reception',)

    # les champs supplementaires des données à caractère personnelle.


    # created_at = models.DateField(auto_now_add=True)

    # image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True, verbose_name= 'Profil')

    #CATEGORIE = (
    #     ('G', 'Grande'),
    #     ('M', 'Moyenne'),
    #     ('P', 'Petite'),
    # )
    # categorie = models.CharField(max_length=20, choices=CATEGORIE, default='Grande')

    # domicile = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    # alias = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    # profession = models.CharField(max_length=30, null=True, blank=True)
    # contact_2 = models.CharField(max_length=20, null=True, blank=True)
    # date_naissance = models.DateField()
    # nationalite = models.CharField(max_length=30, null=True, blank=True)
    # tutuelle = models.CharField(max_length=30, null=True, blank=True)
    # telephonique_fix = models.CharField(max_length=30, null=True, blank=True)
    # numero_reference = models.PositiveIntegerField(null=True, blank=True)
    # nina = models.PositiveIntegerField(null=True, blank=True)

# @python_2_unicode_compatible

#
# # @python_2_unicode_compatible




# Table pour toutes les depenses effectuées dans l'entreprise
# @python_2_unicode_compatible
# class Depense(models.Model):
#         MODE_DEPENSE = (
#             ('MATERIELS', 'Materiels'),
#             ('FRAIS OUVRIER','Frais_Ouvrier'),
#             ('BON', 'Bon'),
#             ('LOCATION', 'Location'),
#             ('ELECTRICITE', 'Electricite'),
#             ('CONSOMMABLE', 'Consommable'),
#             ('IMPOT SYNTHETIQUE', 'Impot_synthetique'),
#             ('TAXE MUNICIPAL', 'Taxe_municipal'),
#
#         )
#
#         mode_depense = models.CharField(max_length=30, choices=MODE_DEPENSE, default='Materiels',)
#         # categorie_depense = models.BooleanField(default=False)
#         titulaire_depense = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire Depense',)
#         # acquisiteur = models.ForeignKey('Programme', on_delete=models.CASCADE, verbose_name='Payement hebdomaiare',)
#         quantite = models.PositiveSmallIntegerField(default=1)
#         prix_unitaire = models.PositiveIntegerField()
#         montant = models.PositiveIntegerField()
#         justificatif = models.TextField(max_length=200, null=True, blank=True)
#         is_valide = models.BooleanField(default=False)
#         created_at = models.DateTimeField(auto_now_add=True)
#
#         def __str__(self):
#             return '{}'.format(self.mode_depense)


# class Programme(models.Model):
#     TYPE_COUTURE = (
#         ('BRODERIE', 'Broderie'),
#         ('COUTURE SIMPLE', 'Couture simple'),
#         ('COUTURE A MAIN', 'Couture a main'),
#         ('REPARATION', 'Reparation'),
#     )
#     type_couture = models.CharField(max_length=30, choices=TYPE_COUTURE, default='Broderie', )
#     TYPE_MACHINE = (
#         ('20U', '20U'),
#         ('CORNER', 'Corner'),
#         ('PIQUASE', 'Piquase'),
#         ('GROS PETIT', 'Gros petit'),
#         ('GROS FIL', 'Gros fil'),
#         ('SARABA', 'Saraba'),
#     )
#
#     type_machine = models.CharField(max_length=30, choices=TYPE_MACHINE, default='20U',)
#     prix_ouvrier = models.PositiveIntegerField()
#     ouvrier = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Ouvrier', )
#     proprietaire = models.ForeignKey('Commande', on_delete=models.CASCADE, verbose_name='proprietaire de commande', )
#     produit = models.ManyToManyField('Produit', verbose_name='liste des produits')
#     affecter = models.BooleanField(default=False)

    # categorie_depense = models.BooleanField(default=False)
    # quantite = models.PositiveSmallIntegerField(default=1)
    # montant = models.PositiveIntegerField()
    # justificatif = models.TextField(max_length=200, null=True, blank=True)
    # is_valide = models.BooleanField(default=False)

    # def __str__(self):
    #     return '{}{}{}'.format(self.ouvrier, self.proprietaire, self.proprietaire)

# Creation d'une nouvelle table de vente des habilles pour la boutique de kalaliso !

# @python_2_unicode_compatible
# class Vente(models.Model):
#         photo_modele = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
#         client = models.ForeignKey('Person', on_delete=models.CASCADE)
#         type_modele = models.ManyToManyField('Produit')
#         vente = models.ForeignKey('Commande', on_delete=models.CASCADE)
#         montant = models.DecimalField(max_digits=10, decimal_places=2)
#         satisfact = models.BooleanField(default=True)
#         commentaire = models.TextField(max_length=100, null=True, blank=True)
#         created_at = models.DateTimeField(auto_now_add=True)
#
#         def __str__(self):
#             return '{} {}'.format(self.photo_modele, self.montant,)


# @python_2_unicode_compatible
# class DivisionAdministrativeMali(models.Model):
#         codereg = models.PositiveIntegerField()
#         region = models.CharField(max_length=100)
#         codecer = models.PositiveIntegerField()
#         cercle = models.CharField(max_length=100)
#         codearr = models.PositiveIntegerField()
#         arrondissement = models.CharField(max_length=100)
#         codecom = models.PositiveIntegerField()
#         commune = models.CharField(max_length=100)
#         codec = models.PositiveIntegerField()
#         village = models.CharField(max_length=100)
#         long = models.IntegerField()
#         lat = models.PositiveIntegerField()
#         divisionadministrative = models.CharField(max_length=100)
#         nombrelocal = models.PositiveIntegerField()
#         prhomme = models.PositiveIntegerField()
#         prfemme = models.PositiveIntegerField()
#         prtotal = models.PositiveIntegerField()
#         nbredemeanges = models.PositiveIntegerField()
#         nbredeconcess = models.PositiveIntegerField()
#         tm = models.PositiveIntegerField()
#         rm = models.PositiveIntegerField()
#         persparlocalite = models.PositiveIntegerField()
#         menparconcess = models.PositiveIntegerField()
#         persparmenages = models.PositiveIntegerField()
#
#         def __str__(self):
#             return '{} {} {}'.format(self.region, self.cercle, self.commune,)


# @python_2_unicode_compatible
# class User(models.Model):
#  username = models.CharField(max_length=200, )
#  password = models.CharField(max_length=100, )
#  email = models.EmailField()
#
#  def __str__(self):
#      return '{}'.format(self.username)
#
# @python_2_unicode_compatible
# class UserProfileInfo(models.Model):
#  user = models.OneToOneField(User, on_delete=models.CASCADE)
#  portfolio_site = models.URLField(blank=True)
#  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
#
#  def __str__(self):
#      return '{}'.format(self.user,)




# @python_2_unicode_compatible
# class Cercle(models.Model):
#         codecer = models.PositiveIntegerField()
#         cercle = models.CharField(max_length=100)
#
#         def __str__(self):
#            return '{}'.format(self.name,)
#
#
# @python_2_unicode_compatible
# class Commune(models.Model):
#         codecom = models.PositiveIntegerField()
#         commune = models.CharField(max_length=100)
#
#         def __str__(self):
#             return '{}'.format(self.name, )


# @python_2_unicode_compatible
# class Arrondissement(models.Model):
#         codearr = models.PositiveIntegerField()
#         arrondissement = models.CharField(max_length=100)
#
#         def __str__(self):
#             return '{}'.format(self.name, )

# @python_2_unicode_compatible
# class Longitude(models.Model):
#         longitude = models.PointField()
#
#         def __str__(self):
#             return '{}'.format(self.longitude, )
