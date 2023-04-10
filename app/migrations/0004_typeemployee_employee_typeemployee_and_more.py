# Generated by Django 4.1.5 on 2023-02-26 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employee_liscen_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='typeemployee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.typeemployee'),
        ),
        migrations.AddField(
            model_name='fuelexpense',
            name='typeemployee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.typeemployee'),
        ),
    ]
