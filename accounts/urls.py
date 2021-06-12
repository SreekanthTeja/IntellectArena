from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.register,name = 'signup'),
    path('login',views.signin,name = 'signin'),
    path('logout/',views.logout_request,name='signout'),
    path('date',views.store_date,name = 'date'),
    path('appointment',views.AppointmentView.as_view(), name = 'appointment'),
]