from django.db import models
from django.contrib import admin

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=50)
    date_time= models.DateTimeField(auto_now=True)
    status=models.CharField(blank=True,max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now_add=True)
    valid= models.BooleanField(default=True)


    def getDict(self):
        return {
            'title':self.title,
            'description':self.description,
            'date_time':self.date_time,
            'status':self.status,
            'created':self.created,
            'modified':self.modified,
            'valid': self.valid
        }
# class StatAdmin(admin.ModelAdmin):
#     list_display = ('title', 'discription', 'date_time', 'status', 'created','modified')


