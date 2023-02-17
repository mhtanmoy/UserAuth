# Generated by Django 4.1.7 on 2023-02-16 17:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
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
            name='LegalId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificationId', models.CharField(max_length=100)),
                ('identificationType', models.CharField(max_length=100)),
                ('issuingAuthority', models.CharField(max_length=100)),
                ('issuingDate', models.DateTimeField()),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.attachment')),
                ('validFor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.validfor')),
            ],
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
                ('geographicLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.geographiclocation')),
                ('geographicSubAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.geographicsubaddress')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('email_verified', models.BooleanField(blank=True, null=True)),
                ('family_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('given_name', models.CharField(blank=True, max_length=100, null=True)),
                ('locale', models.CharField(blank=True, max_length=10, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number_verified', models.BooleanField(blank=True, null=True)),
                ('picture', models.URLField(blank=True, null=True)),
                ('preferred_username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('profile', models.URLField(blank=True, null=True)),
                ('sub', models.UUIDField(blank=True, null=True, unique=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('zoneinfo', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('legalId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.legalid')),
                ('userAssets', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.userassets')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
