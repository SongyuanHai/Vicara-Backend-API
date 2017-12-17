from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            employeeID=validated_data['employeeID'],
            role=validated_data['role'],
            level=validated_data['level']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class TimeSheetSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.TimeSheet
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}
        

class ProejctMasterSerializer(serializers.ModelSerializer):
    """A serializer for project master objects."""
    
    class Meta:
        model = models.ProejctMaster
        fields = '__all__'
        
    