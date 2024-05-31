from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path('list/grantgoal/', views.ListGrantGoal.as_view(), name="list_gg"),
    path('new/grantgoal/', views.NewGrantGoal.as_view(), name="create_gg"),
    path('detail/grantgoal/<int:pk>/', views.DetailGrantGoal.as_view(), name="detail_gg"),
    path('update/grantgoal/<int:pk>/', views.UpdateGrantGoal.as_view(), name="update_gg"),
    path('delete/grantgoal/<int:pk>/', views.DeleteGrantGoal.as_view(), name="delete_gg"),
    ### SUBGRANTGOALS URLS ###
    path('list/subgrantgoal/', views.ListSubGrantGoal.as_view(), name="list_sgg"),
    path('detail/subgrantgoal/<int:pk>/', views.DetailSubGrantGoal.as_view(), name="detail_sgg"),
    path('new/subgrantgoal/', views.NewSubGrantGoal.as_view(), name="create_sgg"),
    path('update/subgrantgoal/<int:pk>/', views.UpdateSubGrantGoal.as_view(), name="update_sgg"),
    path('delete/subgrantgoal/<int:pk>/', views.DeleteSubGrantGoal.as_view(), name="delete_sgg"),
    ### GOAL URLS ###
    path('list/goal/', views.ListGoal.as_view(), name="list_ggg"),
    path('new/goal/', views.NewGoal.as_view(), name="create_ggg"),
    path('detail/goal/<int:pk>/', views.DetailGoal.as_view(), name="detail_ggg"),
    path('update/goal/<int:pk>/', views.UpdateGoal.as_view(), name="update_ggg"),
    path('delete/goal/<int:pk>/', views.DeleteGoal.as_view(), name="delete_ggg"),
    ### ISSUE URLS ###
    path('list/issue/', views.ListIssue.as_view(), name="list_is"),
    path('new/issue/', views.NewIssue.as_view(), name="create_is"),
    path('detail/issue/<int:pk>/', views.DetailIssue.as_view(), name="detail_is"),
    path('update/issue/<int:pk>/', views.UpdateIssue.as_view(), name="update_is"),
    path('delete/issue/<int:pk>/', views.DeleteIssue.as_view(), name="delete_is"),

]
    