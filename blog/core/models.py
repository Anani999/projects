from django.db import models

# Create your models here.
class Blogs(models.Model):
    image = models.ImageField(upload_to='blogs-images/',default='blogs-images/default.jpg')
    heading = models.CharField(max_length=200)
    body = models.TextField(null=False)

    def __str__(self):
        return self.heading
    
    def first_two_lines(self):
        return '\n'.join(self.body.splitlines()[:1])
