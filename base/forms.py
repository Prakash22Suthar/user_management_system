from django import forms
# from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(
                    widget=forms.PasswordInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Password',
                    }
                ))

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser #User
        fields = ["profile_photo", "username", "email", "password"]
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={"style":"display:none;"}),
            'username':forms.TextInput(attrs={'placeholder':"Select a UserName", "class":"form-control"}),
            'email':forms.EmailInput(attrs={'placeholder':"Enter an Email", "class":"form-control"}),
            'password':forms.TextInput(attrs={'placeholder':"Create a Password", "class":"form-control"}),
            # 'is_staff':forms.CheckboxInput(attrs={'placeholder':"Select"}),
            # 'is_active':forms.CheckboxInput(attrs={'placeholder':"Select"}),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user