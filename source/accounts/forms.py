from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, strip=False)
    email = forms.EmailField(label="Email Address", required=True)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        return password_confirm

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('Email already registered.', code='email_registered')
        except User.DoesNotExist:
            return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise forms.ValidationError('Fill out either First Name or Last Name!')
        return first_name

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserChangePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=100, required=True, label='New Password',
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='New Password confirm',
                                       widget=forms.PasswordInput)
    old_password = forms.CharField(max_length=100, required=True, label='Old Password',
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invalid password.', code='invalid_password')
        return old_password

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match.', code='passwords_do_not_match')
        return self.cleaned_data

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']