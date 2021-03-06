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
# from django.contrib.gis.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import utc
from django.db.models import Avg
import psycopg2
import datetime
import sys

class Person(models.Model):
    # image = models.ImageField(upload_to='photos/profil%Y/%m/%d', null=True, blank=True, verbose_name='Photo_commande')
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
    CATEGORIE = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),
    )
    sex              = models.CharField(max_length=20, choices=SEX, default='Homme')
    prenom           = models.CharField(max_length=30, null=True, blank=True)
    nom              = models.CharField(max_length=30, null=True, blank=True)
    contact_1        = models.IntegerField(primary_key=True)
    email            = models.EmailField(max_length=100, null=True, blank=True)
    categorie        = models.CharField(max_length=20, choices=CATEGORIE, default='Grande')
    domicile         = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    alias            = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    profession       = models.CharField(max_length=30, null=True, blank=True)
    contact_2        = models.CharField(max_length=20, null=True, blank=True)
    date_naissance   = models.DateField(auto_now_add=True)
    nationalite      = models.CharField(max_length=30, null=True, blank=True)
    tutuelle         = models.CharField(max_length=30, null=True, blank=True)
    telephonique_fix = models.CharField(max_length=30, null=True, blank=True)
    numero_reference = models.PositiveIntegerField(null=True, blank=True)
    nina             = models.PositiveIntegerField(null=True, blank=True)
    # create_at        =  models.DateTimeField(auto_now_add=True)
    # update_at        = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return'{} {} {}'.format(self.prenom, self.nom, self.contact_1)


class Mesure(models.Model):
    MESURE_MODELE  = (
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
        ('Tenu Securite', 'Tenu Securite'),)

    mesure_modele   = models.CharField(max_length=50, primary_key=True, choices=MESURE_MODELE, default='Boubou')
    person_mesure   = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Client')
    mesure_client   = models.ManyToManyField('Produit', verbose_name='Mesure Par Produit')
    # person          = models.ManyToManyField('Person')
    coude           = models.FloatField(null=True, blank=True)
    epaule          = models.FloatField(null=True, blank=True)
    manche          = models.FloatField(null=True, blank=True)
    tour_manche     = models.FloatField(null=True, blank=True)
    taille          = models.FloatField(null=True, blank=True)
    poitrine        = models.FloatField(null=True, blank=True)
    longueur_boubou = models.FloatField(null=True, blank=True)
    longueur_patanlon = models.FloatField(null=True, blank=True)
    fesse           = models.FloatField(null=True, blank=True)
    ceinture        = models.FloatField(null=True, blank=True)
    cuisse          = models.FloatField(null=True, blank=True)
    patte           = models.FloatField(null=True, blank=True)
    create_at       =  models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.person_mesure)

class Produit(models.Model):
    PRODUIT         = (
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
        ('AUTRES', 'AUTRES'),)

    produit         = models.CharField(max_length=25, choices=PRODUIT, default='Boubou')
    price           = models.FloatField(null=True, blank=True)

    def __str__(self):
        return'{}'.format(self.produit)

class Order(models.Model):
    command_person  = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Titulaire command', )
    products        = models.ManyToManyField('Produit', verbose_name='list_commande')
    reception       = models.DateTimeField(auto_now_add=True)
    montant_total   = models.FloatField(null=True, blank=True)
    rendez_vous     = models.DateTimeField(auto_now_add=False)
    livre           = models.BooleanField(default=False)
    create_at       =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return'{}'.format(self.id)

