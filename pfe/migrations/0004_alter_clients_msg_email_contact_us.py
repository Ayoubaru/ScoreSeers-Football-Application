# Generated by Django 4.1.6 on 2023-02-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfe', '0003_rename_email_clients_msg_email_contact_us_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients_msg',
            name='email_contact_us',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
