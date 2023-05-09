from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# UserManager class to manage user model
class UserManager(BaseUserManager):
    # Function to create a new user
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have a username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # Function to create a new superuser
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

# User model
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    api_gpt_key = models.CharField(max_length=255, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    # String representation of User object
    def __str__(self):
        return self.username

    # Functions to check user permissions
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Function to check if user is staff
    @property
    def is_staff(self):
        return self.is_admin

# TextAnalysis model
class TextAnalysis(models.Model):
    text = models.TextField()
    mood = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    font_policy = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of TextAnalysis object
    def __str__(self):
        return f"Text: {self.text}, Mood: {self.mood}, Color: {self.color}, Font Policy: {self.font_policy}"