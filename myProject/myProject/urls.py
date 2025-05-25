
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('student/', student_view, name='student'),
    path('student/create/', student_create, name='student_create'),
    path('student/<int:id>/', student_detail, name='student_view'),
    path('student/<int:id>/edit/', student_edit, name='student_edit'),
    path('student/<int:id>/delete/', student_delete, name='student_delete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)