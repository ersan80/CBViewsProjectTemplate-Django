from django.urls import path
from .views import home,student_list, student_add, student_detail, student_update,student_delete,HomeView,StudentListView,StudentDetailView,StudentCreateView,StudentUpdateView,StudentDeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

urlpatterns = [
    #path('', home, name="home"),
    path("",HomeView.as_view(), name="home"),
    path(" ", TemplateView.as_view( template_name = "fscohort/home.html"), name="home"),
    #path('student_list/', student_list, name="list"),
    path("student_list/", StudentListView.as_view(), name="list"),
    #path('student_add/', student_add, name="add"),
    path("student_add" , StudentCreateView.as_view(), name="add"),
    #path('detail/<int:id>/', student_detail, name="detail"),
    path("detail/<int:id>/", StudentDetailView.as_view(), name="detail"),
    #path('update/<int:id>/', student_update, name="update"),
    path("update/<int:pk>/", StudentUpdateView.as_view(), name="update"),
    #path('delete/<int:id>/', student_delete, name="delete"),
    path("delete/<int:pk>/",StudentDeleteView.as_view(),name="delete")
    
]