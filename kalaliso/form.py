from django import forms




class PersonForm(forms.Form):

    STATUS            = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),
    )

    status             = forms.ChoiceField(label='Status', choices=STATUS, required='CLIENT')

    SEX                = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),
    )
    CATEGORIE = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),
    )
    sex                = forms.ChoiceField(label='SEX', choices=SEX, required='Homme')
    prenom             = forms.CharField(label='LAST NAME', max_length=30)
    nom                = forms.CharField(label='FIRST NAME', max_length=30)
    contact_1          = forms.IntegerField(label='TELEPHONE')
    email              = forms.EmailField(label='EMAIL', max_length=100)
    categorie          = forms.CharField(max_length=20, choices=CATEGORIE, default='Grande')
    domicile           = forms.CharField(label='DOMICILE', max_length=30, null=True, blank=True, default='Lafiabougou')
    alias              = forms.CharField(label='ALIAS', max_length=30, null=True, blank=True)
    profession         = forms.CharField(label='PROFESSION', max_length=30, null=True, blank=True)
    contact_2          = forms.CharField(label='CONTACT 2', max_length=20, null=True, blank=True)
    date_naissance     = forms.DateField(auto_now_add=True)
    nationalite        = forms.CharField(label='NATIONALITE',max_length=30, null=True, blank=True)
    tutuelle           = forms.CharField(label='TUTUELLE',max_length=30, null=True, blank=True)
    telephonique_fix   = forms.CharField(label='TELEPHONIQUE FIXE',max_length=30, null=True, blank=True)
    numero_reference   = forms.IntegerField(label='NUMERO REFERENCE', null=True, blank=True)
    nina               = forms.IntegerField(label='NINA',null=True, blank=True)


class ProductForm(forms.Form):
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

    produit          = forms.ChoiceField(label='PRODUCT', choices=PRODUIT, required='Boubou')


class MesureForm(forms.Form):

    MESURE_MODELE      = (
        ('Boubou', 'Boubou'),
        ('Grand Boubou', 'Grand Boubou'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Complet', 'Pagne Complet'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Veste complet', 'Veste Complet'),
        ('Abacos Complet', 'Abacos Complet'),
        ('Abacos Simple', 'Abacos Simple'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),)

    PRODUCTS_MODEL      = (
        ('Boubou', 'Boubou'),
        ('Grand Boubou', 'Grand Boubou'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Complet', 'Pagne Complet'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Veste complet', 'Veste Complet'),
        ('Abacos Complet', 'Abacos Complet'),
        ('Abacos Simple', 'Abacos Simple'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),)

    mesure_modele      = forms.ChoiceField(choices=MESURE_MODELE,)
    person_mesure      = forms.ModelChoiceField('Person')
    mesure_client      = forms.ModelMultipleChoiceField(label='Product',
                                                        required=False,
                                                        widget=forms.CheckboxSelectMultiple,
                                                        choices='PRODUCTS_MODEL')
    coude              = forms.FloatField(label='Coude',)
    epaule             = forms.FloatField(label='Epaule',)
    manche             = forms.FloatField(label='Manche',)
    tour_manche        = forms.FloatField(label='Tour Manche',)
    taille             = forms.FloatField(label='Taille',)
    poitrine           = forms.FloatField(label='Poitrine',)
    longueur_boubou    = forms.FloatField(label='Longueur Boubou',)
    longueur_patanlon  = forms.FloatField(label='Longueur Patanlon',)
    fesse              = forms.FloatField(label='Fesse',)
    ceinture           = forms.FloatField(label='Ceinture',)
    cuisse             = forms.FloatField(label='Cuisse',)
    patte              = forms.FloatField(label='Patte',)
    created_at         = forms.DateTimeField()
    updated_at         = forms.DateTimeField()


class DepenseForm(forms.Form):

    titulaire_depense  = forms.IntegerField()
    montant_total      = forms.IntegerField()
    is_valide          = forms.BooleanField()
    created_at         = forms.DateTimeField()



class Depense_DetailForm(forms.Form):

    type_depense        = forms.CharField()
    depense             = forms.ModelChoiceField('Depense', )
    type_materiel       = forms.CharField()
    quantite            = forms.IntegerField()
    prix_unitaire       = forms.IntegerField()
    montant_unitaire    = forms.IntegerField()
    description         = forms.CharField()
    created_at          = forms.DateTimeField()



class CommandeForm(forms.Form):

    command_person     = forms.ModelChoiceField()
    reception          = forms.IntegerField()
    rendez_vous        = forms.DateTimeField()
    created_at         = forms.DateTimeField()
    livre              = forms.BooleanField()



class Commande_DetailForm(forms.Form):

    PRODUCTS_MODEL      = (
        ('Boubou', 'Boubou'),
        ('Grand Boubou', 'Grand Boubou'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Complet', 'Pagne Complet'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Veste complet', 'Veste Complet'),
        ('Abacos Complet', 'Abacos Complet'),
        ('Abacos Simple', 'Abacos Simple'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),)


    image              = forms.ImageField()
    command            = forms.ModelChoiceField('Commande')
    products           = forms.ModelMultipleChoiceField(label='Product',
                                                        required=False,
                                                        widget=forms.CheckboxSelectMultiple,
                                                        choices='PRODUCTS_MODEL')
    couture            = forms.CharField()
    tissu              = forms.CharField()
    couloir            = forms.CharField()
    quantite           = forms.IntegerField()
    metrage            = forms.FloatField()
    price              = forms.FloatField()
    avance             = forms.FloatField()
    reliquat           = forms.FloatField()
    remise             = forms.FloatField()
