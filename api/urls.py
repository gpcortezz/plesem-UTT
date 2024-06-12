from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    path('v1/list/grantgoal/', views.ListGrantGoalAPIView.as_view(), name='list_gg_api'),
    path('v1/detail/grantgoal/<int:pk>/', views.DetailGrantGoalAPIView.as_view(), name='detail_gg_api'),
]
