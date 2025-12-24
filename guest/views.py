from django.shortcuts import render, get_object_or_404
from guest.models import Category, DepartmentInfo, ContactData, TeacherInfo, News

def category_list_view(request):
    categories = Category.objects.exclude(title="Новости кафедры")
    news_list = News.objects.order_by('-created_at')

    return render(request, 'guest_temp/guest_home.html', {
        'categories': categories,
        'news_list': news_list,
    })

def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    department_info = DepartmentInfo.objects.filter(category=category).first()
    contact_data = ContactData.objects.filter(category=category).first()
    teachers = TeacherInfo.objects.filter(category=category)

    context = {
        'category': category,
        'department_info': department_info,
        'contact_data': contact_data,
        'teachers': teachers,
    }
    return render(request, 'guest_temp/info_for_guest.html', context)

def news_detail_view(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'guest_temp/news_detail.html', {'news': news})

