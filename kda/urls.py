from django.urls import path

from kda import views

app_name='kda'

urlpatterns =[
    path('ari/',views.show_ari, name='ari'),
    path('akali/',views.show_akali, name='ari'),
]