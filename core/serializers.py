from rest_framework import serializers


class MyModelBaseSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner_name = serializers.SerializerMethodField()

    deleted_at = serializers.ReadOnlyField()

    def get_owner_name(self, obj):
        return obj.owner.get_full_name()
