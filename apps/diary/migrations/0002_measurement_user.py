import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
