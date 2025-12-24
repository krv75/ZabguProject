from  django.urls import path
from student.views import methodical_info,lecture_info, student_menu, link

app_name = 'student'


urlpatterns = [
    path('student-memu/', student_menu, name='student-menu'),
    path('methodical-info/', methodical_info, name='methodical-nfo'),
    path('lecture-info/', lecture_info, name='lecture-info'),
    path('links/', link, name='links'),

]