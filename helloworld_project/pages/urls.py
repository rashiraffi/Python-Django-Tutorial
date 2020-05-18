# pages/urls.py
"""import path from Django to power our URLpattern and on the next line we import our views."""
from django.urls import path
from .views import homePageView
"""By using the period .views we reference the current directory"""

urlpatterns = [
    path('', homePageView, name='home')
]

"""
URLpattern has three parts:
• a Python regular expression for the empty string ''
• specify the view which is called homePageView
• add an optional URL name of 'home'
"""

#if the user requests the homepage, represented by the empty string '' then use the view called homePageView .