from django.db import models


class Book(models.Model):
    title = models.CharField('Book name', max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    content = models.TextField('Description', max_length=2000)
    picture = models.ImageField('Book cover', upload_to='pictures/%Y-%m-%d')
    book = models.FileField('Download the book', upload_to='books/%Y-%m-%d')
    time_create = models.DateTimeField('Record creation time', auto_now_add=True)

    def __str__(self):
        return '%s (%s)' % (self.title, self.time_create)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
