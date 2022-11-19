from django.urls import path
from .views import *

app_name = "employe"

urlpatterns = [
    path("",HomePage.as_view(),name="home"),
    path('createuser/',register_user,name="create"),
    path('employe/',EmployeList.as_view(),name='list'),
    path('employe_detail/<int:pk>',EmployeDetail.as_view(),name='details'),
    path('employe_update/<int:pk>',EmployeUpdate.as_view(),name='update'),
    path('employe_delete/<int:pk>',EmployeDelete.as_view(),name='delete'),
    path('aboutus/',FeedbackView.as_view(),name='about'),
    path('userhome/',Userview,name='userhome'),
    path('profile',Profileview,name='profile_details'),
    path("feedback_list/",FeedBackList.as_view(),name='feedback_list'),
    path("feedback_detail/<int:pk>",FeedBackDetail.as_view(),name="feedback_detail"),
    path('feedbackadmin',Admin2user.as_view(),name='admin_feedback'),
    path('notification',usernotification,name='usr_note')
       
]