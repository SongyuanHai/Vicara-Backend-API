from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from datetime import date
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, employeeID, first_name, last_name, role, level, email, password=None):
        """Creates a new user profile."""

        if not employeeID:
            raise ValueError('Users must have an employeeID.')
        
        if not first_name:
            raise ValueError('Users must have a first_name.')
        
        if not last_name:
            raise ValueError('Users must have a last_name.')
        
        if not role:
            raise ValueError('Users must have a role')
        
        if not level:
            raise ValueError('Users must have a level')
        
        if not email:
            raise ValueError('Users must have an email address.')
                                             
        email = self.normalize_email(email)
        user = self.model(employeeID=employeeID, first_name=first_name, last_name=last_name, role=role, level=level, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, employeeID, first_name, last_name, role, level, email, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(employeeID, first_name, last_name, role, level, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a "user profile" inside our system. Stores all user account
    related data, such as 'email address' and 'name'.
    """
    employeeID = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['employeeID','first_name','last_name','role','level']

    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.first_name, self.last_name

    def get_short_name(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.first_name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.email
    
    
class TimeSheet(models.Model):
    """User timesheet create"""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    employeeID = models.CharField(max_length = 128, unique = True)
    name = models.CharField(max_length = 128)
    location = models.CharField(max_length = 128)
    project_code = models.CharField(max_length=128)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    break_hour = models.TimeField()
    work_hour = models.TimeField()
    approval_status = models.CharField(max_length=128)
    description = models.CharField(max_length = 255)

    def __str__(self):
        """Return the model as a string."""

        return self.name


