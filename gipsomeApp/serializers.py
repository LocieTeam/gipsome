from rest_framework import serializers
from .models import Servei,AdsRequest,DE,Advertisment,CR2F,Item,Offer,Order,Rate,Rules,Users,OTP,Notifier,Buissness,AdminBase,Options,WebView


class ServeiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servei
        fields = ('aadhar','country_code','web_pays','name','address','allowed','body_type','city_code','credit','email','employer','firm_name','image','coordinate','phone_number','pin_code','service_type','status','tin','pan','floating_money','servei_id','servei_state','rating',)


"""
    Few Serializer classes for making prevented lookup
"""

 #For Add_Employee which only calls servei_id,aadhar,address,image and name
class AddEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model= Servei
        fields = ('servei_id','aadhar','image','name','address','employer_name','body_type',)

# This class will return data when customer will look for items cateogerywise,so it will be easy to fit into pices
class ItemCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model=Servei
        fields=('rating','servei_id','firm_name','name','coordinate','address',)

#login serializer for taking only servei_id and hashed_password ,emails and aadharno.
class ServeiLogin(serializers.ModelSerializer):
    class Meta:
        model = Servei
        fields = ('servei_id','password','email','aadhar',)


class AdsRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdsRequest
        fields = ('city_code','image','plan','servei_id','status',)

class DESerializer(serializers.ModelSerializer):

    class Meta:
        model = DE
        fields = ('web_pays','rating','aadhar','address','city_code','email','insurance_detail','name','pan','pin_code','password','credit','phone_number','coordinate','vehicle_id','driving_license','vehicle_type')

class AdvertismentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisment
        fields = ('city_code','image','last_settelment','coordinate','plan','servei_id','start_time',)
class CR2FSerializer(serializers.ModelSerializer):

    class Meta:
        model = CR2F
        fields = ('item_id','de_id','order_id','servei_id','type','rating_de','rating_servei','remark_de','remark_servei','user_id',)
class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model= Item
        fields = ('rating','city_code','coordinate','cost','effective_cost','father_option','image','item_description','item_id','item_name','measure','offer_id','prev_option','servei_id',)
class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('city_code','offer_id','item_ids','offer','offer_detail','offer_tag','servei_id',)
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields=('user_id','user_address','user_coordinates','order_status','cart','order_id','item_list','city_code','cost_markup','cost','effective_cost_markup','effective_cost','payment_mode','payment_status','payment_to_servei','servei_id','de_id','user_id','time',)

class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ('city_code','ad_rate','run_rate','sector_rate',)

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields=('city_code','address','email','name','password','phone_number','credit','coordinate','user_id',)

class RulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rules
        fields = ('city_code','measure','tile_dimen',)

class NotifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifier
        fields = ('note_to','note_from','content','image','response','time','notify_state',)

class OTPSerializer(serializers.ModelSerializer):

    class Meta:

        model = OTP
        fields = ('to','otp','time','status',)

class BuissnessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buissness
        fields = ('status','customer_id','outstanding','instanding','sales','income','instanding_list','outstanding_list','time',)

class AdminBaseSerializer(serializers.ModelSerializer):

    class Meta:

        model = AdminBase
        fields = ('name','id','password','city_code','post','child_post',)

class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = ('name','city_code','prev_option','next_option','service_type','delivery_type',)

class WebViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebView
        fields = '__all__'

class DeCoord(serializers.ModelSerializer):
    class Meta:
        model = DE
        fields = ('de_id','coordinate',)




#################################################################################
###################################################################################
