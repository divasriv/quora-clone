from django.urls import path
from django.contrib import admin
from quora_app.views import (
    RegisterView, LoginView, LogoutView,
    HomeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
