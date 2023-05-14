from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


'''
The code in your message is a Python code. It is a method called save that is defined in a class called NewUserForm. 
The method saves the user’s email address to the database. The commit parameter is used to determine whether the changes 
should be committed to the database or not. If it is set to True, then the changes are committed. If it is set to False, 
then the changes are not committed and the method returns the user object without saving it to the database.'''
