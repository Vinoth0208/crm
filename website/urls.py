from django.urls import path

from website import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('Customer/<int:pk>',views.customer_record, name='Customer'),
    path('delete_record/<int:pk>',views.delete_record, name='delete_record'),
    path('add_customer/',views.add_customer, name='add_customer'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]
