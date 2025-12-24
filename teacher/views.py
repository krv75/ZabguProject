from django.shortcuts import render, redirect
from teacher.models import DownloadMethodicalmaterial, DownloadLecture, MyDocuments, MyMethodicalmaterial


def teacher_menu(request):
    elements = [
        {
            'title': 'Загрузить методический материал',
            'url_name': 'teacher:download_methodical_material',
        },
        {
            'title': 'Загрузить лекцию',
            'url_name': 'teacher:download_lecture',
        },
        {
            'title': 'Мои методические материалы',
            'url_name': 'teacher:my_methodical_material',
        },
        {
            'title': 'Мои документы',
            'url_name': 'teacher:my_documents',
        },
    ]
    return render(request, 'teacher_temp/teacher_menu.html', {'elements': elements})


def download_methodical_material(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        title = request.POST.get('title')
        file = request.FILES.get('file')

        if subject and title and file:
            DownloadMethodicalmaterial.objects.create(
                subject=subject,
                title=title,
                file=file,
            )
            return redirect('teacher:download_methodical_material')

    materials = DownloadMethodicalmaterial.objects.all().order_by('-uploaded_at')
    return render(
        request,
        'teacher_temp/download_methodical_material.html',
        {'materials': materials},
    )


def download_lecture(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        title = request.POST.get('title')
        file = request.FILES.get('file')

        if subject and title and file:
            DownloadLecture.objects.create(
                subject=subject,
                title=title,
                file=file,
            )
            return redirect('teacher:download_lecture')

    lectures = DownloadLecture.objects.all().order_by('-uploaded_at')
    return render(
        request,
        'teacher_temp/download_lecture.html',
        {'lectures': lectures},
    )


def my_methodical_material(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        title = request.POST.get('title')

        if subject and title:
            MyMethodicalmaterial.objects.create(
                subject=subject,
                title=title,
            )
            return redirect('teacher:my_methodical_material')

    materials = MyMethodicalmaterial.objects.all()
    return render(
        request,
        'teacher_temp/my_methodical_material.html',
        {'materials': materials},
    )



def my_documents(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        title = request.POST.get('title')

        if subject and title:
            MyDocuments.objects.create(
                subject=subject,
                title=title,
            )
            return redirect('teacher:my_documents')

    documents = MyDocuments.objects.all()
    return render(
        request,
        'teacher_temp/my_documents.html',
        {'documents': documents},
    )
