from django.urls import path,include
from . import views
from .views import blogHomeView, blogDetailsView, ArticlesView, newsletterView



urlpatterns = [



    path('', views.home , name='home'),
    path('requestappointment/',views.requestappointment, name='requestappointment'),
    path('patientcare/', views.patientcare, name='patientcare'),
    # path('blog/',views.blog, name='blog'),
    path('blog/',blogHomeView.as_view(), name='blog'),
    path('blog/articles',ArticlesView.as_view(), name='articles'),
    path('blog/articles/<int:pk>',blogDetailsView.as_view(), name='blog_details'),
    path('newsletter/', views.newsletterView, name='newsletter'),
    path('aboutus/',views.aboutus, name='aboutus'),
]
