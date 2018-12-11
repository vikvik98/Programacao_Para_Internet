# Generated by Django 2.1.4 on 2018-12-10 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desenvolvedora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fundacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Desenvolvimento_jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_desenvolvimento', models.DateField()),
                ('termino_desenvolvimento', models.DateField()),
                ('desenvolvedora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Desenvolvedora')),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('desenvolvedoras', models.ManyToManyField(through='games.Desenvolvimento_jogo', to='games.Desenvolvedora')),
            ],
        ),
        migrations.AddField(
            model_name='desenvolvimento_jogo',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Jogo'),
        ),
    ]