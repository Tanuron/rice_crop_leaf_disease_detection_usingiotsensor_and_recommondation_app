from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict, name='predict'),
    path('store_prediction/', views.store_prediction, name='store_prediction'),
    path('get_predictions/', views.get_predictions, name='get_predictions'),
]
