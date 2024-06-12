from rest_framework import serializers

from core.models import GrantGoal

class ListGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = [
            "ggname",
            "timestamp",
            "days_duration",
            "state",
            "status"
        ]

class DetailGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = "__all__"