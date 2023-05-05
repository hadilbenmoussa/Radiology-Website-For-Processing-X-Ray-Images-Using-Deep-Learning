from django.urls import path,include
from . import views
from .views import blogHomeView, blogDetailsView, ArticlesView, newsletterView,newsletterfooterView,writetestimonial



urlpatterns = [



    path('', views.home , name='home'),
    path('writetestimonial/',views.writetestimonial, name='writetestimonial'),
    path('patientcare/', views.patientcare, name='patientcare'),
    # path('blog/',views.blog, name='blog'),
    path('blog/',blogHomeView.as_view(), name='blog'),
    path('blog/articles',ArticlesView.as_view(), name='articles'),
    path('blog/articles/<int:pk>',blogDetailsView.as_view(), name='blog_details'),
    path('newsletter/', views.newsletterView, name='newsletter'),
    path('footer/', views.newsletterfooterView, name='footer'),

    path('aboutus/',views.aboutus, name='aboutus'),
]
