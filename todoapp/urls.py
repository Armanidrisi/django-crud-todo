from django.urls import path
from todoapp import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("delete/<str:id>",views.deleteTask,name="Delete"), 
    path("update/<str:id>",views.updateTask,name="Update"),
    path("about",views.about,name="About"),
]
