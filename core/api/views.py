from rest_framework import status
from core.models import Article
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, ArticleSerializer


#class view for user registration
class UserRegistrationView(APIView):

    def post(self,request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"account successfully created"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class ArticleListView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self,request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)