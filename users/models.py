from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    id = models.AutoField(primary_key=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class stkStatus(models.Model):
    devicename = models.CharField(max_length=100)
    createtime = models.DateTimeField()
    x_current = models.FloatField()
    y_current = models.FloatField()
    z_current = models.FloatField()
    x_speed = models.FloatField()
    y_speed = models.FloatField()
    z_speed = models.FloatField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    encodervalue_x = models.FloatField()
    encodervalue_y = models.FloatField()
    encodervalue_z = models.FloatField()
    pin = models.CharField(max_length=50)
    carcode = models.CharField(max_length=50)

    def __str__(self):
        return self.devicename  # 返回设备名称作为对象的字符串表示
