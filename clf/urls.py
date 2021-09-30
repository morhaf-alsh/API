
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('predict/',views.predict),
    path('get_clf_info/',views.get_clfinfo),
    path('login_page/',views.login_page),
    path('login/',views.login_user),
]

