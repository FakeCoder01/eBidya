from asyncio import streams
from django.db import models

# Create your models here.

#JEE
class jee(models.Model):

    #CHAPTER
    sub = models.CharField(max_length=16)
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.ImageField(upload_to = 'media')
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()

#NEET
class neet(models.Model):

    #CHAPTER
    sub = models.CharField(max_length=16)
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.CharField(max_length=50)
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()    

#UPSC
class upsc(models.Model):

    #CHAPTER
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.CharField(max_length=50)
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()

#BOARDS
class boards(models.Model):

    #CHAPTER
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.CharField(max_length=50)
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()


#CAT
class cat(models.Model):

    #CHAPTER
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.CharField(max_length=50)
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()


#PSU
class psu(models.Model):

    #CHAPTER
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.CharField(max_length=50)
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()


#PROGRAMMING
class progm(models.Model):

    #CHAPTER
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.CharField(max_length=50)
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()


#OTHERS
class other(models.Model):

    #CHAPTER
    chapter_no = models.IntegerField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    #VIDEO_DETAILS
    video_id = models.CharField(max_length=8)
    video_url = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=8)
    thumbnail = models.CharField(max_length=50)
    assignment_id = models.CharField(max_length=50)

    #RES
    uploaded_by = models.CharField(max_length=50)
    likes = models.IntegerField(max_length=4)
    uploaded_on = models.DateTimeField()


#COMMENTS_TABLE
class comment(models.Model):

    video_id = models.CharField(max_length=8)
    comment_id = models.CharField(max_length=8)
    userid = models.CharField(max_length=8)
    username = models.CharField(max_length=50)
    comment_text = models.TextField()
    created_on = models.DateTimeField()


class assignment(models.Model):
    
    video_id = models.CharField(max_length=8)
    assignment_id = models.CharField(max_length=50)
    assignment_name = models.CharField(max_length=50)
    description = models.TextField()
    userid = models.CharField(max_length=8)
    answer_url = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    created_on = models.DateTimeField()

class test_image_upload(models.Model):
    name = models.CharField(max_length=8)
    image = models.CharField(max_length=64)   

class likes(models.Model):
    
    video_id = models.CharField(max_length=8)
    userid = models.CharField(max_length=8)
    username = models.CharField(max_length=50)