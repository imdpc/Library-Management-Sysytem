
from django.contrib import admin
from django.urls import path

from libapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('admin_signup/',views.admin_signup,name='admin_signup'),
    path('signup/',views.signup,name='signup'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_book/',views.add_book,name='add_book'),
    path('delete/<rid>',views.delete_book,name='delete_book'),
    path('edit/<rid>',views.edit_book,name='edit_book'),

]
