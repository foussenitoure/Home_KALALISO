from django import forms

class PersonForm(forms.Form):

    STATUS = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),
    )

    status = forms.ChoiceField(label='Status', choices=STATUS, required='CLIENT')

    SEX = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),
    )
    sex         = forms.ChoiceField(label='Sex', choices=SEX, required='Homme')
    prenom      = forms.CharField(label='Last Name', max_length=30)
    nom         = forms.CharField(label='First Name', max_length=30)
    contact_1   = forms.IntegerField(label='Telephone')
    email       = forms.EmailField(label='Email', max_length=100)

class MesureForm(forms.Form):
        person            = forms.IntegerField()
        coude             = forms.FloatField(label='Coude',)
        epaule            = forms.FloatField(label='Epaule',)
        manche            = forms.FloatField(label='Manche',)
        tour_manche       = forms.FloatField(label='Tour Manche',)
        taille            = forms.FloatField(label='Taille',)
        poitrine          = forms.FloatField(label='Poitrine',)
        longueur_boubou   = forms.FloatField(label='Longueur Boubou',)
        longueur_patanlon = forms.FloatField(label='Longueur Patanlon',)
        fesse             = forms.FloatField(label='Fesse',)
        ceinture          = forms.FloatField(label='Ceinture',)
        cuisse            = forms.FloatField(label='Cuisse',)
        patte             = forms.FloatField(label='Patte',)

