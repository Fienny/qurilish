from django.core.files.storage import FileSystemStorage
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


fs = FileSystemStorage(location="/media/directors")


class Director(models.Model):
    DAYS = (
        ('Du', 'DUSHANBA'),
        ('SE', 'SESHANBA'),
        ("CHO", 'CHORSHANBA'),
        ('JU', 'JUMA'),
        ('SHA', 'SHANBA'),
        ('YA', 'YAKSHANBA'),
    )

    image = models.ImageField(storage=fs)
    job_title = models.CharField(max_length=128, null=False)
    full_name = models.CharField(max_length=256, null=False)
    days = models.CharField(max_length=3, choices=DAYS, blank=False)
    tel_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.full_name


class Notification(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    date = models.DateField(auto_now_add=True, null=False)
    text = models.TextField(null=False, blank=False, default="Default text")

    def __str__(self):
        return self.title


class New(models.Model):
    date = models.DateField(auto_now_add=True, null=False, blank=False)
    title = models.CharField(max_length=256, blank=False, null=False)
    subtitle = models.TextField(null=False, blank=False, default="Default text")
    text = models.TextField(null=False, blank=False, default="Default text")
    image = models.ImageField(storage=fs)

    def __str__(self):
        return self.title


class System(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.title


class Subsystem(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    system = models.ForeignKey(System, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Article(models.Model):
    code = models.CharField(max_length=256, blank=False, null=False)
    title = models.CharField(max_length=256, blank=False, null=False)
    subtitle = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(null=False, blank=False, default="Default text")
    subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=256, null=False)
    date = models.DateField(auto_now_add=True, null=False, blank=False)
    likes = models.IntegerField(blank=True, null=False, default=0)
    dislikes = models.IntegerField(blank=True, null=False, default=0)
    text = models.TextField(null=False, blank=False, default="Default text")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.dislikes += 1
        self.save()

    def __str__(self):
        return self.name


class About(models.Model):
    text = models.TextField(null=False, blank=False, default="Default text")
    image = models.ImageField(storage=fs)

    def __str__(self):
        return "About page"
