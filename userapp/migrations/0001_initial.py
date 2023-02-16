# Generated by Django 4.1.7 on 2023-02-16 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.URLField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=20)),
                ('stateOrProvince', models.CharField(max_length=100)),
                ('streetName', models.CharField(max_length=100)),
                ('streetNr', models.CharField(max_length=20)),
                ('streetNrLast', models.CharField(max_length=20)),
                ('streetNrLastSuffix', models.CharField(max_length=10)),
                ('streetNrSuffix', models.CharField(max_length=10)),
                ('streetSuffix', models.CharField(max_length=100)),
                ('streetType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.URLField()),
                ('attachmentType', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('mimeType', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('baseType', models.CharField(max_length=200)),
                ('schemaLocation', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('referredType', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entitlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GeographicLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('baseType', models.CharField(max_length=100)),
                ('schemaLocation', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('referredType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GeographicSubAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=200)),
                ('buildingName', models.CharField(max_length=100)),
                ('levelNumber', models.CharField(max_length=20)),
                ('levelType', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('privateStreetName', models.CharField(max_length=100)),
                ('privateStreetNumber', models.CharField(max_length=20)),
                ('subAddressType', models.CharField(max_length=100)),
                ('subUnitNumber', models.CharField(max_length=20)),
                ('subUnitType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LegalId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificationId', models.CharField(max_length=100)),
                ('identificationType', models.CharField(max_length=100)),
                ('issuingAuthority', models.CharField(max_length=100)),
                ('issuingDate', models.DateTimeField()),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.attachment')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('units', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ValidFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endDateTime', models.DateTimeField()),
                ('startDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAssets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetType', models.CharField(max_length=100)),
                ('entityType', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('entitlement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.entitlement')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('email_verified', models.BooleanField()),
                ('family_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('given_name', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=10)),
                ('middle_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('phone_number_verified', models.BooleanField()),
                ('picture', models.URLField()),
                ('preferred_username', models.CharField(max_length=100)),
                ('profile', models.URLField()),
                ('sub', models.UUIDField()),
                ('website', models.URLField()),
                ('zoneinfo', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.address')),
                ('legalId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.legalid')),
                ('userAssets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userassets')),
            ],
        ),
        migrations.AddField(
            model_name='legalid',
            name='validFor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.validfor'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.size'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='validFor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.validfor'),
        ),
        migrations.AddField(
            model_name='address',
            name='geographicLocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.geographiclocation'),
        ),
        migrations.AddField(
            model_name='address',
            name='geographicSubAddress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.geographicsubaddress'),
        ),
    ]
