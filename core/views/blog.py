from django.shortcuts import render
from django.views import View


class Blog(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'blog.html')
