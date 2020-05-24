from django.urls import path
from rest_framework import routers

from . import views

app_name = 'api_v1'

router = routers.SimpleRouter()
router.register(r'currency', views.CurrencyViewSet)


urlpatterns = [
    path('currency/rate/<currency>-EUR/', views.CurrencyRateView.as_view()),
]
urlpatterns += router.urls
