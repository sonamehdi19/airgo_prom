from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import Account

class RegisterForm(UserCreationForm):

    email=forms.EmailField(max_length=100,
                           required=True,
                           help_text='Enter Email Address',
                           widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                           )

    
    phone_number=forms.CharField(max_length=50, required=True, help_text='Enter Phone number', 
                            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
                            )


    identity_id=forms.CharField(max_length=200, required=True, help_text='Enter Identity ID',widget=forms.TextInput(attrs={'class':'form-control',
                            'placeholder':'Identity ID'}),
                            )

    class Meta:
        model = Account
        fields = ('username','email', 'password1','password2','phone_number','identity_id', )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'required': 'true'})
        self.fields['password'].widget.attrs.update({'required': 'true'})

    class Meta:
        model = Account
        fields = ('email', 'password')

	# def clean(self):
	# 	if self.is_valid():
	# 		email = self.cleaned_data['email_check']
	# 		password = self.cleaned_data['password_check']
	# 		if not authenticate(email=email, password=password):
	# 			raise forms.ValidationError("Invalid login")
