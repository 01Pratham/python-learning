# Generated by Django 5.0.4 on 2024-04-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ucontact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uemail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uname',
        ),
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.CharField(default='arshad', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='cpassword',
            field=models.CharField(default='arshad', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(default='20/01/2024'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='arshad@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='empid',
            field=models.IntegerField(default=11),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='arshad', max_length=20),
        ),
    ]