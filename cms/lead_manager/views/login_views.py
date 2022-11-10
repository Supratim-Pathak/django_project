from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView
from lead_manager.Forms.login_auth import LoginForm
# Create your views here.
from django.contrib.auth.models import User

class login(LoginView):
    template_name = "lead_manager/Auth/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user=True
    
    # PASS EXTRA CONTEXT
    
    # all_users = User.objects.values()
    # print(all_users)
    # print(all_users[0]['email'])  
    # extra_context = {'data_1':all_users[0]['email'],'data_2':'tong..'}
        