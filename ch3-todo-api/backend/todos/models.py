from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

# Luồng công việc : initial setup => startproject và startapp = > edit todos/models =>  migrate => edit todos/admin => runserver =>  pip djangorestframework => edit config/setting => edit config url => config todos/url => edit todo/serializer => edit todos/views => runserver => config/setting