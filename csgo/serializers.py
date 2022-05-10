from rest_framework import serializers


class RankingSerializer(serializers.Serializer):
    position = serializers.IntegerField()
    team = serializers.CharField()
    logo = serializers.CharField()
