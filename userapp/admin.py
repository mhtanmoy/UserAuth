from django.contrib import admin
from .models import GeographicLocation, GeographicSubAddress, Address, Size, ValidFor, Attachment, LegalId, Entitlement, UserAssets, UserAccount

# Register your models here.
admin.site.register([GeographicLocation, GeographicSubAddress, Address, Size, ValidFor, Attachment, LegalId, Entitlement, UserAssets, UserAccount])
