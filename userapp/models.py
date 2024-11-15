from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class GeographicLocation(models.Model):
    href = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    baseType = models.CharField(max_length=100)
    schemaLocation = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    referredType = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GeographicSubAddress(models.Model):
    href = models.CharField(max_length=200)
    buildingName = models.CharField(max_length=100)
    levelNumber = models.CharField(max_length=20)
    levelType = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    privateStreetName = models.CharField(max_length=100)
    privateStreetNumber = models.CharField(max_length=20)
    subAddressType = models.CharField(max_length=100)
    subUnitNumber = models.CharField(max_length=20)
    subUnitType = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Address(models.Model):
    href = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    stateOrProvince = models.CharField(max_length=100)
    streetName = models.CharField(max_length=100)
    streetNr = models.CharField(max_length=20)
    streetNrLast = models.CharField(max_length=20)
    streetNrLastSuffix = models.CharField(max_length=10)
    streetNrSuffix = models.CharField(max_length=10)
    streetSuffix = models.CharField(max_length=100)
    streetType = models.CharField(max_length=100)
    geographicLocation = models.ForeignKey(GeographicLocation, on_delete=models.CASCADE)
    geographicSubAddress = models.ForeignKey(GeographicSubAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Size(models.Model):
    amount = models.PositiveIntegerField()
    units = models.CharField(max_length=200)

    def __str__(self):
        return self.units


class ValidFor(models.Model):
    endDateTime = models.DateTimeField()
    startDateTime = models.DateTimeField()



class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    href = models.URLField(max_length=200)
    attachmentType = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    description = models.TextField()
    mimeType = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE)
    baseType = models.CharField(max_length=200)
    schemaLocation = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    referredType = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LegalId(models.Model):
    identificationId = models.CharField(max_length=100)
    identificationType = models.CharField(max_length=100)
    issuingAuthority = models.CharField(max_length=100)
    issuingDate = models.DateTimeField()
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE)

    def __str__(self):
        return self.identificationId


class Entitlement(models.Model):
    action = models.CharField(max_length=100)
    function = models.CharField(max_length=100)

    def __str__(self):
        return self.action

class UserAssets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assetType = models.CharField(max_length=100)
    entityType = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    entitlement = models.ForeignKey(Entitlement, on_delete=models.CASCADE)

    def __str__(self):
        return self.assetType

class UserAccount(AbstractUser):
    customusermanager = CustomUserManager()
    birthdate = models.DateField(blank=True, null=True)
    email_verified = models.BooleanField(blank=True, null=True)
    family_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    given_name = models.CharField(max_length=100, blank=True, null=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_number_verified = models.BooleanField(blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    preferred_username = models.CharField(max_length=100, unique=True)
    profile = models.URLField(blank=True, null=True)
    sub = models.UUIDField(unique=True, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    zoneinfo = models.CharField(max_length=100, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    legalId = models.ForeignKey(LegalId, on_delete=models.CASCADE, blank=True, null=True)
    userAssets = models.ForeignKey(UserAssets, on_delete=models.CASCADE, blank=True, null=True)

    first_name = None
    last_name = None

    username = None
    USERNAME_FIELD = 'preferred_username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.preferred_username