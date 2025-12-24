from django.urls import path
from .views import category_list_view, category_detail_view, news_detail_view

app_name = 'guest'

urlpatterns = [
    path('', category_list_view, name='guest_category_list'),
    path('category/<int:pk>/', category_detail_view, name='guest_category_detail'),
    path("news/<int:pk>/",news_detail_view, name="news_detail"),
]
