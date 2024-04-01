from django.urls import path

from kda import views

app_name='kda'

urlpatterns =[
    path('<멤버>/',views.show_멤버, name='멤버'),
   # path('ari/',views.show_ari, name='ari'),
   # path('akali/',views.show_akali, name='akali'),
]