# Generated by Django 4.2.1 on 2023-06-09 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_country_newssng_newssngimage_pressreleaseimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssngimage',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newsSNGImage', to='app.newssng'),
        ),
        migrations.AlterField(
            model_name='pressreleaseimage',
            name='press_release_news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pressReleaseImage', to='app.press_release'),
        ),
    ]
