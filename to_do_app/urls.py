
from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-details'),
    path('create/', TaskCreate.as_view(), name='create-task'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
    
    path('login/', CustomLogin.as_view(), name='login' ),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register')

]
