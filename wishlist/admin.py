from django.contrib.auth.models import User
# Register your models here.
user = User.objects.create_user('ramyanares', 'ramya.nareswari@ui.ac.id','lollipop31')
user.save()