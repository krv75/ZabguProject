from django.shortcuts import render
from student.models import *
from teacher.models import *


def student_menu(request):
    elements = [
        {
            'title': 'Методические материалы',
            'url_name': 'student:methodical-nfo',
        },
        {
            'title': 'Лекции',
            'url_name': 'student:lecture-info',
        },
        {
            'title': 'Библиотеки',
            'url_name': 'student:links'
        },
    ]
    return render(request, 'student_temp/student_menu.html', {'elements': elements})



def methodical_info(request):
    materials = DownloadMethodicalmaterial.objects.all().order_by("-id")
    return render(request, 'student_temp/methodical_material.html', {'materials': materials})


def lecture_info(request):
    materials = DownloadLecture.objects.all().order_by("-id")
    return render(request, 'student_temp/lecture_material.html', {'materials': materials})


def link(request):
    links = LinksLibraries.objects.all()
    return render(request, "student_temp/links.html", {'links': links})

