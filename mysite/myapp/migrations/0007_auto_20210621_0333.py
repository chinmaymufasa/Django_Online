# Generated by Django 3.2.4 on 2021-06-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210621_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DGE', 'Dodge'), ('CHE', 'Chrevolet'), ('MBZ', 'Mercedes'), ('FRD', 'Ford'), ('TYT', 'Toyota')], max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
