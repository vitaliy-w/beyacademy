from django import forms
from django.db import models

CharLength = 200



## 1) Creating new User
class Student(models.Model):
    messenger = models.CharField(max_length=CharLength)
    token = models.CharField(max_length=CharLength)
    
    #cur_r = models.EmbeddedModelField(model_container=CurRTask, model_form_class=CurRTaskForm)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=CharLength)

    lang = models.CharField(max_length=CharLength)
    edlang = models.CharField(max_length=CharLength)

    chat_id = models.CharField(max_length=200)
    level = models.CharField(max_length=CharLength)


    def __unicode__(self):
        return u'%s %s %s %s' % (self.name, self.lang, self.edlang, self.level)





# 2) Current task of the user
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



#3) update information


#4) create RAnswer



#5) Authentification (login)
#5.1 Login form
class LoginForm(models.Model):
    chat_id = models.CharField(max_length=CharLength)
    messenger = models.CharField(max_length=CharLength)

    def __unicode__(self):
        return u'%s %s' % (self.chat_id, self.messenger)



#5.2 Login get
#from django.contrib.auth import authenticate

#def login(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)



#5.3 Changelang get
#ChangeLang
#-messenger
#-chat_id
#-lang

def changelang(request):
    Student.lang = request.GET['lang']

#ChangeEdLang
#-messenger
#-chat_id
#-lang

def changeedlang(request):
    Student.edlang = request.GET['edlang']

#6) Get basic info (level, lang, edlang)
#BasicInfo
#-level
#-lang
#-edlang


# let's try to list all Student values
# return JSON table about Student
from django.http import JsonResponse

def student_info (request):
    students = Student.objects.all().values() 
    student_list = list(students)
    return JsonResponse(student_list, safe=False)



#7) Add user queries to postman

#7.1 registration form
#7.2 registration querie

#7.3 add JWT

