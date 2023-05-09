from rest_framework import serializers
from .models import User, TextAnalysis
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims to the token
        token['name'] = user.name
        
        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at', 'updated_at', 'api_gpt_key', 'is_active', 'is_admin']

class TextAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAnalysis
        fields = ['id', 'text', 'mood', 'color', 'font_policy', 'created_at']
