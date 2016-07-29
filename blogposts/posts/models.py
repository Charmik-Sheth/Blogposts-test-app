from django.db import models


class User(models.Model):
	user_name = models.CharField(max_length=26)
	password = models.CharField(max_length=26)

	def __unicode__(self):
		return self.user_name


class Post(models.Model):
	#user = models.ForeignKey(User)
	post_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.post_text


class Comment(models.Model):
	#user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	comment_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.comment_text

