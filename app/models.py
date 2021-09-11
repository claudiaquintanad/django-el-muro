from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['first_name']) < 2:
            errors['firstname_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if len(postData['last_name']) < 2:
            errors['lastname_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        if not SOLO_LETRAS.match(postData['first_name']):
            errors['solo_letras'] = "solo letras en nombreporfavor"
        
        if not SOLO_LETRAS.match(postData['last_name']):
            errors['solo_letras'] = "solo letras en nombreporfavor"

        if len(postData['password']) < 4:
            errors['password'] = "contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        
        return errors

class MessageManager(models.Manager):
        pass

class CommentManager(models.Manager):
        pass

class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=1002, null=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Message(models.Model):
    message = models.TextField()
    user_id = models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return f"{self.message}"

class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name="messages", on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, related_name="users2", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __str__(self):
        return f"{self.comment}"

    def __repr__(self):
        return f"{self.comment}"