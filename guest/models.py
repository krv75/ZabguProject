from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='categories/',
    blank = True,
    null = True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class DepartmentInfo(models.Model):
   history = RichTextField()
   learning_activities = RichTextField()
   scientific_activities = RichTextField()
   educational_activities = RichTextField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)

   class Meta:
       verbose_name = "Информация о кафедре"
       verbose_name_plural = "Информация о кафедре"


class ContactData(models.Model):
    address = RichTextField()
    phone = RichTextField()
    email = RichTextField()
    head_department = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Контактные данные"


class TeacherInfo(models.Model):
    full_name = RichTextField()
    profile = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Информация о преподавателях"

    def __str__(self):
        return self.full_name


class News(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=320, unique=True)
    content = RichTextField()
    image = models.ImageField(upload_to='news/', blank=True, null = True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='news')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=True)
    is_pinned = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


