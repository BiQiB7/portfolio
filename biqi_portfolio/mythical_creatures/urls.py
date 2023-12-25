from django.urls import path
from .views import DragonProjectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('mythical_creatures/', DragonProjectView.as_view(),name='mythical_creatures')
]