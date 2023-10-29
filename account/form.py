from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from account.models import User


class RegisterForm(forms.Form):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'شماره تلفن'}) , validators=[validators.MaxLengthValidator(11)])
    is_bus_driver = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'  , 'placeholder':' ثبت نام به عنوان راننده ی اتوبوس'}))
    is_realestate = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input' , 'placeholder':' ثبت نام به عنوان املاک دار'}))
    is_simple_user = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input' , 'placeholder':' ثبت نام به عنوان کاربر ساده'}))

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone)<11:
            raise ValidationError("This Information is not correct")
        return phone

class OtpForm(forms.Form):
    code = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder':'کد ارسال شده :'}) , validators=[validators.MaxLengthValidator(4)])
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox , required = True)
    def clean_code(self):
        code = self.cleaned_data.get("code")
        if len(code)<4:
            raise ValidationError("this code is invalid")
        return code

class Edite_Profile_Form(forms.ModelForm):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'شماره تلفن'}) , validators=[validators.MaxLengthValidator(11)] , required=False)
    class Meta:
        model=User
        fields=['Full_name', 'username' , 'email' , 'phone']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام کاربری'}),
            'Full_name' :forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام و نام خانوادگی'}),
            'email' :forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'ایمیل'}),
        }