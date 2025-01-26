# Updated models with validation
from django.core.exceptions import ValidationError

class Post(models.Model):
    title = models.CharField(max_length=200)

    def clean(self):
        if len(self.title) < 5:
            raise ValidationError('Title must be at least 5 characters long.')
