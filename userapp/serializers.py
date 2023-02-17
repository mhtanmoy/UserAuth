from rest_framework import serializers
from .models import *

class GeographicLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicLocation
        fields = '__all__'

class GeographicSubAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicSubAddress
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    geographicLocation = serializers.SerializerMethodField()
    geographicSubAddress = serializers.SerializerMethodField()
    class Meta:
        model = Address
        fields = '__all__'

    def get_geographicLocation(self, obj):
        geographicLocation_serializer = GeographicLocationSerializer(obj.geographicLocation)
        return geographicLocation_serializer.data

    def get_geographicSubAddress(self, obj):
        geographicSubAddress_serializer = GeographicSubAddressSerializer(obj.geographicSubAddress)
        return geographicSubAddress_serializer.data
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['amount', 'units']

class ValidForSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidFor
        fields = ['endDateTime', 'startDateTime']

class AttachmentSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    validFor = serializers.SerializerMethodField()
    class Meta:
        model = Attachment
        fields = ['id', 'href', 'attachmentType', 'content', 'description', 'mimeType', 'name', 'url', 'size', 'validFor', 'baseType', 'schemaLocation', 'type', 'referredType']

    def get_size(self, obj):
        size_serializer = SizeSerializer(obj.size)
        return size_serializer.data

    def get_validFor(self, obj):
        validFor_serializer = ValidForSerializer(obj.validFor)
        return validFor_serializer.data
class LegalIdSerializer(serializers.ModelSerializer):
    attachment = serializers.SerializerMethodField()
    validFor = serializers.SerializerMethodField()
    class Meta:
        model = LegalId
        fields = ['identificationId', 'identificationType', 'issuingAuthority', 'issuingDate', 'attachment', 'validFor']

    def get_attachment(self, obj):
        attachment_serializer = AttachmentSerializer(obj.attachment)
        return attachment_serializer.data

    def get_validFor(self, obj):
        validFor_serializer = ValidForSerializer(obj.validFor)
        return validFor_serializer.data
class EntitlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entitlement
        fields = ['id' ,'action', 'function']

class UserAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssets
        fields = ['id', 'assetType', 'entityType', 'role', 'entitlement']

class UserAccountSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    legalId = serializers.SerializerMethodField()
    userAssets = serializers.SerializerMethodField()
    class Meta:
        model = UserAccount
        fields = ['birthdate', 'email', 'email_verified', 'family_name', 'gender', 'given_name', 'locale', 'middle_name', 'name', 'nickname', 'phone_number', 'phone_number_verified', 'picture', 'preferred_username', 'profile', 'sub', 'website', 'zoneinfo', 'address', 'legalId', 'userAssets', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_address(self, obj):
        address_serializer = AddressSerializer(obj.address)
        return address_serializer.data

    def get_legalId(self, obj):
        legalId_serializer = LegalIdSerializer(obj.legalId)
        return legalId_serializer.data

    def get_userAssets(self, obj):
        userAssets_serializer = UserAssetsSerializer(obj.userAssets)
        return userAssets_serializer.data

class UserAccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['birthdate', 'email', 'email_verified', 'family_name', 'gender', 'given_name', 'locale', 'middle_name', 'name', 'nickname', 'phone_number', 'phone_number_verified', 'picture', 'preferred_username', 'profile', 'sub', 'website', 'zoneinfo', 'address', 'legalId', 'userAssets', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    