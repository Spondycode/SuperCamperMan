from django.urls import path
from a_users.views import *

urlpatterns = [
    path('', profile_view, name="profile"),
    path("<username>/", user_profile_view, name="user-profile"),
    path('profile/edit/', profile_edit_view, name="profile-edit"),
    path('onboarding/', profile_edit_view, name="profile-onboarding"),
    path('settings/', profile_settings_view, name="profile-settings"),
    path('emailchange/', profile_emailchange, name="profile-emailchange"),
    path('emailverify/', profile_emailverify, name="profile-emailverify"),
    path('profile/verify-email/', profile_verify_email, name="profile-verify-email"),
    path('delete/', profile_delete_view, name="profile-delete"),
]