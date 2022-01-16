from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Ссылка: https://www.mantto.com.pe/nosotros/
# Для этой ссылки сделаем только одну модель с изображениями для динамической их замены 
# текст весь вытащим в HTML или во views.py, так как он статичный и нет смысла занимать бд

class nosotros_images(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Пользователь, добавивший изображение')
    title = models.CharField(max_length=200)
    images = models.ImageField(verbose_name="Изображения о нас", upload_to = "images/about_us/", blank=True)
    
    class Meta:
        verbose_name = "О Нас"
        verbose_name_plural = "О Нас"

    def __str__(self):
        return self.title


# Ссылка: https://www.mantto.com.pe/lineas-de-negocio-gerenciamiento-y-gestion-integral-de-proyectos/
# Для этой ссылки сделаем только одну модель с изображениями для динамической их замены 
# текст весь вытащим в HTML или во views.py, так как он статичный и нет смысла занимать бд

class Business_Direction_images(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Пользователь, добавивший изображение')
    title = models.CharField(max_length=200)
    images = models.ImageField(verbose_name="Изображения о направлений", upload_to = "images/business_direction/", blank=True)
    
    class Meta:
        verbose_name = "Направления"
        verbose_name_plural = "Направления"

    def __str__(self):
        return self.title
    



# Ссылка: https://www.mantto.com.pe/sectores/
class Sectors_Category(models.Model):
    sectors_name = models.CharField(verbose_name="Название сектора", max_length=100)
    img = models.ImageField(verbose_name="Иконка сектора", upload_to="images/sectors_icons")

    class Meta:
        verbose_name = "Категории Секторов"
        verbose_name_plural = "Категории Секторов"
    
    def __str__(self):
        return self.sectors_name


# Ссылка: https://www.mantto.com.pe/sectores/edificaciones-urbanas/
class Sectors(models.Model):
    name = models.CharField(verbose_name="Название сектора", max_length=125)
    category = models.ForeignKey(Sectors_Category, on_delete=models.CASCADE, verbose_name="Категория")
    client = models.CharField(verbose_name="Клиент", max_length=50)
    location = models.CharField(verbose_name="Место положения", max_length=150)
    year = models.IntegerField(verbose_name='Год')
    price = models.CharField(verbose_name="Цена", max_length=40)
    image = models.ImageField(verbose_name="фото", upload_to="images/sectors_images")

    class Meta:
        verbose_name = "Сектора"
        verbose_name_plural = "Сектора"

    def __str__(self):
        return f'{self.name}, {self.category}'

class Category(models.Model):
    
    name = models.CharField(max_length=100,unique=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

# Ссылка: https://www.mantto.com.pe/laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado/
class Blog_Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=225, verbose_name="Заголовок поста", blank=True)
    img = models.ImageField(verbose_name="Фото поста", upload_to="images/blog_images")
    text = models.TextField(verbose_name="Текст поста", max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)
    
    class Meta:
        ordering = ('title',)
        verbose_name = "Блог"
        verbose_name_plural = "Блог"

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Blog_Page, self).save(*args, **kwargs)


# Ссылка: https://www.mantto.com.pe/laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado/
class TegPost(models.Model):
    """Теги постов"""
    post = models.ForeignKey(Blog_Page, on_delete=models.CASCADE, verbose_name="Пост")
    teg = models.CharField(max_length=225, verbose_name="Тег")

    def __str__(self):
        return self.teg


# Ссылка: https://www.mantto.com.pe/laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado/
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    post = models.ForeignKey(Blog_Page, on_delete=models.PROTECT)
    comment = models.CharField(max_length=5000)

    def __str__(self):
        return self.comment

# Ссылка: https://www.mantto.com.pe/sectores/obras/
class SocialResponsibilityCategories(models.Model):
    """Категории Социальной Ответственности"""
    # КАК ПУНКТЫ ВСПЛЫВАЮЩЕГО МЕНЮ
    name = models.CharField(max_length=225, verbose_name="Наимкнование катнгории")

    def __str__(self):
        return self.name


# Ссылка: https://www.mantto.com.pe/sectores/obras/
class SocialResponsibility(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Пользователь, добавивший изображение')
    title = models.CharField(max_length=200)
    images = models.ImageField(verbose_name="Изображения о наших работах", upload_to = "images/works/", blank=True)
    
    class Meta:
        verbose_name = "Наши работы"
        verbose_name_plural = "Наши работы"

    def __str__(self):
        return self.title


# Ссылка: https://www.mantto.com.pe/contacto/
class FeedbackForm(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    position = models.CharField(max_length=125, verbose_name="Должность")
    business = models.CharField(max_length=125, verbose_name="Бизнес")
    phone = models.CharField(max_length=17, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")
    text = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Форма обратной связи"

    def __str__(self):
        return self.name