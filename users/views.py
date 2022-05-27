from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import View
from .forms import RegisterForm, AccountAuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse

# def register(request, *args, **kwargs):
#     if request.method=='GET':
#         form = RegisterForm()
#         form2 = AccountAuthenticationForm()
#         context={'form':form,'login_form':form2}
#         return render(request,'join.html',context)

#     if request.method=='POST':
#         print('Inside Post Request')
#         # Checking if post request is coming from registration page
#         if request.POST.get('submit')=='sign_up':
#             user = request.user
#             print('User: ',user)
#             if user.is_authenticated:
#                 print('USer is authenticated')
#                 return HttpResponse("You are already authenticated as " + str(user.email))

#             context = {}
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 print('Valid form')
#                 form.save()
#                 email = form.cleaned_data.get('email').lower()
#                 raw_password = form.cleaned_data.get('password1')
#                 account = authenticate(email=email, password=raw_password)
#                 if account is not None:
#                     login(request, account)
#                     return redirect('account_page')
#             else:
#                 print('Invalid Form. Errors: ',form.errors)
#                 context['form'] = form
#                 return render(request,'join.html',context)


#         # Checking if post request is coming from login page
#         elif request.POST.get('submit') == 'sign_in':
#             context2 = {}
#             user = request.user
#             if user.is_authenticated:
#                 print('USer is authenticated')
#                 return redirect("account_page")
            
#             form = AccountAuthenticationForm(request.POST)
#             print('Form:  ',form)
#             print(' ')
#             if form.is_valid():
#                 print('Valid form')
#                 email = request.POST['email_check']
#                 password = request.POST['password_check']
#                 user = authenticate(email=email, password=password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect("account_page")
#             else:
#                 print('Invalid Form. Errors: ',form.errors)
#                 context2['login_form'] = form
#                 return render(request,'join.html',context2)
               
                    
class RegisterView(View):
    template_name = 'join.html'

    def get(self, request):
        form = RegisterForm()
        form2 = AccountAuthenticationForm()
        context={
            'form':form,
            'login_form':form2
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # Checking if post request is coming from registration page
        if request.POST.get('submit')=='sign_up':
            user = request.user
            if user.is_authenticated:
                print('USer is authenticated')
                return HttpResponse("You are already authenticated as " + str(user.email))

            context = {}
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email').lower()
                raw_password = form.cleaned_data.get('password1')
                account = authenticate(email=email, password=raw_password)
                if account is not None:
                    login(request, account)
                    return redirect('account_page')
            else:
                context['form'] = form
                return render(request, self.template_name, context)


        # Checking if post request is coming from login page
        elif request.POST.get('submit') == 'sign_in':
            context2 = {}
            user = request.user
            if user.is_authenticated:
                return redirect("account_page")
            
            form = AccountAuthenticationForm(request.POST)
            # if form.is_valid():
            email = request.POST['email_check']
            password = request.POST['password_check']
            if email and password:
                user = authenticate(request, email=email, password=password, backend='django.contrib.auth.backends.ModelBackend')
                if user is not None:
                    try:
                        user.backend = 'django.contrib.auth.backends.ModelBackend'
                        login(request, user)
                    except Exception as exc:
                        print('Login failed!. Error: ',exc)
                        return HttpResponse('Login failed!. Error: ')
                    return redirect("account_page")

                else:
                    context2['login_form'] = form
                    return render(request, self.template_name, context2)
            else:
                context2['login_form'] = form
                return render(request, self.template_name, context2)


# def register2(request,*args, **kwargs):
#     if request.method=='GET':
#         form=RegisterForm()
#         form2 = AccountAuthenticationForm()
#         context={'form':form,'login_form':form2}
#         return render(request,'join.html',context)

#     if request.method=='POST':
#         if request.POST.get('submit')=='sign_up':
#             form=RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 email = form.cleaned_data.get('email').lower()
#                 raw_password = form.cleaned_data.get('password1')
#                 account = authenticate(email=email, password=raw_password)
#                 if account is not  None:
#                     login(request, account,backend='django.contrib.auth.backends.ModelBackend')
#                     return redirect('account_page')
#             else:
#                 messages.error(request,'Error Processing your request')
#                 context={'form':form}
#                 return render(request,'join.html', context)

#         elif request.POST.get('submit') == 'sign_in':
            
#             context={}
#             user = request.user
#             if user.is_authenticated: 
#                 return redirect("account_page")

#             form = AccountAuthenticationForm(request.POST)
#             # if form.is_valid():
#             email = request.POST['email_check']
#             password = request.POST['password_check']
#             print('Email: ',email)
#             print('Password', password)
#             if email and password:
#                 user = authenticate(email=email, password=password)
#                 if user is not None:
#                     login(request, user,backend='django.contrib.auth.backends.ModelBackend')
#                     return redirect("account_page")
#             else:
#                 context['login_form'] = form
#                 return render(request, "join.html", context)

#     #return render(request, 'join.html',{})



def logout_view(request):
	logout(request)
	return redirect("home_page")

