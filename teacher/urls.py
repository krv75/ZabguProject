from django.urls import path
from teacher.views import  teacher_menu, download_lecture, download_methodical_material, my_methodical_material, my_documents


app_name = 'teacher'

urlpatterns = [
    path('teacher_menu/', teacher_menu, name='teacher_menu'),
    path('download-lecture/', download_lecture, name='download_lecture'),
    path('download-methodical/', download_methodical_material, name='download_methodical_material'),
    path('my-methodical/', my_methodical_material, name='my_methodical_material'),
    path('my-documents/', my_documents, name='my_documents'),
]
