from drf_writable_nested import WritableNestedModelSerializer

from Contact.Address.serializers import AddressSerializer
from Contact.models import Contact
from core.serializers import MyModelBaseSerializer


class ContactSerializer(MyModelBaseSerializer, WritableNestedModelSerializer):
    addresses = AddressSerializer(many=True, required=False)

    class Meta:
        model = Contact
        fields = (
            'pk',
            'owner_name',
            'name',
            'is_global',
            'fone',
            'email',
            'addresses',
            'created_at',
            'updated_at',
        )
