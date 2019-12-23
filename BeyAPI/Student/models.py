from django import forms
from django.forms import models


class CurRTask(models.Model):
    #task = m.M(RepeatTask)
    #audio_url = models.CharField()
    #date = DateTimeField(default=datetime.utcnow(), required=True)

    class Meta:
        abstract = True

class CurRTaskForm(forms.ModelForm):
    pass
       #class Meta:
       #     model = CurRTask
       #     fields = (
       #         'audio_url'#, 'task'
       #     )

#class CurTask(m.Model):
    #task = ReferenceField(Task)
    #answer = StringField()
    #translate = StringField()
    #audio_url = StringField()
    #date = DateTimeField(default=datetime.utcnow(), required=True)

class Student(models.Model):
    messenger = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    
    #cur_r = models.EmbeddedModelField(model_container=CurRTask, model_form_class=CurRTaskForm)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    lang = models.CharField(max_length=200)
    edlang = models.CharField(max_length=200)

    chat_id = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
