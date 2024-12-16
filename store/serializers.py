from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection', 'description']

    price_with_tax = serializers.SerializerMethodField()

    def get_price_with_tax(self, product):
        return product.unit_price * Decimal(1.1)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, collection):
        return collection.products.count()