from django.urls import path

from django.contrib.auth import views as auth_views
from lead_manager.views import login_views,dashboard_view,logout_view
from lead_manager.views.Role import RoleView
from lead_manager.views.Permission import PermissionView

 
urlpatterns = [
    path('', login_views.login.as_view(), name='Login'),
    path('dashboard/', dashboard_view.Dashboard.as_view(), name='dashboard'),
    path('logout/', logout_view.Logout.as_view(), name='logout'),
    
    path('role/', RoleView.Role.as_view(), name='Role'),
    path('Permission/', PermissionView.Permission.as_view(), name='Role'),
]