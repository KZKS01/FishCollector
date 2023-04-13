from django.urls import path
from . import views # from the current folder, import views
# contains the view fns that will be associated with each URL pattern

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    # fishes
    path('fishes/', views.fishes_index, name='fishes_index'),
    path('fishes/<int:fish_id>/', views.fish_detail, name='fish_detail'),
    path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
    path('fishes/add/', views.FishAdd.as_view(), name='fish_add'),
    path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
    # tanks
    path('tanks/', views.tanks_index, name='tanks_index'),
    path('tanks/add/', views.TankAdd.as_view(), name='tank_add'),
    path('tanks/<int:pk>/update/', views.TankUpdate.as_view(), name='tank_update'),
    path('tanks/<int:pk>/delete/', views.TankDelete.as_view(), name='tank_delete'),
]
