from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.post_list, name='post_list'),
    path('signup/', views.signup, name='signup'),
    path('class_details/', views.class_details, name='class_details'),
    path('instructor_details/', views.instructor_details, name='instructor_details'),
    path('hotclass_details/', views.hotclass_details, name='hotclass_details'),
    path('yoga_details/', views.yoga_details, name='yoga_details'),
    path('oneday_class_details/', views.oneday_class_details, name='oneday_class_details'),
    path('pilates_details/', views.pilates_details, name='pilates_details'),
    path('view_on_map/', views.view_on_map, name='view_on_map'),

]
