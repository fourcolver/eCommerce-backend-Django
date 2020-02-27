from django.db import models


class Order_Detail_Vendor(models.Model):

    PAYMENT = [
        ('C', 'Cash'),
        ('P', 'POS'),
        ('O', 'Online Payment'),
    ]

    id = models.AutoField(primary_key=True)
    orderid = models.CharField(max_length=50)
    productname = models.CharField(max_length=100)
    customername = models.CharField(max_length=100)
    itemcost = models.FloatField()
    paymentstatus = models.BooleanField()
    paymentmode = models.CharField(max_length=2,choices=PAYMENT)
    logistics = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_detail_vendor'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return self.productname