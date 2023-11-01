from django.shortcuts import render
from django.views import View


class Contact(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'contact.html')


