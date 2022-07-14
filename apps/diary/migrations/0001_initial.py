import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now, verbose_name='Measurement day')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Measurement time')),
                ('temperature', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True,
                                                    verbose_name='Temperature (Celsius)')),
                ('health', models.CharField(choices=[('EXCELLENT', 'Excellent'), ('GOOD', 'Good'), ('BAD', 'Bad')],
                                            default='EXCELLENT', max_length=9, verbose_name='Health')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_bout', models.BooleanField(default=False, verbose_name='High blood pressure bout')),
            ],
            options={
                'verbose_name': 'measurement',
                'verbose_name_plural': 'measurements',
                'db_table': 'measurement',
            },
        ),
        migrations.CreateModel(
            name='RightHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic',
                 models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500)],
                                     verbose_name='Systolic (high) blood pressure')),
                ('diastolic',
                 models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500)],
                                     verbose_name='Diastolic (high) blood pressure')),
                ('pulse',
                 models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500)],
                                     verbose_name='Pulse')),
                ('measurement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                     related_name='right_hand', to='diary.measurement',
                                                     verbose_name='Measurement')),
            ],
            options={
                'verbose_name': 'right hand',
                'verbose_name_plural': 'right hands',
                'db_table': 'right_hand',
            },
        ),
        migrations.CreateModel(
            name='LeftHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic',
                 models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500)],
                                     verbose_name='Systolic (high) blood pressure')),
                ('diastolic',
                 models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500)],
                                     verbose_name='Diastolic (high) blood pressure')),
                ('pulse',
                 models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500)],
                                     verbose_name='Pulse')),
                ('measurement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                     related_name='left_hand', to='diary.measurement',
                                                     verbose_name='Measurement')),
            ],
            options={
                'verbose_name': 'left hand',
                'verbose_name_plural': 'left hands',
                'db_table': 'left_hand',
            },
        ),
    ]
