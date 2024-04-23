
from django.conf import settings
from .models import Feature

def feature_enabled(id):
    feature = Feature.objects.get(id=id)
    
    if settings.ENVIRONMENT == 'development' or \
        feature.staging_enabled == True and settings.STAGING == 'True' or \
        feature.production_enabled:  # noqa: E712
        feature_enabled = True
    else:
        feature_enabled = False
    
    return feature_enabled
