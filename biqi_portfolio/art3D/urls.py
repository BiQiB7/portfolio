from django.urls import path
from .views import Art3DView
from django.conf.urls.static import static


urlpatterns = [
    path('art3D/', Art3DView.as_view(),name='art3D')
]