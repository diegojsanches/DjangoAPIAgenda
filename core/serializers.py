from rest_framework import serializers


class MyModelBaseSerializer:
    deleted_at = serializers.ReadOnlyField()
