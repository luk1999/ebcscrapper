from rest_framework import (
    generics,
    response,
    viewsets,
)

from scrapper import models
from . import serializers


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CurrencySerializer
    queryset = models.Currency.objects.all()


class CurrencyRateView(generics.GenericAPIView):
    serializer_class = serializers.CurrencyRateSerializer
    queryset = models.CurrencyRate.objects.order_by('-updated_at')
    lookup_field = 'currency'

    def get_queryset(self):
        currency = self.kwargs['currency']
        queryset = super().get_queryset()
        return queryset.filter(currency__symbol=currency)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
