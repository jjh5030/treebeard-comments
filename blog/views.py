from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm

import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect, get_object_or_404, RequestContext

def home(request):
	last_posts = Post.objects.all().order_by('-added')[:3]
	context_dict = {'last_posts': last_posts}
	return render(request, 'home.html', context_dict)

def single_post(request, post_id):

	single_post = get_object_or_404(Post, pk=post_id)

	if request.method == "POST":
		#save comment
		form = CommentForm(request.POST)
		if form.is_valid():
			parent = form['parent'].value()

			if parent == '' or parent is None:
				# reply to root
				root = Comment.add_root(post=single_post,
									    author='',
									    comment=form.cleaned_data['comment'],
									    added=datetime.datetime.now())
			else:
				# reply to comment
				get = lambda node_id: Comment.objects.get(pk=parent)
				node = get(parent).add_child(post=single_post,
											 author='',
											 comment=form.cleaned_data['comment'],
											 added=datetime.datetime.now())

			return HttpResponseRedirect(reverse('single_post', args=(post_id,)))
		else:
			print "INVALID FORM"
	else:
		form = CommentForm()

	# LOAD COMMENTS
	comment_tree = Comment.objects.filter(post=single_post)

	#return render(request, 'post.html', context_dict)
	return render_to_response('post.html', locals(), context_instance=RequestContext(request))	