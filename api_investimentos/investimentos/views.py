from rest_framework import viewsets
from rest_framework import status
from .models import Currency, Investor, ExchangeRate, InvestmentHistory
from .serializers import CurrencySerializer, InvestorSerializer, ExchangeRateSerializer, InvestmentHistorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

    def perform_create(self, serializer):
        if Investor.objects.filter(email=serializer.validated_data['email']).exists():
            raise serializer.ValidationError({"email": "Este e-mail já está registrado."})
        serializer.save()

class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def perform_create(self, serializer):
        serializer.save()

    #Lista a variação por mais recentes e mais antigas

    @action(detail=False, methods=['get'])
    def recent(self, request):
        seven_days_ago = datetime.now() - timedelta(days=7)
        rates = ExchangeRate.objects.filter(date__gte=seven_days_ago).order_by('-date')
        serializer = self.get_serializer(rates, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def old(self, request):
        thirty_days_ago = datetime.now() - timedelta(days=30)
        deleted_count, _ = ExchangeRate.objects.filter(date__lte=thirty_days_ago).delete()

        if deleted_count > 0:
            return Response(status=status.HTTP_204_NO_CONTENT)  # Retorna 204 quando exclui registros
        return Response({"message": "Nenhum registro para excluir."}, status=status.HTTP_200_OK)  # 200 se nada for excluído
    
class InvestmentHistoryViewSet(viewsets.ModelViewSet):
    queryset = InvestmentHistory.objects.all()
    serializer_class = InvestmentHistorySerializer
