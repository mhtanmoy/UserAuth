from django.db import models
#from django.contrib.auth.models import AbstractUser

# Create your models here.


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
    href = models.URLField()
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

    def __str__(self):
        return self.startDateTime


class Attachment(models.Model):
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
    assetType = models.CharField(max_length=100)
    entityType = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    entitlement = models.ForeignKey(Entitlement, on_delete=models.CASCADE)

    def __str__(self):
        return self.assetType

class UserAccount(models.Model):
    birthdate = models.DateField()
    email = models.EmailField()
    email_verified = models.BooleanField()
    family_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    given_name = models.CharField(max_length=100)
    locale = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    phone_number_verified = models.BooleanField()
    picture = models.URLField()
    preferred_username = models.CharField(max_length=100)
    profile = models.URLField()
    sub = models.UUIDField()
    website = models.URLField()
    zoneinfo = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    legalId = models.ForeignKey(LegalId, on_delete=models.CASCADE)
    userAssets = models.ForeignKey(UserAssets, on_delete=models.CASCADE)

    def __str__(self):
        return self.name