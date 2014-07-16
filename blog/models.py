from django.db import models
from treebeard.mp_tree import MP_Node

from django.db import models
import datetime  

class Post(models.Model): 
	""" Blog entry """ 
	title = models.CharField(max_length=255) 
	text = models.TextField() 
	added = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return str(self.title)

class Comment(MP_Node): 
	""" Threaded comments for blog posts """ 
	post = models.ForeignKey(Post) 
	author = models.CharField(max_length=60) 
	comment = models.TextField() 
	added = models.DateTimeField(auto_now_add=True) 

	node_order_by = ['added']

	def __unicode__(self):
		return str(self.comment[:100])