from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user']
#         widgets = {
#             'image': forms.FileInput(),
#             'displayname' : forms.TextInput(attrs={'placeholder': 'Add display name'}),
#             'info' : forms.Textarea(attrs={'rows':3, 'placeholder': 'Add information'})
#         }
        
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user", "level", "plot_reports", "numplots", "email", "created"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "displayname" : forms.TextInput(attrs={"placeholder": "Add Displayname"}),
            "info" : forms.Textarea(attrs={"rows":3, "placeholder": "Add Information about you..."}),
            "campermode" : forms.Select(attrs={"class": "form-control"}),
            "camperstory" : forms.Textarea(attrs={"rows":3, "placeholder": "Add your Camping Experience..."}),
            "nationality" : forms.TextInput(attrs={"placeholder": "Add Nationality"}),
            "fav_campsite" : forms.TextInput(attrs={"placeholder": "Add Favourite Campsite"}),
            "realname" : forms.TextInput(attrs={"placeholder": "Add Real Name"}),
        }
        labels = {
            "realname": "Name",
            "campermode": 'Tent or Camper?',
            "camperstory": "Your Camping Experience",
        }
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']