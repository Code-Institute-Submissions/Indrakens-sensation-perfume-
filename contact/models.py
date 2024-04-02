from django.db import models


class Contact(models.Model):
    """Model for contact form"""
    CHOICES = [
        ('order', 'Order Query'),
        ('general', 'General Query'),
    ]

    email = models.EmailField()
    query = models.CharField(max_length=20, choices=CHOICES, default='query')
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=800)

    def __str__(self):
        return self.email    
