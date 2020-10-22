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
    sex                = forms.ChoiceField(label='Sex', choices=SEX, required='Homme')
    prenom             = forms.CharField(label='Last Name', max_length=30)
    nom                = forms.CharField(label='First Name', max_length=30)
    contact_1          = forms.IntegerField(label='Telephone')
    email              = forms.EmailField(label='Email', max_length=100)



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

    mesure_modele      = forms.ChoiceField(choices=MESURE_MODELE,)
    person_mesure      = forms.IntegerField()
    mesure_client      = forms.IntegerField()
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



class CommandeForm(forms.Form):

    command_person     = forms.IntegerField()
    reception          = forms.IntegerField()
    rendez_vous        = forms.DateTimeField()
    created_at         = forms.DateTimeField()
    livre = forms.BooleanField()



class Commande_DetailForm(forms.Form):

    image              = forms.ImageField()
    couture            = forms.CharField()
    tissu              = forms.CharField()
    couloir            = forms.CharField()
    quantite           = forms.IntegerField()
    metrage            = forms.FloatField()
    price              = forms.FloatField()
    avance             = forms.FloatField()
    reliquat           = forms.FloatField()
    remise             = forms.FloatField()