import uuid

from .models import Abonent
from rest_framework import serializers


class StatusRequsetSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(format='hex_verbose')

    def validate_uuid(self, value):

        try:
            Abonent.objects.get(ab_uuid=value)
        except Abonent.DoesNotExist:
            raise serializers.ValidationError(f'Abonent with uuid {value} does not exist')
        else:
            return value


class StatusInfoSerialzier(serializers.Serializer):
    uuid = serializers.UUIDField(source='ab_uuid')
    full_name = serializers.CharField()
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    hold = serializers.DecimalField(max_digits=12, decimal_places=2)
    status = serializers.BooleanField()


class ChangeBalanceSerializer(StatusRequsetSerializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2, min_value=1)
