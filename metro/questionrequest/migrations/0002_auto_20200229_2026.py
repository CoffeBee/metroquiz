# Generated by Django 2.2.7 on 2020-02-29 20:26

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionrequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
