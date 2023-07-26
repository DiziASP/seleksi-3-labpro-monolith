from rest_framework import serializers
from .models import PurchaseHistory

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'
    
    def create(self, validated_data):
        new_prod = PurchaseHistory.objects.create(
            user=validated_data['user'],
            product=validated_data['nama'],
            price=validated_data['quantity'],
            total=validated_data['total'],
        )
        new_prod.save()

        return new_prod