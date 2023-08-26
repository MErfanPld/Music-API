from rest_framework import serializers
from .models import Special, PlanMusic


class PlanMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMusic
        fields = "__all__"


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ["user", "plan_music", "expires_at"]
