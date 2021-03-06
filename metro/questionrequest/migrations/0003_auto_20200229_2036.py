# Generated by Django 2.2.7 on 2020-02-29 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionrequest', '0002_auto_20200229_2026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос'},
        ),
        migrations.AlterModelOptions(
            name='stationsquestinon',
            options={'verbose_name': 'Станция'},
        ),
        migrations.AlterModelOptions(
            name='textelem',
            options={'verbose_name': 'Станция-вопрос'},
        ),
        migrations.AddField(
            model_name='textelem',
            name='who',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Для кого вопрос'),
            preserve_default=False,
        ),
    ]
