# Generated by Django 4.2 on 2024-12-05 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_rename_usuario_proveedor_usuario_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='categoria_id',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='proveedor',
            new_name='proveedor_id',
        ),
    ]