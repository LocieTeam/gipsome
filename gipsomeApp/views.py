from django.shortcuts import render
from rest_framework.parsers import JSONParser
#from .serializers import AddEmployeeSerializer,ItemCheckSerializer,WebViewSerializer,ServeiSerializer,AdsRequestSerializer,DESerializer,AdvertismentSerializer,CR2FSerializer,ItemSerializer,OfferSerializer,OrderSerializer,RateSerializer,UsersSerializer,OTPSerializer,NotifierSerializer,BuissnessSerializer,AdminBaseSerializer,OptionsSerializer
from rest_framework import status
import gipsomeApp.serializers as serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework.response import Response
import psycopg2
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
import gipsomeApp.models as models
#from .models import Servei,AdsRequest,DE,Advertisment,CR2F,Item,Offer,Order,Rate,Rules,Users,OTP,Notifier,Buissness,AdminBase,Options,WebView



# Create your views here.
class ServeiView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    """
        This is View is used for servei and my_employee,
        create, retreive and partial_update
        filter used : servei_id,employer
    """
    queryset = models.Servei.objects.all()
    serializer_class = serializers.ServeiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employer','allowed']
    lookup_field = 'servei_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class AddEmployeeView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    """
      This view will specifically respond to AddEmployee

    """
    queryset = models.Servei.objects.all()
    serializer_class = serializers.AddEmployeeSerializer
    lookup_field = 'servei_id'

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class ItemCheckView(mixins.RetrieveModelMixin,generics.GenericAPIView):


    """
      This View will return data associated with the
      item in the view
      """
    queryset = models.Servei.objects.all()
    serializer_class = serializers.ItemCheckSerializer
    lookup_field = 'servei_id'

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

""" Views for servei ends here
    needed to add auth permissions and login and register power
"""

#####################################################################

"""
   AdsRequest and advertisment view
"""

class AdsRequestView(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = models.AdsRequest.objects.all()
    serializer_class = serializers.AdsRequestSerializer
    filer_backends = [DjangoFilterBackend]
    filterset_fields = ['status','servei_id','city_code']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class AdvertismentView(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset  = models.Advertisment.objects.all()
    serializer_class = serializers.AdvertismentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plan','city_code','servei_id']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

"""
    Advertisment vieew ends here
 """
 #####################################################################

"""
   CR2F view for returning reports,review,feedbacks and concerns
   filterd by servei_id/de_id/order_id and type.
"""
class CR2FView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):

    queryset = models.CR2F.objects.all()
    serializer_class = serializers.CR2FSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['servei_id','item_id','de_id','order_id','type','user_id']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BuissnessReportView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = models.Buissness.objects.all()
    serializer_class = serializers.BuissnessSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['customer_id','status']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class OrderView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field = 'order_id'

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class NotifierView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = models.Notifier.objects.all()
    serializer_class = serializers.NotifierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['note_to','note_from','notify_state']


    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class AdminBaseView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = models.AdminBase.objects.all()
    serializer_class = serializers.AdminBaseSerializer
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class OptionsView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = models.Options.objects.all()
    serializer_class = serializers.OptionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city_code','prev_option']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class WebviewView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = models.WebView.objects.all()
    serializer_class = serializers.WebViewSerializer
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'web_view_id'
    filterset_fields = ['servei_id']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)
@api_view(['GET'])
def callDE(request,longitude,latitude):

    if request.method == 'GET':
        long = float(longitude)
        lat= float(latitude)
        radius = 5.000
        point = Point(long,lat)
        des = models.DE.objects.filter(coordinate_distance_lte = (point,Distance(km=radius)))
        serializer = serializers.DECoord(des,many=True)
        return Response(serializer.data,status=201)
