from django.urls import path
from . import views
urlpatterns=[
    path('',views.hello),
    path('add/', views.add_event, name='add_event'),
    path('display/', views.display_events, name='display_events'),
    path('image/', views.image, name='image_page'),  # Adjust the URL path as needed
]
