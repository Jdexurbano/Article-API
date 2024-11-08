from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from django.urls import path
from . import views

urlpatterns = [
    #authentication
    path('token/',TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register/',views.UserRegistrationView.as_view(),name = 'register'),

    #articles
    path('articles/',views.ArticleListView.as_view(),name = 'article_list'),

    #articles of user
    path('articles/users/<int:user_id>/',views.UserArticleListView.as_view(),name = 'user_article_list'),
    path('articles/<int:article_id>/users/<int:user_id>/',views.UserArticleDetailView.as_view(),name = 'user_article_detail'),
]