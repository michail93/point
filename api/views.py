from decimal import Decimal

from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import StatusRequsetSerializer, StatusInfoSerialzier, ChangeBalanceSerializer
from .models import Abonent


class PingView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response(data={'response': 'pong'}, status=status.HTTP_200_OK)


class StatusView(generics.GenericAPIView):
    serializer_class = StatusRequsetSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        abonent_info = Abonent.objects.get(ab_uuid=serializer.data['uuid'])

        serialized_data = StatusInfoSerialzier(abonent_info)

        response_data = {
            "status": 200,
            "result": True,
            "addition": serialized_data.data
        }

        return Response(data=response_data, status=status.HTTP_200_OK)


class BalanceRefillView(generics.GenericAPIView):
    serializer_class = ChangeBalanceSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        abonent_info = Abonent.objects.get(ab_uuid=serializer.data['uuid'])

        serialized_data = StatusInfoSerialzier(abonent_info)

        response_data = {
            "status": None,
            "result": None,
            "addition": serialized_data.data
        }

        if not abonent_info.status:
            response_data.update({"status": 400})
            response_data.update({"result": False})
            response_data.update({"description": {
                "message": "account is disabled"
            }})
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

        balance = Abonent.refill_balance(serializer.data['uuid'], serializer.data['amount'])

        response_data.update({"status": 200})
        response_data.update({"result": True})
        response_data["addition"].update({"balance": balance})

        return Response(data=response_data, status=status.HTTP_200_OK)


class DecreasingBalanceView(generics.GenericAPIView):
    serializer_class = ChangeBalanceSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        abonent_info = Abonent.objects.get(ab_uuid=serializer.data['uuid'])

        serialized_data = StatusInfoSerialzier(abonent_info)

        response_data = {
            "status": None,
            "result": None,
            "addition": serialized_data.data
        }

        if not abonent_info.status:
            response_data.update({"status": 400})
            response_data.update({"result": False})
            response_data.update({"description": {
                "message": "account is disabled"
            }})
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

        result = abonent_info.balance - abonent_info.hold - Decimal(serializer.data['amount'])

        if result < 0:
            isPossible = False
            response_data.update({"status": 400})
            response_data.update({"result": isPossible})
            response_data.update({"description": {
                "message": "it's not enough monetary means on account"
            }})
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            isPossible = True

            balance = Abonent.decreacse_balance(serializer.data['uuid'], serializer.data['amount'])

            response_data.update({"status": 200})
            response_data.update({"result": isPossible})
            response_data["addition"].update({"balance": balance})

            return Response(data=response_data, status=status.HTTP_200_OK)
