from django import forms
# from django.contrib.auth.models import User

from users.models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["profile_photo","first_name", "last_name", "username", "email", "password", "is_staff", "is_active"]
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        # self.fields["profile_photo"].widget.attrs.update({"style":"display:none;"})
        # self.fields['current_profile_photo'] = forms.ImageField(required=False)
        self.fields["is_active"].widget.attrs.update({"class":""})
        self.fields["is_staff"].widget.attrs.update({"class":""})

        if self.instance and self.instance.pk:
            # If the instance exists and has a profile photo, add the URL to the form
            self.fields['current_profile_photo'] = forms.CharField(
                required=False, widget=forms.HiddenInput(), initial=self.instance.profile_photo.url if self.instance.profile_photo else ''
            )
    
    def clean(self):
        cleaned_data = super().clean()
        profile_photo = cleaned_data.get('profile_photo')
        if not profile_photo:
            cleaned_data['profile_photo'] = self.instance.profile_photo
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user