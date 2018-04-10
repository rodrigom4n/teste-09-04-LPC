# Generated by Django 2.0.2 on 2018-04-10 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_auto_20180409_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoAvaliador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='avaliacao',
            name='avaliador',
        ),
        migrations.AddField(
            model_name='avaliacaoavaliador',
            name='avaliacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Avaliacao', to='evento.Avaliacao'),
        ),
        migrations.AddField(
            model_name='avaliacaoavaliador',
            name='avaliador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Avaliador', to='evento.Avaliador'),
        ),
    ]
