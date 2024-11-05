from rest_framework import status
from django.http import Http404
from core.models import Article
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, ArticleSerializer


#class view for user registration
class UserRegistrationView(APIView):

    def post(self,request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"account successfully created"}, status = status.HTTP_201_CREATED)
        return Response({
            "errors":serializer.errors,
            "message":"registration failed due to validation errors"
        },status = status.HTTP_400_BAD_REQUEST)


class ArticleListView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self,request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class UserArticleListView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_object(self,user_id):
        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist:
            raise NotFound(detail = "user not found")

    def get(self,request,user_id):
        user = self.get_object(user_id)
        articles = user.articles.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,request,user_id):
        author = self.get_object(user_id)
        serializer = ArticleSerializer(data = request.data, context = {'author':author})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({"errors":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

class UserArticleDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self,user_id,article_id):
        try:
            user = User.objects.get(pk = user_id)
            article = user.articles.get(pk = article_id)
            return article
        except Article.DoesNotExist:
            raise NotFound(detail = "article not found")

    def get(self,request,user_id,article_id):
        article = self.get_object(user_id,article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    def put(self,request,user_id,article_id):
        article = self.get_object(user_id,article_id)
        author_instance = User.objects.get(pk = user_id)
        serializer = ArticleSerializer(article, data = request.data, context = {'author':author_instance})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({"errors":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,user_id,article_id):
        article = self.get_object(user_id,article_id)
        article.delete()
        return Response({'message':'article deleted successfully'}, status = status.HTTP_200_OK)