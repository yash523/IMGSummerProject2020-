from django.db import models

# Create your models here.

class App(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80, blank=False)
    up_for_testing = models.BooleanField(default=False)
    description = models.TextField(max_length=200, blank=True, default='')
    testing_instructions = models.TextField(max_length=500, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='apps_owned', on_delete=models.CASCADE)
    team_members = models.ManyToManyField('auth.User', related_name='apps_member')

class Bug(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=80, blank=False)
    app = models.ForeignKey('App', related_name='bugs', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='bugs_reported', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('auth.User', related_name='bugs_assigned',on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, default='')
    enhance = 'E'
    bug = 'B'
    ui_ux = 'U'
    bug_tags = [
        (enhance,'Enhancement'),
        (bug,'Bug'),
        (ui_ux,'UI/UX'),
    ]
    tag =   models.CharField(choices=bug_tags, default = bug,max_length =1)
    is_resolved = models.BooleanField(default=False)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    bug = models.ForeignKey('Bug', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=False)

class Reply(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='replies', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', related_name='replies', on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=False)

