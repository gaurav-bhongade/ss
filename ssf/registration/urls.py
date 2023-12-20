from django.urls import path
from registration import views
urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'),

    path('save_pipe_details/', views.add_pipe_laying_details, name='save_pipe_details'),
    path('pipe_details_list/', views.pipe_laying_list, name='pipe_details_list'),
    path('update_pipe_record/<int:id>/', views.update_pipe_record, name='update_pipe_record'),


    path('save_site/', views.add_site, name='save_site'),
    path('site_list/', views.site_list, name='site_list'),
]