from django.urls import path
from . import views

urlpatterns = [
    path('/image-check', views.CheckImage),
    path('/add-annotation', views.AddAnnotation),
    
    path('/report', views.Report),
    
]
