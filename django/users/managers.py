from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, phoneNo, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, phoneNo=phoneNo)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phoneNo, password):
        """ Create a new superuser profile """
        user = self.create_user(email, phoneNo, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
