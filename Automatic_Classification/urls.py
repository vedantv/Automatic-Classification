"""Automatic_Classification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from user_profile.views import (login_view,home_page_view,feedback_1,feedback_2,feedback_3,feedback_4,
                                feedback_5,feedback_6,feedback_7,feedback_8,
                                feedback_9,feedback_10,feedback_11,feedback_12,
                                feedback_13,feedback_14,feedback_15,
                                feedback_16,feedback_a,feedback_b,feedback_c,feedback_d,
                                feedback_e,feedback_f,feedback_g,feedback_h,feedback_i,
                                feedback_j,feedback_k,feedback_l,)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_view,name='login'),
    path('feedback-1',feedback_1,name='feedback-1'),
    path('feedback-2/',feedback_2,name='feedback 2'),
    path('feedback-3/',feedback_3,name='feedback_3'),
    path('feedback-4/',feedback_4,name='feedback_4'),
    path('feedback-5/',feedback_5,name='feedback_5'),
    path('feedback-6/',feedback_6,name='feedback_6'),
    path('feedback-7/',feedback_7,name='feedback_7'),
    path('feedback-8/',feedback_8,name='feedback_8'),
    path('feedback-9/',feedback_9,name='feedback_9'),
    path('feedback-10/',feedback_10,name='feedback_10'),
    path('feedback-11/',feedback_11,name='feedback_11'),
    path('feedback-12/',feedback_12,name='feedback_12'),
    path('feedback-13/',feedback_13,name='feedback_13'),
    path('feedback-14/',feedback_14,name='feedback_14'),
    path('feedback-15/',feedback_15,name='feedback_15'),
    path('feedback-16/',feedback_16,name='feedback_16'),
    path('feedback-a/',feedback_a,name='feedback_a'),
    path('feedback-b/',feedback_b,name='feedback_b'),
    path('feedback-c/',feedback_c,name='feedback_c'),
    path('feedback-d/',feedback_d,name='feedback_d'),
    path('feedback-e/',feedback_e,name='feedback_e'),
    path('feedback-f/',feedback_f,name='feedback_f'),
    path('feedback-g/',feedback_g,name='feedback_g'),
    path('feedback-h/',feedback_h,name='feedback_h'),
    path('feedback-i/',feedback_i,name='feedback_i'),
    path('feedback-j/',feedback_j,name='feedback_j'),
    path('feedback-k/',feedback_k,name='feedback_k'),
    path('feedback-l/',feedback_l,name='feedback_l'),
    path('',home_page_view,name='home_page')
    ]

