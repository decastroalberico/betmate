# Generated by Django 4.2 on 2023-05-14 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_hora', models.DateTimeField(default='2001-01-01 00:00:00')),
            ],
        ),
        migrations.CreateModel(
            name='Atletas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='nome', max_length=100)),
                ('data_nascimento', models.DateTimeField(default='2000-01-01', max_length=100)),
                ('img_perfil', models.ImageField(blank=True, default='img_perfil/default.png', null=True, upload_to='img_perfil/')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='cidade', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome', models.CharField(default='nome', max_length=100)),
                ('email', models.EmailField(default='email', max_length=254, unique=True)),
                ('data_nascimento', models.DateField(blank=True, default='2000-01-01', null=True)),
                ('endereco', models.CharField(blank=True, default='endereco', max_length=200, null=True)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('cliente_cidade', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cidade')),
                ('groups', models.ManyToManyField(blank=True, related_name='cliente_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='cliente_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='nome', max_length=100)),
                ('descricao', models.TextField(default='descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_hora', models.DateTimeField(default='2001-01-01 00:00:00')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cliente')),
                ('compra_aposta', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.aposta')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(default='2000-01-01 00:00:00')),
                ('descricao', models.TextField()),
                ('placar_mandante', models.IntegerField(default=0)),
                ('placar_visitante', models.IntegerField(default=0)),
                ('odd_vitoria', models.FloatField(default=0)),
                ('odd_empate', models.FloatField(default=0)),
                ('odd_derrota', models.FloatField(default=0)),
                ('num_bets', models.IntegerField(default=0)),
                ('chance_mandante', models.FloatField(default=0)),
                ('chance_visitante', models.FloatField(default=0)),
                ('evento_competicao', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.competicao')),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='nome', max_length=100)),
                ('descricao', models.TextField(default='descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='pais', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Scout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='nome', max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='nome', max_length=100)),
                ('sigla', models.CharField(default='sigla', max_length=10, null=True)),
                ('descricao', models.TextField(default='descricao', null=True)),
                ('escudo', models.ImageField(blank=True, default='escudos/default.png', null=True, upload_to='escudos/')),
                ('cidade_time', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cidade')),
                ('time_atletas', models.ManyToManyField(related_name='times', to='front.atletas')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_hora', models.DateTimeField(default='2001-01-01 00:00:00')),
                ('status', models.CharField(default='status', max_length=100)),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cliente')),
                ('compra_aposta', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.aposta')),
            ],
        ),
        migrations.CreateModel(
            name='OpcaoAposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odd', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('evento', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.eventos')),
                ('scout', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.scout')),
                ('time', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.time')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_arena', models.CharField(default='nome_arena', max_length=100)),
                ('local_cidade', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_hora', models.DateTimeField(default='2001-01-01 00:00:00')),
                ('status', models.CharField(default='status', max_length=20)),
                ('metodo_pagamento', models.CharField(default='metodo_pagamento', max_length=100)),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoAposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_hora', models.DateTimeField(default='2001-01-01 00:00:00')),
                ('status', models.CharField(default='status', max_length=100)),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cliente')),
                ('ha_eventos', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.eventos')),
                ('historico_compra', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.compra')),
                ('opcao_aposta', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.opcaoaposta')),
            ],
        ),
        migrations.AddField(
            model_name='eventos',
            name='local',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.local'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='mandante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mandante', to='front.time'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='visitante',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='visitante', to='front.time'),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='estado', max_length=100)),
                ('estado_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.pais')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='compra_pagamento',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.pagamentos'),
        ),
        migrations.AddField(
            model_name='competicao',
            name='competicao_modalidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.modalidade'),
        ),
        migrations.AddField(
            model_name='competicao',
            name='competicao_pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.pais'),
        ),
        migrations.AddField(
            model_name='competicao',
            name='times',
            field=models.ManyToManyField(default=1, related_name='competicoes', to='front.time'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='cidade_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.estado'),
        ),
        migrations.AddField(
            model_name='atletas',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cidade'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.cliente'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='evento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.eventos'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='opcao_aposta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.opcaoaposta'),
        ),
    ]