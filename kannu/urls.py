from django.contrib import admin
from django.urls import path
from kannu import views
urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("BS/",views.BS,name="BHAGAT SINGH"),
    path("MG/",views.MG,name="mahatama gandhi"),
    path("BGT/",views.BGT,name="Bal Gangadgar Tilak "),
    path("RLB/",views.RLB,name="rnai laxmi bai"),
    path("SCB/",views.SCB,name="subhash chandra bose"),
    path("SVP/",views.SVP,name="sardar vallabbhai patel"),
    path("LBS/",views.LBS,name="lal bahadur shastri"),
    path("MP/",views.MP,name="mangal pandey"),
]
