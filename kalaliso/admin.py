from django.contrib import admin

# Register your models here.
import os
from django.contrib import admin
from django.contrib import auth
from django import forms
from django.utils import timezone
# from suit.admin import SortableTabularInline
from kalaliso.models import Person, Mesure, Commande, Produit

    #  Depense, ,  Vente, Programme, \
    # DivisionAdministrativeMali

# UserProfileInfo, User,

class KALALISOAdminSite(admin.AdminSite):

    site_header = "KALALISO CREATION"

admin.site = KALALISOAdminSite(name="admin")

class PersonAdmin(admin.ModelAdmin):
    save_on_top = True
    models = Person
    fields = [
              # 'image',
              'status',
              'prenom',
              'nom',
              'sex',
              # 'categorie',
              'contact_1',
              'email']
    #
    # exclude = ['profession',
    #           'alias',
    #           'nationalite',
    #           'contact_2',
    #           'domicile',
    #            'nina',
    #            'telephonique_fix',
    #            'tutuelle',
    #            'numero_reference',
    #            'date_naissance']
    #
    list_display = (
                    # 'image',
                    'status',
                    'prenom',
                    'nom',
                    # 'alias',
                     'sex',
                    # 'categorie',
                    'contact_1',
                    # 'contact_2',
                    # 'domicile',
                     'email'
                    )

    # ordering  = ['created_at']
    # date_hierarchy = 'created_at'
    list_filter = ['status']
    search_fields = ['prenom', 'nom', 'contact_1']
admin.site.register(Person, PersonAdmin)

class ProduitAdmin(admin.ModelAdmin):
    save_on_top = True
    models = Produit
    fields = [
             'produit',
            ]

   #  exclude = ['profession',
   # ]
    list_display = ('produit',)

    # ordering  = ['created_at']
    # date_hierarchy = 'created_at'
    list_filter = ['produit']
    search_fields = ['produit',]
admin.site.register(Produit, ProduitAdmin)


class MesureAdmin(admin.ModelAdmin):
    save_on_top = True
    models = Mesure
    fields = ['coude',
              'epaule',
              'manche',
              'tour_manche',
              'taille',
              'poitrine',
              'longueur_boubou',
              'longueur_patanlon',
              'patte',]

    exclude = ['fesse',
              'ceinture',
              'cuisse',]

    list_display = (
                'coude',
                'epaule',
                'manche',
                'taille',
                'poitrine',
                'longueur_boubou',
                'longueur_patanlon',
                'patte',
                    )

    # ordering  = ['created_at']
    # date_hierarchy = 'created_at'
    # list_filter = ['status']
    # search_fields = ['prenom', 'nom', 'contact_1']
admin.site.register(Mesure, MesureAdmin)

class CommandeAdmin(admin.ModelAdmin):
    save_on_top = True
    models = Commande
    fields = ['command_person',
              # 'produit_command',
              # 'mesure',
               'quantite',
               'couture',
               'tissu',
               'couloir',
               'metrage',
               'prix_unitaire',
               'avance',
               'reliquat',
               'remise',
               'montant_total',
               'rendez_vous',
               # 'reception',
               'livre',
              ]

    # exclude = ['reception']
    list_display = (
                     'command_person',
                     # 'produit_command',
                     # 'mesure',
                     'quantite',
                     'couture',
                     'tissu',
                     'couloir',
                     'metrage',
                     'prix_unitaire',
                     'avance',
                     'reliquat',
                     'remise',
                     'montant_total',
                     'rendez_vous',
                     # 'reception',
                     'livre',)

    # ordering = ['reception']

    list_filter = ['rendez_vous', 'livre']
    search_fields = ['produit_command', 'rendez_vous']
admin.site.register(Commande, CommandeAdmin)



# class DepenseAdmin(admin.ModelAdmin):
#     save_on_top = True
#     models = Depense
#     fields = ['mode_depense',
#               'titulaire_depense',
#               'acquisiteur',
#               'quantite',
#               'prix_unitaire',
#               'is_valide',
#               'montant',
#               'justificatif',
#               'created_at',
#
#               ]
#
#     # exclude = ['created_at',]
#
#     list_display = ('mode_depense',
#                     'titulaire_depense',
#                     'acquisiteur',
#                     'quantite',
#                     'prix_unitaire',
#                     'montant',
#                     'justificatif',
#                     'is_valide',
#                     'created_at',
#                     )
#
#     ordering = ['created_at',]
#     list_filter = ['acquisiteur',]
#     search_fields = ['acquisiteur', 'is_valide',]
# admin.site.register(Depense, DepenseAdmin)
#
#
# class VenteAdmin(admin.ModelAdmin):
#     save_on_top = True
#     models = Vente
#     fields = ['photo_modele',
#               'client',
#               'type_modele',
#               'vente',
#               'montant',
#               'satisfact',
#               'commentaire',
#               ]
#
#     exclude = ['created_at',]
#
#     list_display = ('photo_modele',
#                     'montant',
#                     'satisfact',
#                     'commentaire',
#                     )
#
#     ordering = ['created_at',]
#     list_filter = ['client', 'type_modele',]
#     search_fields = ['client', 'type_modele', 'satisfact',]
# admin.site.register(Vente, VenteAdmin)
#
# class ProgrammeAdmin(admin.ModelAdmin):
#          models = Programme
#          fiels = ['__all__']
#
# admin.site.register(Programme, ProgrammeAdmin)


# FOR TABLE USER AUTHENTICATE

# class UserAdmin(admin.ModelAdmin):
#     models = User
#     fiels = ['__all__']
#
# admin.site.register(User, UserAdmin)
#
#
# class UserProfileInfoAdmin(admin.ModelAdmin):
#     models = UserProfileInfo
#     fiels = ['__all__']
#
# admin.site.register(UserProfileInfo, UserProfileInfoAdmin)


# FOR TABLE DIVISION ADMINISTRATION DU MALI

# class DivisionAdministrativeMaliAdmin(admin.ModelAdmin):
#          models = DivisionAdministrativeMali
#          fiels = ['__all__']
#
# admin.site.register(DivisionAdministrativeMali, DivisionAdministrativeMaliAdmin)


# class RegionAdmin(admin.ModelAdmin):
#     models = Region
#     fiels = ['id',
#              'codereg',
#              'name']
#
#     list_display = [
#         'id',
#         'codereg',
#         'name',    ]

# admin.site.register(Region, RegionAdmin)