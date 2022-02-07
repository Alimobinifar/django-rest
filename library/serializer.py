from rest_framework import serializers

from .models import book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ('id', 'name', 'book_cat', 'page', 'price')

    def validate_name(self, value):
        if value in ("admin", "Admin"):
            raise serializers.ValidationError("name cannot be admin")
        return value
