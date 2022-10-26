# Generated by Django 4.0.4 on 2022-10-26 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('plate', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True, verbose_name='Plate')),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('status', models.CharField(choices=[('ruta', 'ruta'), ('sede', 'sede')], default='sede', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_plate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.bus')),
            ],
        ),
        migrations.CreateModel(
            name='StopPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_hour_start', models.DateTimeField(blank=True, null=True)),
                ('date_hour_end', models.DateTimeField(blank=True, null=True)),
                ('bus_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bus')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Name')),
                ('password', models.CharField(max_length=8, verbose_name='Password')),
                ('type', models.IntegerField(choices=[(0, 'admin'), (1, 'student'), (2, 'driver'), (3, 'guard')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TravelRegisterDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_student', models.IntegerField()),
                ('stop_point_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stoppoint')),
                ('travel_register_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.travelregister')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
