from django.urls import path
from . import views
from django_prometheus.views import ExportToDjangoView
from health_check.views import health_check, metrics



urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('health/', health_check, name='health_check'),
    path('metrics/', ExportToDjangoView.as_view(), name='metrics'),
]

