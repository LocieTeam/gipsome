from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gipsomeApp import views

urlpatterns = [
        path('servei/<str:servei_id>/',views.ServeiView.as_view()),
        path('employee/<str:servei_id>/',views.AddEmployeeView.as_view()),
        path('itemServei/<str:servei_id>/',views.ItemCheckView.as_view()),
        path('adsRequest/',views.AdsRequestView.as_view()),
        path('advertisment/',views.AdvertismentView.as_view()),
        path('cr2f/',views.CR2FView.as_view()),
        path('buissnessReport/',views.BuissnessReportView.as_view()),
        path('order/<str:order_id>/',views.OrderView.as_view()),
        path('notifier/',views.NotifierView.as_view()),
        path('adminBase/<str:id>/',views.AdminBaseView.as_view()),
        path('options/',views.OptionsView.as_view()),
        path('webView/<str:web_view_id>/',views.WebviewView.as_view()),
        path('callde/<str:longitude>/<str:latitude>/',views.callDE),



]

urlpatterns = format_suffix_patterns(urlpatterns)
