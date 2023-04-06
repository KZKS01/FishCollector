from django.urls import path
from . import views # from the current folder, import views
# contains the view fns that will be associated with each URL pattern

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fishes/', views.fishes_index, name='fishes_index'),
    path('fishes/<int:fish_id>', views.fishes_detail, name='fishes_detail'),
]
