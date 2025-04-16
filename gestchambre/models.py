from django.db import models

class Client(models.Model):
    noms = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    genre = models.CharField(max_length=1, default='M', choices=[('M', 'Masculin'),('F', 'Féminin')])

    def __str__(self):
        return f"{self.noms} _ {self.genre}"

class Chambre(models.Model):
    TYPE_CHOICES = [
        ('simple', 'Simple'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    
    ETAT_TYPES = [
        ('libre', 'Libre'),
        ('réservée', 'Réservée'),
        ('occupée', 'Occupée'),
    ]
    
    numero = models.CharField(max_length=10, unique=True)
    type_chambre = models.CharField(max_length=10, choices=TYPE_CHOICES)
    prix_par_nuit = models.DecimalField(max_digits=7, decimal_places=2)
    etat = models.CharField(max_length=15, choices=ETAT_TYPES, default='libre')
    description = models.TextField(blank=True)
    nombre_de_lits = models.IntegerField()
    photo = models.ImageField(upload_to='chambres/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chambre {self.numero} - {self.get_type_chambre_display()}"





