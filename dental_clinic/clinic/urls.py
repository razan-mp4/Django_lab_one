from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointments_view, name='appointments'),
    path('treatments/', views.treatments_view, name='treatments'),
    path('invoices/', views.invoices_view, name='invoices'),
    path('feedbacks/', views.feedbacks_view, name='feedbacks'),
]
