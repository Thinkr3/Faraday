# Generated by Django 3.1.7 on 2021-02-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0006_dataentry_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapool',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]