# class ItemsOrders(models.Model):
#         orders      = models.ForeignKey('Orders', on_delete=models.DO_NOTHING)
#         products    = models.ManyToManyField('Produit', verbose_name='list_commande')
#         image       = models.ImageField(upload_to='photos/modele/%Y/%m/%d', null=True, blank=True, verbose_name='Photo_commande')
#         COUTURE     = (
#             ('BRODERIE', 'Broderie'),
#             ('COUTURE SIMPLE', 'Couture simple'),
#             ('COUTURE A MAIN', 'Couture a main'),
#             ('REPARATION', 'Reparation'),)
#         couture     = models.CharField(max_length=25, choices=COUTURE, default='Broderie')
#         TISSU       = (
#             ('BAZIN GETZNER', 'BAZIN GETZNER'),
#             ('BAZIN RICHE', 'BAZIN RICHE'),
#             ('BAZIN MOYEN', 'BAZIN MOYEN'),
#             ('WAX', 'WAX'),
#             ('TISSU', 'TISSU'),
#             ('LEGER', 'LEGER'),
#             ('BRODE', 'BRODE'),
#             ('PERCALE', 'PERCALE'),
#             ('VOILE', 'VOILE'),
#             ('BOGOLAN', 'BOGOLAN'),
#             ('AUTRES', 'AUTRES'),)
#         tissu       = models.CharField(max_length=25, choices=TISSU, default='BAZIN GETZNER')
#         COULOIR     = (
#             ('BLANCHE', 'BLANCHE'),
#             ('ROUGE SANG', 'ROUGE SANG'),
#             ('BLEU', 'BLEU'),
#             ('ORANGE', 'ORANGE'),
#             ('ROSE', 'ROSE'),
#             ('VERT', 'VERT'),
#             ('GRIS', 'GRIS'),
#             ('GRIS CLAIR', 'GRIS CLAIR'),
#             ('VIOLET', 'VIOLET'),
#             ('MARON', 'MARON'),
#             ('MARON CLAIR', 'MARON CLAIR'),
#             ('TURGUOISE', 'TURGUOISE'),
#             ('JAUNE', 'JAUNE'),
#             ('JAUNE COUSIN', 'JAUNE COUSIN'),
#             ('NOIR', 'NOIR'),
#             ('BAGA', 'BAGA'),
#             ('BAGA CLAIR', 'BAGA CLAIR'),
#             ('DEUX TONS', 'DEUX TONS'),
#             ('MULTICOLOR', 'MULTICOLOR'),)
#         couloir      = models.CharField(max_length=25, choices=COULOIR, default='BLANCHE')
#         quantite     = models.PositiveSmallIntegerField()
#         metrage      = models.FloatField()
#         price        = models.FloatField()
#         # sub_price = models.FloatField()
#         avance       = models.FloatField()
#         reliquat     = models.FloatField()
#         remise       = models.FloatField(default=0)
#
#         class Meta:
#             ordering = ["id"]
#
#         def __str__(self):
#             return '{}'.format(self.orders)



class Depense(models.Model):
        titulaire_depense        = models.ForeignKey('Person', on_delete=models.DO_NOTHING, verbose_name='Titulaire Depense',)
        montant_total            = models.PositiveIntegerField(null=True, blank=True)
        is_valide                = models.BooleanField(default=False)
        created_at               = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return '{}'.format(self.is_valide)

# class ItemsDepense(models.Model):
#             MODE_DEPENSE = (
#                 ('MATERIELS', 'Materiels'),
#                 ('FRAIS OUVRIER', 'Frais_Ouvrier'),
#                 # ('BON', 'Bon'),
#                 ('LOCATION', 'Location'),
#                 ('ELECTRICITE', 'Electricite'),
#                 ('CONSOMMABLE', 'Consommable'),
#                 ('IMPOT SYNTHETIQUE', 'Impot_synthetique'),
#                 ('TAXE MUNICIPAL', 'Taxe_municipal'),
#             )
#
#             type_depense = models.CharField(max_length=30, choices=MODE_DEPENSE, default='Materiels', )
#
#             TYPE_MATERIEL       = (
#                 ('FIL', 'Fil'),
#                 ('AIGU', 'Aigu'),
#                 ('SATIN', 'Satin'),
#                 ('POPILINE', 'Popiline'),
#                 ('DUPURE', 'Dupure'),
#                 ('CISEAU', 'Ciseau'),
#                 ('CHARBON', 'Charbon'),
#                 ('COL', 'Col'),
#             )
#
#             type_materiel      = models.CharField(max_length=30, choices=TYPE_MATERIEL, default='Fil', )
#
#             quantite           = models.PositiveSmallIntegerField(default=1)
#             prix_unitaire      = models.PositiveIntegerField(null=True, blank=True)
#             montant_unitaire   = models.PositiveIntegerField(null=True, blank=True)
#             description        = models.TextField(max_length=200, null=True, blank=True)
#             created_at         = models.DateTimeField(auto_now_add=True)
#
#             def __str__(self):
#                 return '{}'.format(self.description)





    # class Meta:
    #       ordering = ('reception',)

    # created_at = models.DateField(auto_now_add=True)

# @python_2_unicode_compatible

#
# # @python_2_unicode_compatible

# Table pour toutes les depenses effectuées dans l'entreprise
# @python_2_unicode_compatible



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
    #     return '{}{}{}'.format(self.ouvrier, self.proprietaire,)

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
