from django.db import models

# Create your models here.


class Hclass(models.Model):
    class_name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.class_name

class Student(models.Model):

    COLLEDGE = 'CO'
    BACHELOR = 'BA'
    MASTER = 'MA'
    DOCTOR = 'DO'
    OTHER = 'OT'
    EDUCATION_BACKGROUD_CHOICES = (
        (COLLEDGE, 'Colledge'),
        (BACHELOR, 'Bachelor'),
        (MASTER, 'Maser'),
        (DOCTOR, 'Doctor'),
        (OTHER, 'Other'),
    )

    name = models.CharField(max_length=10, null=False)
    whichclass = models.ForeignKey(Hclass, related_name='student', null=False)
    education = models.CharField(max_length=2, choices=EDUCATION_BACKGROUD_CHOICES, default=MASTER, null=False)
    university_company = models.CharField(max_length=40, null=False)
    mobile = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(null=False)
    wechat = models.CharField(max_length=20, null=False)
    dream = models.TextField(max_length=400, null=False)
    want_say = models.TextField(max_length=100, null=False)
    photo = models.ImageField(null=False, upload_to='photos')
    ismonitor = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return u"%s" % self.name



if __name__ == '__main__':
    pass