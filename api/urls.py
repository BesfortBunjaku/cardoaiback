from django.urls import path
from .views import CashFlowAPIView,CsvFileAPIView
 
urlpatterns = [
    path('cashflow', CashFlowAPIView.as_view(), name='cashflow'),
    path('upload/', CsvFileAPIView.as_view(), name='upload'),
 

]
