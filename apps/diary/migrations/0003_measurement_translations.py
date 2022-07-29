from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diary', '0002_measurement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='description_en_us',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='description_sr',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
