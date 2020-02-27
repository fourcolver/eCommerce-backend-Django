from rest_framework import serializers
from api_product.models import Product
from api_category.models import Category
from api_category.serializers import CategoryWithParentSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'image_urls', 'description', 'stock', 'categories', 'cost_price', 'sales_price', 'discount','short_name',
                  'color', 'size', 'dimension_l', 'dimension_w', 'dimension_h', 'weight', 'added_by', 'added_on', 'modified_on')
        read_only_fields = ('added_by', 'added_on')


class EditProductSerializer(serializers.ModelSerializer):
    category_objs = serializers.SerializerMethodField('get_artifact_categories')

    def get_artifact_categories(self, obj):
        categories = []
        for category in obj.categories:
            _category = Category.objects.filter(id=category).first()
            categories.append(_category)
        categories_serializer = CategoryWithParentSerializer(categories, many=True)
        return categories_serializer.data

    class Meta:
        model = Product
        fields = ('id', 'title', 'image_urls', 'description', 'stock', 'categories', 'category_objs', 'cost_price', 'sales_price', 'discount',
                  'color', 'size', 'dimension_l', 'dimension_w', 'dimension_h', 'weight', 'added_by', 'added_on', 'modified_on')
        read_only_fields = ('added_by', 'added_on')
