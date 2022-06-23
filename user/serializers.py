from rest_framework import serializers
from .models import MyUser

class SignUpSerializer(serializers.ModelSerializer):
    confirmpassword = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = MyUser
        fields = ['email','password','confirmpassword']
        extra_kwargs = {'password': {'write_only': True},
                        'confirmpassword':{'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirmpassword = validated_data.pop('confirmpassword', None)
        instance = self.Meta.model(**validated_data)
        if password ==  confirmpassword:
            instance.set_password(password)
        else:
            raise serializers.ValidationError("password doesn't match")
        instance.save()
        return instance
