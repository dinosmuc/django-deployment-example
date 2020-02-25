from django.conf.urls import url,include
from app import views

app_name = "app"

urlpatterns = [
    url(r'^database/',views.database, name="database"),
    url(r'^input/',views.input, name="input"),
    ]
