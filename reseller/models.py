from datetime import datetime
from django.db import models

# Create your models here.

class Resellers(models.Model):

    cmp_name = models.CharField(max_length=30,db_column='c_name')
    company_regid = models.CharField(max_length=12,db_column='reg_id')
    cmp_addr = models.CharField(max_length=70,db_column='addr')
    country = models.CharField(max_length=30,db_column='cntry')
    cmp_phno = models.CharField(max_length=12,db_column='phno')
    acc_holder = models.CharField(max_length=30,db_column='acc_hld')
    acc_no = models.CharField(max_length=30,db_column='acc_no')
    acc_ifsc = models.CharField(max_length=30,db_column='ifsc')
    user_type = models.CharField(max_length=20,db_column='type')
    email=models.CharField(max_length=30,db_column='email')
    passwd=models.CharField(max_length=30,db_column='passwd')
    user_id = models.IntegerField(db_column='log_id')
    request_date = models.DateField(default=datetime.now)
    status = models.CharField(max_length=20, default= 'inactive')

    class Meta:
        db_table='reseller_tb'