from rest_framework import serializers


class MyModelBaseSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner_name = serializers.CharField(source='owner.name', read_only=True)
    owner_id = serializers.IntegerField(source='owner.id', read_only=True)

    deleted_at = serializers.ReadOnlyField()
