from rest_framework import serializers

from Contact.Address.models import Address
from core.serializers import MyModelBaseSerializer


class AddressSerializer(MyModelBaseSerializer):

    class Meta:
        model = Address
        fields = (
            'pk',
            'owner',
            'zip_code',
            'street',
            'number',
            'complement',
            'district',
            'city',
            'state',
            'created_at',
            'updated_at',
        )