from django.shortcuts import render
from django.views import View


class HomeView(View):
    # GET request for index/home
    def get(self, request):
        template = 'index.html'
        return render(request, template)
