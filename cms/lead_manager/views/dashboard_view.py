from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = 'lead_manager/AppPages/dashboard.html'
    