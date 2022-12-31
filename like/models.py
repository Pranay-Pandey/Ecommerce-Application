from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_item = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_body = GenericForeignKey(ct_field="liked_item")
