# Generated by Django 4.1.6 on 2023-03-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfe', '0012_alter_login_user_mail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=100),
        ),
    ]
