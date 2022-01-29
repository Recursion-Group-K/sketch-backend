from user.models import User
from django.db.models import (
  Model,
  CharField,
  ImageField,
  JSONField,
  BooleanField,
  DateTimeField,
  ForeignKey,
  CASCADE
)

# Create your models here.
class Drawing(Model):
  title = CharField(max_length=128)
  image = ImageField(upload_to='blah', default='path/to/my/default/image.jpg')
  data = JSONField(blank=False)
  is_public = BooleanField(default=False)
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)
  user = ForeignKey(User, default='', on_delete=CASCADE)

  ETCH_A_SKETCH = 'EAS'
  NORMAL = 'NRL'
  DRAWING_MODE_CHOICES = [
    ('EAS', 'Etch A Sketch'),
    ('NRL', 'Normal')
  ]
  mode = CharField(
    max_length=3,
    choices=DRAWING_MODE_CHOICES,
    default=ETCH_A_SKETCH,
  )
