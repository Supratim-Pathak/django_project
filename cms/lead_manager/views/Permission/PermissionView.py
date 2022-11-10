from django.views import View
from django.shortcuts import render,redirect


class Permission(View):
    def get(self, request):
        return render(request, 'lead_manager/Permission/Permission.html')
        