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
    class Meta:
        model = Address
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ValidForSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidFor
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class LegalIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalId
        fields = '__all__'

class EntitlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entitlement
        fields = '__all__'

class UserAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssets
        fields = '__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'

