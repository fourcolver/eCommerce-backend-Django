from rest_framework import generics, permissions
from api_product.models import Product
from api_product.serializers import ProductSerializer, EditProductSerializer


class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(added_by=self.request.user).order_by('-id')
        return queryset

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class FeaturedView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        count = int(self.request.GET.get('count') or 5)
        queryset = Product.objects.all().order_by('-id')[:count]
        return queryset

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class TopSellView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        count = int(self.request.GET.get('count') or 5)
        queryset = Product.objects.all().order_by('-id')[5:]
        return queryset

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class OnSaleView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        count = int(self.request.GET.get('count') or 5)
        queryset = Product.objects.all().order_by('-id')[3:]
        return queryset

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class SpecialView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        count = int(self.request.GET.get('count') or 5)
        queryset = Product.objects.all().order_by('-id')[:count]
        return queryset

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class GetProductView(generics.ListAPIView):
    serializer_class = EditProductSerializer

    def get_queryset(self):
        pk = self.kwargs['id']
        queryset = Product.objects.filter(id=pk, added_by=self.request.user)
        return queryset


class UpdateProductView(generics.UpdateAPIView):
    serializer_class = EditProductSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Product.objects.filter(id=pk, added_by=self.request.user)
        return queryset


class DeleteProductView(generics.DestroyAPIView):
    serializer_class = EditProductSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Product.objects.filter(id=pk, added_by=self.request.user)
        return queryset
