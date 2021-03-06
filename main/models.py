from statistics import mode
from django.db import models
import uuid


# Course
class Course(models.Model):
    course_name = models.CharField('Course name', max_length=255)
    course_details = models.TextField('Details')
    duration = models.CharField('Course Duration', default="1", max_length=255)
    courseType = models.CharField('CourseType', default="0", max_length=255)
    image = models.ImageField('Choose image main (format: jpg, jpeg, png)', upload_to='img/%y/%m/%d/')

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['-id']


# Teacher
class Teacher(models.Model):
    teacher_name = models.CharField('Teacher name', max_length=255)
    about = models.TextField('About')
    image = models.ImageField('Choose image main (format: jpg, jpeg, png)', upload_to='img/%y/%m/%d/')

    def __str__(self):
        return self.teacher_name

    class Meta:
        ordering = ['-id']


# Faq
class Faq(models.Model):
    question = models.CharField('Question', max_length=255)
    answer = models.CharField('Answer', max_length=655)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-id']


# Photo
class Photo(models.Model):
    photo = models.ImageField('Choose image main (format: jpg, jpeg, png)', upload_to='img/%y/%m/%d/')

    def __str__(self):
        return f'Photo {self.photo}'

    class Meta:
        ordering = ['-id']


# Contact
class Contact(models.Model):
    name = models.CharField('Name', max_length=255)
    surname = models.CharField('Surname', max_length=255)
    phone = models.CharField('Phone', max_length=255)
    phone2 = models.CharField('Phone2', max_length=255)
    message = models.TextField('Message')
    created_at = models.DateTimeField('Time', auto_now_add=True)
    is_pinned = models.BooleanField('Pin', default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


# Settings
class Settings(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tiktok = models.CharField('@Tiktok', max_length=255)
    instagram = models.CharField('@Instagram', max_length=255)
    telegram = models.CharField('@Telegram', max_length=255)

    def __str__(self):
        return self.email

