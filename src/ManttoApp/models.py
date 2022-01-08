from django.db import models

from django.contrib.auth.models import User


# Create your models here:
# Ссылка: https://www.mantto.com.pe/nosotros/
class AboutUs(models.Model):
    """Модель Онас"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = models.TextField(verbose_name="Текст Онас")

    def __str__(self):
        return self.title


# Ссылка: https://www.mantto.com.pe/nosotros/
class ImgAboutUs(models.Model):
    """Фото О нас"""
    about_as = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name="img_about_as",
                                 verbose_name="О нас (pk)")
    img = models.ImageField(upload_to="about_as", verbose_name="Фото")

    def __str__(self):
        return str(self.about_as)


# Ссылка: https://www.mantto.com.pe/nosotros/
class Strategy(models.Model):
    """Модель Стратегии"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = models.TextField(verbose_name="Текст стратегии")
    file = models.FileField(upload_to="strategy_file", verbose_name="файл")

    def __str__(self):
        return self.text


# Ссылка: https://www.mantto.com.pe/nosotros/
class Mission(models.Model):
    """Модель Миссий"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = models.TextField(verbose_name="Текст миссии")

    def __str__(self):
        return self.text


# Ссылка: https://www.mantto.com.pe/nosotros/
class View(models.Model):
    """Модель Вида"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = models.TextField(verbose_name="Текст стратегии")

    def __str__(self):
        return self.text


# Ссылка: https://www.mantto.com.pe/nosotros/
class Values(models.Model):
    """Модель Ценностей"""
    img = models.ImageField(upload_to="values_img")
    title = models.CharField(verbose_name="Заголовок", max_length=100)

    def __str__(self):
        return self.img


# Ссылка: https://www.mantto.com.pe/lineas-de-negocio-gerenciamiento-y-gestion-integral-de-proyectos/
class BusinessDirectionCategory(models.Model):
    """Категории Деловых направлении"""
    # Наименования пунктов всплывающего меню
    name = models.CharField(verbose_name="Наименование", max_length=80)

    def __str__(self):
        return self.name


# Ссылка: https://www.mantto.com.pe/lineas-de-negocio-gerenciamiento-y-gestion-integral-de-proyectos/
class BusinessDirection(models.Model):
    """Деловое направление"""
    category = models.ForeignKey(BusinessDirectionCategory, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.category.name


# Ссылка: https://www.mantto.com.pe/lineas-de-negocio-gerenciamiento-y-gestion-integral-de-proyectos/
class ImgBusinessDirection(models.Model):
    """Фото делового напревление"""
    business = models.ForeignKey(BusinessDirection, on_delete=models.CASCADE, verbose_name="Бизнес напровление")
    img = models.ImageField(upload_to="img_business")
    text = models.TextField(verbose_name="текст")

    def __str__(self):
        return self.business


# Ссылка: https://www.mantto.com.pe/sectores/
class SectorsCategory(models.Model):
    """Категории сектора"""
    name = models.CharField(verbose_name="Наименование сектора", max_length=40)
    img = models.ImageField(verbose_name="Иконка сектора", upload_to="sectors_img")

    def __str__(self):
        return self.name


# Ссылка: https://www.mantto.com.pe/sectores/edificaciones-urbanas/
class Sectors(models.Model):
    """Секторы"""
    name = models.CharField(verbose_name="Наименование", max_length=125)
    category = models.ForeignKey(SectorsCategory, on_delete=models.CASCADE, verbose_name="Категория")
    client = models.CharField(verbose_name="Клиент", max_length=50)
    location = models.CharField(verbose_name="Место положение", max_length=150)
    year = models.IntegerField(verbose_name='Год')
    price = models.CharField(verbose_name="Цена", max_length=40)

    ### !!! НУЖЕН NAME ИЗ SectorsCategory !!!
    ### Это поле с наименованием category УЖЕ ИМЕЕТСЯ В ЭТОМ КЛАССЕ

    def __str__(self):
        return self.name


# Ссылка: https://www.mantto.com.pe/sectores/edificaciones-urbanas/
class ImgSectors(models.Model):
    """Фото Секторов"""
    sectors = models.ForeignKey(Sectors, verbose_name="Сектор", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name="фото", upload_to="sectors_img")

    def __str__(self):
        return self.sectors.name


# Ссылка: https://www.mantto.com.pe/laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado/
class Post(models.Model):
    """Блок Постов"""
    """кода будешь делать пользователя то тут нужно его добавить"""
    # user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=225, verbose_name="Зголовок")
    img = models.ImageField(verbose_name="Фото поста", upload_to="post_img")
    text = models.TextField(verbose_name="Текст поста")
    # Ссылка к видеоролику:
    url = models.URLField(verbose_name="Ссылка на видео")

    def __str__(self):
        return self.title


# Ссылка: https://www.mantto.com.pe/laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado/
class TegPost(models.Model):
    """Теги постов"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    teg = models.CharField(max_length=225, verbose_name="Тег")

    def __str__(self):
        return self.teg


# Ссылка: https://www.mantto.com.pe/laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado/
class CommentPost(models.Model):
    """Каментарии поста"""
    """кода будешь делать пользователя то тут нужно его добавить"""
    text = models.TextField(verbose_name="Текст")
    name = models.CharField(verbose_name="Имя", max_length=50)
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(max_length=12, verbose_name="Телефон")

    def __str__(self):
        return self.name


# Ссылка: https://www.mantto.com.pe/sectores/obras/
class SocialResponsibilityCategories(models.Model):
    """Категории Социальной Ответственности"""
    # КАК ПУНКТЫ ВСПЛЫВАЮЩЕГО МЕНЮ
    name = models.CharField(max_length=225, verbose_name="Наимкнование катнгории")

    def __str__(self):
        return self.name


# Ссылка: https://www.mantto.com.pe/sectores/obras/
class SocialResponsibility(models.Model):
    """Социальной Ответственности"""
    categories = models.ForeignKey(SocialResponsibilityCategories, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=125, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.title


# Ссылка: https://www.mantto.com.pe/sectores/obras/
class ImgSocialScene(models.Model):
    """Социальной Ответственности фото"""
    social_scene = models.ForeignKey(SocialResponsibility, verbose_name="Социальной Ответственность",
                                     on_delete=models.CASCADE)
    img = models.ImageField(verbose_name="Фото", upload_to="social_img")


# Ссылка: https://www.mantto.com.pe/certificaciones/
class Certificate(models.Model):
    """модкль Сертификвты"""
    title = models.CharField(max_length=70, verbose_name="заголовок сертификата")
    img = models.ImageField(verbose_name="Фото", upload_to="certificate_img")

    def __str__(self):
        return self.title


# Ссылка: https://www.mantto.com.pe/contacto/
class Contacts(models.Model):
    """модель контактов"""
    direction = models.CharField(max_length=225, verbose_name="Напровление")
    phone = models.CharField(max_length=225, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")

    def __str__(self):
        return self.direction


# Ссылка: https://www.mantto.com.pe/contacto/
class FeedbackForm(models.Model):
    """модель ФОРМА ОБРАТНОЙ СВЯЗИ"""
    name = models.CharField(max_length=50, verbose_name="Полное имя")
    position = models.CharField(max_length=125, verbose_name="Должность")
    business = models.CharField(max_length=125, verbose_name="Бизнес")
    phone = models.CharField(max_length=17, verbose_name="Телефон")
    email = models.EmailField(verbose_name="почта")
    text = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return self.name
