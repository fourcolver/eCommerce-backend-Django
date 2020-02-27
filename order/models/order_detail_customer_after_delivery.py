from django.db import models
from .order_detail_vendor import Order_Detail_Vendor


class Order_Detail_Customer_After_Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    orderid = models.ForeignKey(Order_Detail_Vendor, on_delete=models.CASCADE)
    rateorder = models.BooleanField()
    trackpackagelink = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_detail_customer_after_delivery'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return self.orderid