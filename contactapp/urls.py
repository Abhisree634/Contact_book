from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('accounts/login/', views.loginview, name="login"),
    path('logout',views.logout_view),
    path('reset',views.resethome,name='reset'),
    path('resetpwd',views.resetpassword,name='resetpassword'),
    path("add",views.addcontact),
    path("display",views.display),
    path("dlt",views.dltcontact),
    # # path('delete/<int:eid>',views.dltemployee),
    path("update",views.updatecontact), 
    path("updt",views.updatecontactno),
     path("search",views.search)
     
   
  

]
