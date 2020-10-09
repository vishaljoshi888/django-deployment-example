from ravi_app import views
from django.urls import path

# TEMPLATE_TAGGING
app_name = 'ravi_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('actual/', views.actual, name='actual'),
]
