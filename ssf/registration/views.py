from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .forms import SignUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from registration.models import *

# Signup View Function
def sign_up(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():
   messages.success(request, 'Account Created Successfully !!') 
   fm.save()
 else: 
  fm = SignUpForm()
 return render(request, 'signup.html', {'form':fm})

# Login View Function
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          return HttpResponseRedirect('/profile/')
    else: 
      fm = AuthenticationForm()
    return render(request, 'userlogin.html', {'form':fm})
  else:
    return HttpResponseRedirect('/profile/')

# Profile
def user_profile(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      fm = EditUserProfileForm(request.POST, instance=request.user)
      if fm.is_valid():
        messages.success(request, 'Profile Updated !!!')
        fm.save()
    else:
      fm = EditUserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'name': request.user, 'form':fm})
  else:
    return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')

# Change Password with old Password
def user_change_pass(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      fm = PasswordChangeForm(user=request.user, data=request.POST)
      if fm.is_valid():
        fm.save()
        update_session_auth_hash(request, fm.user)
        messages.success(request, 'Password Changed Successfully')
        return HttpResponseRedirect('/profile/')
    else:
      fm = PasswordChangeForm(user=request.user)
    return render(request, 'changepass.html', {'form':fm})
  else:
    return HttpResponseRedirect('/login/')
  
def add_pipe_laying_details(request):
    message = ''
    if request.method == "POST":
        formdata = request.POST
        if formdata:
            try:
                pipe = Pipe_Laying.objects.create(
                    label=formdata.get('label'),
                    start_node=formdata.get('start_node'),
                    stop_node=formdata.get('stop_node'),
                    length=formdata.get('length'),
                    diameter_id=formdata.get('diameter_id'),
                    diameter_od=formdata.get('diameter_od'),
                    material=formdata.get('material'),
                    laying_length=formdata.get('laying_length'),
                    balance_laying=formdata.get('balance_laying'),
                )
                message = "Pipe Laying Details Saved successfully...!"
            except Exception as e:
                message = f"Error saving Pipe Laying Details: {str(e)}"
    return render(request, template_name="pipe_laying.html", context={"result": message})

def pipe_laying_list(request):
    pipes = Pipe_Laying.objects.all()
    return render(request, template_name="pipe_laying_list.html", context={'pipes': pipes})
  
def add_site(request):
    message = ''
    if request.method == "POST":
        formdata = request.POST
        if formdata:
            try:
                site = Site.objects.create(
                    name=formdata.get('name'),
                    location=formdata.get('location'),

                )
                message = "Site Details Saved successfully...!"
            except Exception as e:
                message = f"Error saving Site Details: {str(e)}"
    return render(request, template_name="site.html", context={"result": message})

def site_list(request):
    sites = Site.objects.all()
    return render(request, template_name="site_list.html", context={'sites': sites})

def update_pipe_record(request, id):
    message = ''
    pipe = get_object_or_404(Pipe_Laying, id=id)

    if request.method == "POST":
        formdata = request.POST

        try:
            pipe.label = formdata.get('label')
            pipe.start_node = formdata.get('start_node')
            pipe.stop_node = formdata.get('stop_node')
            pipe.length = formdata.get('length')
            pipe.diameter_id = formdata.get('diameter_id')
            pipe.diameter_od = formdata.get('diameter_od')
            pipe.material = formdata.get('material')
            pipe.laying_length = formdata.get('laying_length')
            pipe.balance_laying = formdata.get('balance_laying')

            pipe.save()
            messages.success(request, 'Pipe Laying Record Updated Successfully...!')
            return redirect('pipe_details_list')

        except Exception as e:
            print(f"Error updating Pipe Laying Record: {e}")
            messages.error(request, f'Error Updating Pipe Laying Record: {e}. Please check the data and try again.')

    return render(request, 'pipe_laying.html', context={"result": message, 'pipe': pipe})

