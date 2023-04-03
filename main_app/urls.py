from django.urls import path
from . import views # from the current folder, import views
# contains the view fns that will be associated with each URL pattern

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('fishes/', views.home, name='fishes_index'),
    path('fishes/<int:fish_id>', views.home, name='fishes_detail'),
]
