from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm ,ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required 
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your views here.
def index(request):
	return render(request,'Auth/loginhome.html',{'LoginForm':LoginForm,'RegisterForm':RegisterForm,'ProfileForm':ProfileForm})

def home(request):
	return render(request,'webapp/index.html')


def Login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect(home)
			else:
				message = "username or password is incorrect"
				# raise forms.ValidationError("Invalid username or password")
				return redirect(home)
				return render(request,'Auth/loginhome.html',{'message':message,'LoginForm':LoginForm})
		else:
			message = "Form is not valid"
			return render(request,'Auth/loginhome.html',{'message':message,'LoginForm':LoginForm})
	else:
		return render(request,'Auth/loginhome.html',{'LoginForm':LoginForm,'RegisterForm':RegisterForm,'ProfileForm':ProfileForm})

def Register(request):
	register = 'register'
	if request.method == "POST":
		form1 = RegisterForm(request.POST)
		form2 = ProfileForm(request.POST)
		if form1.is_valid() & form2.is_valid():
			user = form1.save(commit=False)
			user.is_active = False
			username = form1.cleaned_data['username']
			password1 = form1.cleaned_data['password1']
			password2 = form1.cleaned_data['password2']
			profile = form2.save(commit=False)
			if password1 == password2:
				user.set_password(password1)
				user.save()
				new_object=Profile()
				# recent_user = authenticate(username=username,password=password1)
				new_object.user = User.objects.get(username=username)
				new_object.college = form2.cleaned_data['college']
				new_object.mobile = form2.cleaned_data['mobile']
				new_object.city = form2.cleaned_data['city']
				new_object.gender = form2.cleaned_data['gender']
				new_object.save()
				current_site = get_current_site(request)
				mesage = render_to_string('acc_active_email.html', {
					'user':user, 
					'domain':current_site.domain,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': account_activation_token.make_token(user),
				})
				mail_subject = 'Activate your ElanNvision account.'
				to_email = form1.cleaned_data.get('email')
				email = EmailMessage(mail_subject, mesage, to=[to_email])
				email.send()
				message = "Open link in mail to confirm registration"
				return render(request,'elmatrico/index.html',{'message':message})
			else:
				message = "Password dont match"
			return render(request,'Auth/loginhome.html',{'LoginForm':LoginForm,'RegisterForm':RegisterForm,'ProfileForm':ProfileForm,'message':message,'register':register})
		else:
			message = "Form is valid no"
			return render(request,'Auth/loginhome.html',{'LoginForm':LoginForm,'RegisterForm':RegisterForm,'ProfileForm':ProfileForm,'message':message,'register':register})
	else:
		return render(request,'Auth/loginhome.html',{'LoginForm':LoginForm,'RegisterForm':RegisterForm,'ProfileForm':ProfileForm,'register':register})



# def Register(request):
#     if request.method == 'POST':
#         user_form = RegisterForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#         	user = user_form.save(commit=False)
#         	profile = profile_form.save(commit=False)
#         	password1 = user_form.cleaned_data['password1']
#         	password2 = user_form.cleaned_data['password2']
#         	if password1 == password2:
#  				user.set_password(password1)
#  				user.save()
#  				profile.save()
#  				recent_user = authenticate(username=username,password=password1)
#  				login(request,recent_user)
# 				return redirect(home)
            
#         else:
#             return HttpResponse("failed1")
#     else:
#         return HttpResponse("failed2")

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect(home)
    else:
        return HttpResponse('Activation link is invalid!')

