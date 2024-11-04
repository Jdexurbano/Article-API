from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Article

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only = True, required = True)
    password2 = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ['username','password1','password2','email']
    
    def validate(self, attrs):
        #check if the password is match
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"message":"password did not match"})
        return attrs
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email']

        )
        user.set_password(validated_data['password1'])
        user.save()

        return user

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
    
    def create(self, validated_data):
        author = self.context['author']
        validated_data.pop('author',None)#remove the author to validated data
        article = Article.objects.create(author = author, **validated_data)
        return article