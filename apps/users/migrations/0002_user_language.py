from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en-us', 'English'), ('ru', 'Russian'), ('sr', 'Serbian')],
                                   default='en-us', max_length=5, verbose_name='Language'),
        ),
    ]
