from django import forms
from django.contrib.auth.models import User

from .models import FoodInformation


class FoodInformationForm(forms.ModelForm):
    class Meta:
        model = FoodInformation
        exclude = ('is_public',)


class UserFoodForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
