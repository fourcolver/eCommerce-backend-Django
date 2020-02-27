from django.db import models
from .order_detail_vendor import Order_Detail_Vendor


class Order_Detail_Customer_Before_Shipping(models.Model):
    PAYMENT = [
        ('C', 'Cash'),
        ('P', 'POS'),
        ('O', 'Online Payment'),
    ]

    id = models.AutoField(primary_key=True)
    orderid = models.ForeignKey(Order_Detail_Vendor, on_delete=models.CASCADE)
    estarrivaldate = models.DateField()
    shippingaddress = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    customername = models.CharField(max_length=100)
    itemcost = models.FloatField()
    paymentstatus = models.BooleanField()
    paymentmode = models.CharField(max_length=2,choices=PAYMENT)
    orderdetaillink = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_detail_customer_before_shipping'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return self.productname