from django.urls import path
from .views import register, user_login,user_logout


urlpatterns = [
    path('', register,name='register'),
    # path('new', new),
    path('logout/', user_logout,name='logout'),
    path('login/', user_login, name='login'),

]
