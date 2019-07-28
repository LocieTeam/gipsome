from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField,JSONField
from django.db import connection
from django.contrib.gis.geos import Point





#Basic user authentication model

# Create your models here.
class Servei(models.Model):
    servei_id = models.CharField(default='',max_length=14,db_index= True)
    aadhar = models.CharField(max_length =12,default='')
    country_code = models.CharField(max_length=5,default='+91')
    coordinate = models.PointField(max_length=40,null=True)
    web_pays = JSONField(default=dict,blank=True)
    name = models.CharField(max_length=30,default='')
    address = models.TextField(default='')
    allowed = models.BooleanField(default=True)
    body_type = models.CharField(max_length = 2,default='I')
    city_code = models.CharField(max_length=8,default='')
    credit = models.DecimalField(max_digits=10,decimal_places=3,default=0)
    password = models.CharField(max_length=255,default='')
    email = models.EmailField(default='')
    employer = models.CharField(max_length=15,blank=True,default='')
    firm_name = models.CharField(default='',max_length = 255,blank = True)
    image = models.CharField(max_length= 255,default='',blank=True)
    phone_number = models.CharField(max_length=15,default='')
    pin_code = models.CharField(max_length=10,default='')
    service_type = models.CharField(max_length=4,default='')
    status = models.BooleanField(default=True)
    tin = models.CharField(max_length=255,default='')
    pan = models.CharField(max_length=255,default='')
    floating_money = models.DecimalField(default=0,max_digits=8,decimal_places=3)
    servei_state = models.CharField(primary_key=True,max_length=10,default='online')
    rating = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)



class AdsRequest(models.Model):
    city_code = models.CharField(max_length=8,default='')
    date = models.DateTimeField(default='')
    image = models.CharField(max_length=255,default='')
    plan = models.CharField(max_length=10,default='')
    servei_id = models.CharField(max_length=14,default='')
    status = models.CharField(max_length=20,default='requested')


class DE(models.Model):

    de_id = models.CharField(primary_key=True,max_length=14,db_index= True,default='')
    aadhar = models.CharField(max_length =12,default='')
    coordinate = models.PointField(max_length=40,null=True)
    country_code = models.CharField(max_length=5,default='+91')
    name = models.CharField(max_length=30,default='')
    web_pays = JSONField(default=dict)
    address = models.TextField(default='')
    allowed = models.BooleanField(default=True)
    city_code = models.CharField(max_length=8,default='')
    credit = models.DecimalField(default=0,max_digits=10,decimal_places=3)
    floating_money = models.DecimalField(default=0,max_digits=8,decimal_places=3)
    password = models.CharField(max_length=255,default='')
    email = models.EmailField(default='')
    image = models.CharField(max_length= 255,default='')
    phone_number = models.CharField(max_length=15,default='')
    pin_code = models.CharField(max_length=10,default='')
    vehicle_id = models.CharField(max_length=30,default='')
    vehicle = models.CharField(max_length=30,default='')
    driving_license = models.CharField(max_length=30,default='')
    status = models.BooleanField(default=True)
    rc= models.CharField(max_length=255,default='')
    pan = models.CharField(max_length=255,default='')

    insurance_detail = models.CharField(max_length=30,default='')
    rating = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)

class Advertisment(models.Model):
    id = models.CharField(max_length=255,primary_key=True,default='')
    coordinate = models.PointField(max_length=40,null=True)
    city_code = models.CharField(default='',max_length=8)
    plan = models.CharField(max_length=10,default='')
    image = models.CharField(max_length=255,default='')
    servei_id = models.CharField(max_length=14,default='')
    start_time = models.DateTimeField(default='')
    last_settelment = models.DateTimeField(default='')

class CR2F(models.Model):
    de_id = models.CharField(max_length=14,default='')
    item_id = models.CharField(max_length=35,default='')
    order_id= models.CharField(max_length=35,default='')
    servei_id = models.CharField(max_length=14,default='')
    rating_de = models.DecimalField(max_digits=4,decimal_places=3,default=0)
    rating_servei = models.DecimalField(max_digits=4,decimal_places=3,default=0)
    remark_de =models.TextField(default='')
    remark_servei = models.TextField(default='')
    user_id = models.CharField(max_length=14,default='')
    type = models.CharField(max_length=10,default='')

class Item(models.Model):
    city_code = models.CharField(max_length=8,default='')
    cost = models.DecimalField(max_digits=7,decimal_places=3,default=0)
    effective_cost = models.DecimalField(max_digits=7,decimal_places=3,default=0)
    father_option = models.CharField(max_length=15,default='')
    image = models.CharField(max_length=255,default='')
    item_name = models.CharField(max_length=30,default='')
    item_description = models.TextField(default='')
    measure = models.CharField(max_length=8,default='')
    offer_id = models.CharField(max_length=35,default='')
    prev_option = models.CharField(max_length=30,default='')
    servei_id = models.CharField(max_length=14,default='')
    rating = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    item_id = models.CharField(max_length=35,primary_key=True,default='')

