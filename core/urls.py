from django.urls import path
from django.contrib import admin
from quora_app.views import (
    RegisterView, LoginView, LogoutView,
    HomeView, QuestionCreateView, QuestionDetailView, LikeAnswerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/', QuestionCreateView.as_view(), name='post_question'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('like/<int:answer_id>/', LikeAnswerView.as_view(), name='like_answer'),
]