from django.urls import path,re_path
from . import views
from .views import predictImage

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('patient/', views.patientHomeView , name='patient'),
    # path('predictImage',views.predictImage,name='predictImage'),
        ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
