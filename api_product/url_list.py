from django.urls import re_path
from api_product import views

urlpatterns = [
    re_path(r'create', views.ProductView.as_view()),
    re_path(r'update/(?P<pk>\d+)/?$', views.UpdateProductView.as_view()),
    re_path(r'delete/(?P<pk>\d+)/?$', views.DeleteProductView.as_view()),
    re_path(r'list', views.ProductView.as_view()),
    re_path(r'featured', views.FeaturedView.as_view()),
    re_path(r'top_sell', views.TopSellView.as_view()),
    re_path(r'on_sale', views.OnSaleView.as_view()),
    re_path(r'special', views.SpecialView.as_view()),

    re_path(r'(?P<id>\d+)/?$', views.GetProductView.as_view()),
]
