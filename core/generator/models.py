from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name
    
class Quote(models.Model):
    quote = models.CharField(max_length=123)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        words = self.quote.split()
        return ''.join(words[:5])
    
    
