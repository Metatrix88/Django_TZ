from django.urls import path
from . import views
app_name = 'wild'

urlpatterns = [
    path('wildberries/', views.Wildberries.as_view(), name="wild"),
]
