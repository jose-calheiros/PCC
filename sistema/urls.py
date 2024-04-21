from django.urls import path

from . import views

urlpatterns = [
   
   path("", views.read, name="read"),
   path("add", views.add, name="add"),
   path("delete/<int:experimento_id>", views.delete, name="delete"),
   path("update/<int:experimento_id>", views.update, name="update"),
   path("confdelete/<int:experimento_id>", views.confdelete, name="confdelete"),
]