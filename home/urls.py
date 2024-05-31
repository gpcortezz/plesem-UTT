from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('logout/', views.LogOut.as_view(), name="logout"),
    path('singup/', views.SingUp.as_view(), name="singup"),

    ##PROFILE URLS ##
    path('list/profile/', views.ListProfile.as_view(), name="list_profile"),
    path('detail/profile/<int:pk>/', views.DetailProfile.as_view(), name="detail_profile"),
]

