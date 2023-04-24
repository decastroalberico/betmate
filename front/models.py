from django.db import models

class Eventos(models.Model):
    modalidade = models.CharField(max_length=(100), null=False, blank=False) 
    campeonato = models.CharField(max_length=(100), null=False, blank=False)
    mandante = models.CharField(max_length=(100), null=False, blank=False)
    visitante = models.CharField(max_length=(100), null=False, blank=False)
    placar_mandante = models.IntegerField(null=False, blank=False) 
    placar_visitante = models.IntegerField(null=False, blank=False) 
    odd_vitoria = models.FloatField(null=False, blank=False) 
    odd_empate = models.FloatField(null=False, blank=False) 
    odd_derrota = models.FloatField(null=False, blank=False) 
    num_bets = models.IntegerField(null=False, blank=False)
    chance_mandante = models.FloatField(null=False, blank=False)
    chance_visitante = models.FloatField(null=False, blank=False)
    img_mandante = models.CharField(max_length=(100), null=False, blank=False)
    img_visitante = models.CharField(max_length=(100), null=False, blank=False)

    def __str__(self):
        return f"Campeonato [campeonato={self.campeonato}]"

