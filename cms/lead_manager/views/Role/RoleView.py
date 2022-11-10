from django.views import View
from django.shortcuts import render,redirect

from django.contrib.auth.models import Group

class Role(View):
    def get(self, request):
        role = Group.objects.all() 
        g1 = Group.objects.create(name='member')
        context = {
            'data': Group.objects.all() 
        }
        
        return render(request, 'lead_manager/Role/RoleList.html', context)
        