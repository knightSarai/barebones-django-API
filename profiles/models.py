from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """MAnager for user profile"""
    """django password needs to be hashed, so it will not set until the user provide a falid password"""
    def create_user(self, email, name, password=None):
        """ Create new user profile"""
        if not email:
            raise ValueError('User must have an Email address')
        email = self.normalize_email(email)
        # create a model object and set the email and the name
        user = self.model(email = email,  name = name)
        user.set_password(password)
        # if there multiple databases in future 
        user.save(using = self._db)
    
        return user

    def create_superuser(self, email, name, password):
        """Create a super user """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField( max_length= 254, unique= True)
    name = models.CharField(max_length= 50)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    

    # Allow to control users from django command tool
    objects = UserProfileManager()

    #overwrite the default user name
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def __str__(self):
        """class string represintation"""
        return self.email