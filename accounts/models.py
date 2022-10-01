from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
# Create your models here.

class AccountManager(BaseUserManager):
    """Creates and saves a user with the given details"""
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("The user must provide an email")
        if not username:
            raise ValueError("The user must provide a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """Creates and saves a superuser with the given details"""
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class UserProfile(AbstractBaseUser):
    user =          models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =    models.CharField(max_length=128, null=False)
    last_name =     models.CharField(max_length=128, null=False)
    username =      models.CharField(unique=True, max_length=128, null=False)
    email =         models.EmailField(unique=True, null=False)
    country =       CountryField(max_length=255, null=False, blank=False)
    phone_number =  PhoneNumberField(unique=True, null=False)
    date_joined =   models.DateTimeField(auto_now_add=True)
    last_login =    models.DateTimeField(auto_now=True)
    is_admin =      models.BooleanField(default=False)
    is_staff =      models.BooleanField(default=False)
    is_active =     models.BooleanField(default=True)
    is_superuser =  models.BooleanField(default=False)
    is_worshipper = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Checks if the user has any permissions"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Checks if the user has permission to view the app 'app_label'"""
        return True
    def __str__(self):
        return self.username