class Offer(models.Model):
    offer_id = models.CharField(default='',max_length=35,primary_key=True)
    city_code = models.CharField(max_length=8,default='')
    item_ids =ArrayField(models.CharField(max_length=35),default=list,null=True)
    offer = models.DecimalField(max_digits=6,decimal_places=3,default=0)
    offer_detail = models.TextField(default='')
    offer_tag = models.CharField(max_length=255,default='')
    servei_id = models.CharField(max_length=14,default='')

class Order(models.Model):
    order_id = models.CharField(max_length=35,primary_key=True,default='')
    item_list = ArrayField(models.CharField(max_length=35),default=list,null=True)
    cart = JSONField(default=dict)
    city_code = models.CharField(max_length=8,default='')
    cost_markup = JSONField(default=dict)
    cost = models.DecimalField(max_digits=7,decimal_places=3,default=0)
    effective_cost_markup = JSONField(default=dict)
    effective_cost = models.DecimalField(max_digits=7,decimal_places=3,default=0)
    payment_mode = models.CharField(max_length=30,default='')
    payment_status = models.CharField(max_length=30,default='')
    user_id = models.CharField(max_length=15,default='')
    user_address = models.CharField(max_length=75,default='')
    payment_to_servei = JSONField(default=dict)
    servei_id = models.CharField(max_length=14,default='')
    de_id = models.CharField(max_length=30,default='')
    time = models.DateTimeField(default='')
    user_id = models.CharField(max_length=14,default='')
    order_status = models.CharField(max_length=10,default='')

class Rate(models.Model):
    city_code = models.CharField(max_length=8,primary_key=True,default='')
    ad_rate = JSONField(default=dict)
    run_rate = models.CharField(max_length=10,default='/hrs')
    sector_rate = JSONField(default=dict)

class Users(models.Model):
    city_code = models.CharField(max_length=8,default='')
    user_id = models.CharField(primary_key=True,max_length=15,default='',db_index=True)
    country_code = models.CharField(max_length=5,default='+91')
    coordinate = ArrayField(models.CharField(max_length=10),size=2,default=list)
    phone_number = models.CharField(max_length=10,default='',null=True)
    email = models.EmailField(default = '',null=True)
    name = models.CharField(max_length=30,default='',null=True)
    address = models.TextField(default='')
    image = models.CharField(max_length=255,default='')
    coordinate = models.PointField(max_length=40,null=True)
    credit = models.DecimalField(max_digits=8,decimal_places=3,default=0)



class Rules(models.Model):
    city_code = JSONField(default=dict)
    measure = ArrayField(models.CharField(max_length=20),default=list,null=True)
    tile_dimen = JSONField(default=dict)

class Notifier(models.Model):
    note_from = models.CharField(max_length=35,default='')
    note_to = models.CharField(max_length=35,default='')
    content = models.CharField(max_length=60,default='')
    image = models.CharField(max_length=255,default='')
    response = models.CharField(max_length=30,default='')
    time = models.DateTimeField(default='')
    notify_state = models.CharField(max_length=10,default='')

class OTP(models.Model):
    to = models.CharField(max_length=35,default='')
    otp = models.CharField(max_length=8,default='')
    status = models.CharField(max_length=20,default='')
    time = models.DateTimeField(default='')

class Buissness(models.Model):
    id = models.AutoField(primary_key=True,default='')
    customer_id = models.CharField(max_length=14,blank=True,default='')
    outstanding = models.DecimalField(default=0,max_digits=8,decimal_places=3,blank=True)
    instanding = models.DecimalField(default=0,max_digits=8,decimal_places=3,blank=True)
    outstanding_list = JSONField(default=dict)
    instanding_list = JSONField(default=dict)
    income = models.DecimalField(default=0,max_digits=8,decimal_places=3,blank=True)
    sales = models.DecimalField(default=0,max_digits=8,decimal_places=3,blank=True)
    status = models.CharField(max_length=15,default='')
    time = models.DateTimeField(default='')

class AdminBase(models.Model):
    city_code = models.CharField(max_length=8,default='')
    admin_id = models.CharField(primary_key=True,max_length=20,db_index=True,default='')
    image = models.CharField(max_length=255,default='')
    post = models.CharField(max_length=20,default='')
    child_post = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=30,default='',null=True)


class Options(models.Model):
    name = models.CharField(max_length=30,default='')
    prev_option = models.CharField(max_length=30,default='')
    next_option = models.CharField(max_length=30,default='')
    city_code = ArrayField(models.CharField(max_length=10),default=list,null=True)
    servei_type = models.CharField(max_length=4,default='')
    delivery_type = models.CharField(max_length=5,blank=True,default='')

class WebView(models.Model):
    web_view_id = models.CharField(max_length=30,primary_key=True,default='')
    para = JSONField(default=dict)
    images = JSONField(default=dict)
    contact = JSONField(default=dict)
    video = JSONField(default=dict)
    headings = JSONField(default=dict)
    servei_id = models.CharField(max_length=14,default='')
