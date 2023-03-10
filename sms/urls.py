"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from schoolwork.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="homepage"),
    path("apply/",applyForAdmission,name="apply"),
    path("accounts/login/",login,name="login"),
    path("accounts/logout/",logout,name="logout"),
    path("manage/student",manageStudents,name="manageStudent"),
    path("manage/admission",manageAdmission,name="manageAdmission"),
    path("manage/student/<int:id>/delete/",deleteStudent,name="deleteStudent"),
    path("manage/student/<int:id>/edit/",editStudent,name="editStudent"),
    path("manage/student/<int:id>/view/",viewStudent,name="viewStudent"),
    path("manage/classes/<int:id>/delete/",deleteClasses,name="deleteclasses"),
    path("manage/student/<int:id>/approve/",approve,name="approve"),
    path("manage/classes",manageClasses,name="manageClasses"),
    path("manage/classes/view-class/<className>/",viewClassWise,name="viewclasswise"),
    path("manage/student/scan",scanRFcode,name="scanRFcode"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


