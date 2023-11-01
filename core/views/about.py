from django.shortcuts import render
from django.views import View


class About(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'about.html')

