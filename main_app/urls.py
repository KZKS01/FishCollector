from django.urls import path
from . import views # from the current folder, import views
# contains the view fns that will be associated with each URL pattern

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('fishes/', views.fishes_index, name='fishes_index'),
    path('fishes/<int:fish_id>/', views.fish_detail, name='fish_detail'),
    path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
    path('fishes/create/', views.FishCreate.as_view(), name='fish_create'),
]
