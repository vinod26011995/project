from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('signup1/',views.signup1,name='signup1'),
    path('signup2/',views.signup2,name='signup2'),
    path('signin/',views.signin,name='signin'),
    path('signup3/',views.signup3,name='signup3'),
    path('complete/',views.complete,name='complete'),
    path('signin/',views.signin,name='signin')
    
    ]