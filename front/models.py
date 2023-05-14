from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from allauth.socialaccount.models import SocialAccount

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail deve ser informado')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O superusuário deve ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Pais(models.Model):
    nome = models.CharField(max_length=100, default='pais')

    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=100, default='estado')
    estado_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100, default='cidade')
    cidade_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cliente(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100, default='nome')
    email = models.EmailField(unique=True, default='email')
    data_nascimento = models.DateField(null=True, blank=True,default='2000-01-01')
    endereco = models.CharField(max_length=200, null=True, blank=True, default='endereco')
    cliente_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1)
    saldo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    # Adicione um related_name exclusivo aqui
    groups = models.ManyToManyField(
        'auth.Group', related_name='cliente_groups', blank=True
    )

    # Adicione um related_name exclusivo aqui
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='cliente_user_permissions', blank=True
    )

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

class Atletas(models.Model):
    nome = models.CharField(max_length=(100), null=False, blank=False, default='nome')
    data_nascimento = models.DateTimeField(max_length=(100), null=False, blank=False, default='2000-01-01')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1)
    img_perfil = models.ImageField(upload_to='img_perfil/', null=True, blank=True, default='img_perfil/default.png')

    def __str__(self):
        return f"Atleta [nome={self.nome}]"

class Time(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    sigla = models.CharField(max_length=10, null=True, default='sigla')
    cidade_time = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1)
    descricao = models.TextField(null=True, default='descricao')
    escudo = models.ImageField(upload_to='escudos/', null=True, blank=True, default='escudos/default.png')
    time_atletas = models.ManyToManyField(Atletas, related_name='times')

    def __str__(self):
        return f"Time [nome={self.nome}]"
    
class Modalidade(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    descricao = models.TextField(default='descricao')

class Competicao(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    competicao_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    descricao = models.TextField(default='descricao')
    competicao_modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, default=1)
    times = models.ManyToManyField(Time, related_name='competicoes', default=1)

    def __str__(self):
        return f"Competição [nome={self.nome}]"

class Local(models.Model):
    nome_arena = models.CharField(max_length=100, default='nome_arena')
    local_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.nome_arena}, {self.cidade}'

class Eventos(models.Model):
    evento_competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE, default=1)
    data_hora = models.DateTimeField(default='2000-01-01 00:00:00')
    descricao = models.TextField()
    mandante = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='mandante', default=1)
    visitante = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='visitante', default=2)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, default=1)
    placar_mandante = models.IntegerField(null=False, blank=False, default=0) 
    placar_visitante = models.IntegerField(null=False, blank=False, default=0)
    odd_vitoria = models.FloatField(null=False, blank=False, default=0) 
    odd_empate = models.FloatField(null=False, blank=False, default=0) 
    odd_derrota = models.FloatField(null=False, blank=False, default=0) 
    num_bets = models.IntegerField(null=False, blank=False, default=0)
    chance_mandante = models.FloatField(null=False, blank=False, default=0)
    chance_visitante = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return f'{self.time_casa} vs {self.time_fora} - {self.competicao}'

class Scout(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class OpcaoAposta(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, default=1)
    scout = models.ForeignKey(Scout, on_delete=models.CASCADE, default=1)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True, default=1)
    odd = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.evento} - {self.scout} - {self.time}'
    
class Aposta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, default=1)
    opcao_aposta = models.ForeignKey(OpcaoAposta, on_delete=models.CASCADE, default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_hora = models.DateTimeField(default='2001-01-01 00:00:00')

    def __str__(self):
        return f'{self.cliente} - {self.evento} - {self.opcao_aposta}'

class HistoricoCompra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_hora = models.DateTimeField(default='2001-01-01 00:00:00')
    status = models.CharField(max_length=20, default='status')
    metodo_pagamento = models.CharField(max_length=100, default='metodo_pagamento')

    def __str__(self):
        return f'{self.cliente} - {self.valor} - {self.metodo_pagamento}'

class Pagamentos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    compra_aposta = models.ForeignKey(Aposta, on_delete=models.CASCADE, null=True, default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_hora = models.DateTimeField(default='2001-01-01 00:00:00')
    status = models.CharField(max_length=(100), null=False, blank=False, default='status')

    def __str__(self):
        return f"Pagamento [cliente={self.cliente}]"

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    compra_aposta = models.ForeignKey(Aposta, on_delete=models.CASCADE, null=True, default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_hora = models.DateTimeField(default='2001-01-01 00:00:00')
    compra_pagamento = models.ForeignKey(Pagamentos, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return f'{self.cliente} - {self.valor}'
    
class HistoricoAposta(models.Model):
    historico_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, null=True, default=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    ha_eventos = models.ForeignKey(Eventos, on_delete=models.CASCADE, default=1)
    opcao_aposta = models.ForeignKey(OpcaoAposta, on_delete=models.CASCADE, default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_hora = models.DateTimeField(default='2001-01-01 00:00:00')
    status = models.CharField(max_length=(100), null=False, blank=False, default='status')

    def __str__(self):
        return f'{self.cliente} - {self.opcao_aposta}'