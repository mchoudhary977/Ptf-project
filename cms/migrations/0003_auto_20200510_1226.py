# Generated by Django 2.0.2 on 2020-05-10 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_certificate_certdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='certimg',
            new_name='CertificateBadge',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='logoimg',
            new_name='CertificateImage',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='certdate',
            new_name='CertificationDate',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='title',
            new_name='Title',
        ),
    ]
