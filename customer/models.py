from django.db import models

# Create your models here.

# class UserDetails(models.Model):
#     user_name=models.CharField(max_length=20,db_column='u_name')
#     passwd=models.CharField(max_length=20,db_column='passwd')
#     type=models.IntegerField(db_column='type')

#     class Meta:
#         db_table='user_tb'

class Customer(models.Model):
    first_name = models.CharField(max_length=30,db_column='f_name')
    last_name = models.CharField(max_length=30,db_column='l_name')
    mobile = models.CharField(max_length=12,db_column='mob')
    gender = models.CharField(max_length=6,db_column='gender')
    dob = models.DateField(db_column='dob')
    address = models.CharField(max_length=70,db_column='addr')
    country = models.CharField(max_length=30,db_column='cntry')
    user_type = models.CharField(max_length=10,db_column='u_type')
    email = models.CharField(max_length=50,db_column='email')
    passwd = models.CharField(max_length=50,db_column='passwd')
    otp = models.CharField(max_length=70,db_column='otp')
    status = models.CharField(max_length=20, default="",db_column='status')

    class Meta:
        db_table="customer_tb"