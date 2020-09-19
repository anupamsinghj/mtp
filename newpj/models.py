from django.db import models
from django.core.files.storage import FileSystemStorage
#from app.storage import OverwriteStorage
# Create your models here.

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    csv = models.FileField(upload_to='file/csv/')#,storage=OverwriteStorage())
    #cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

class uploadf(models.Model):
    title = models.CharField(max_length=100)
    csv = models.FileField(upload_to='file')#,storage=OverwriteStorage())

    def __str__(self):
        return self.title
