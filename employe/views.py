from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView)
from .forms import *
from django.http import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
import time
# Create your views here.


# def time_convert(sec):
#   mins = sec // 60
#   sec = sec % 60
#   hours = mins // 60
#   mins = mins % 60
#   time.sleep(2)
#   start_time = time.time()

#   input("press enter to end")
#   end_time = time.time()

#   time_lapsed = end_time - start_time

#   return ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


  
class HomePage(TemplateView):
    template_name = "index.html"

def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'qrcode' in request.FILES:
                profile.qrcode = request.FILES['qrcode']
            profile.save()
            return redirect('employe:home')

        else:
            return HttpResponse(user_form.errors,profile_form.errors)


    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()
    return render(request,'create.html',{
        'user_form':user_form,
        "profile_form":profile_form
    })

class EmployeList(ListView):
    context_object_name = 'employe_list'
    model = UserProfile
    template_name = 'list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employe_list'] = UserProfile.objects.all()
        return context
# def  Employe_list(request):
#     model = UserProfile.objects.all()
#     return render(request,"list,html",{'employe_list':model})
class EmployeDetail(DetailView):
    context_object_name = 'employe_detail'
    model = UserProfile
    template_name = 'detail.html'


class EmployeUpdate(UpdateView):
    context_object_name = "employe_update"
    model = UserProfile
    fields = '__all__'
    success_url  = reverse_lazy("employe:list")
    template_name = "update.html"



class EmployeDelete(DeleteView):
    model = UserProfile
    success_url = reverse_lazy("employe:list")
    template_name = "delete.html"
    


@login_required()
def Userview(request):
    # print(time_convert(0))
    return render(request,'userhome.html')

@login_required()
def Profileview(request):
    db = UserProfile.objects.filter(user_id=request.user.id)
    return render(request,'profile.html',{'db':db})
        

class FeedbackView(CreateView):
    model = FeedBack
    fields =  ('name','role','comments')
    success_url = reverse_lazy("employe:home")
    template_name = "UsertoAdmin.html"


class Aboutus(CreateView):
    model=Commanfeedback
    fields=('name','role','comments')
    success_url=reverse_lazy("employe:about")
    template_name="aboutus.html"

class commanfeedbacklist(ListView):
    context_object_name='commanfeedback_list'
    model=Commanfeedback
    template_name='commanfeedbacklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commanfeedback_list'] = Commanfeedback.objects.all()
        return context

class commanfeedbackdetail(DetailView):
    context_object_name = 'feedback_detail'
    model = Commanfeedback
    template_name = 'commandfeedbackdetail.html'


class FeedBackList(ListView):
    context_object_name = 'feedback_list'
    model = FeedBack
    template_name = 'feedbacklist.html'


class FeedBackDetail(DetailView):
    context_object_name = 'feedback_detail'
    model = FeedBack
    template_name = 'feedbackdetail.html'

class Admin2user(CreateView):   # admin to user feedback
    model = AdmintoUser
    fields = ('user','comments')
    success_url = reverse_lazy('employe:feedback_list')
    template_name = 'adminfeedback.html'

def usernotification(request):
    user = AdmintoUser.objects.filter(user=request.user)
    return render(request,'notification.html',{'note':user})
import datetime

def signout(request):
    logout(request)
    return redirect("employe:home")

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
     user.userprofile.logout_time = datetime.datetime.now()
     user.userprofile.save()