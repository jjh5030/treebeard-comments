from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm

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
		comment = Comment(comment=request.POST['comment'], ) 
		form = CommentForm(request.POST)
		if form.is_valid():
			# if this is a reply to a comment, not to a post 
			if form.cleaned_data['parent'] != '': 
				comment.parent = Comment.objects.get(id=request.POST['parent']) 
				comment.post = single_post
				comment.save()
			else:
				comment.post = single_post
				comment.save()

			return HttpResponseRedirect(reverse('single_post', args=(post_id,)))
		else:
			print "INVALID FORM"
	else:
		form = CommentForm()

	# LOAD COMMENTS
	comments = Comment.objects.filter(post=single_post)

	#return render(request, 'post.html', context_dict)
	return render_to_response('post.html', locals(), context_instance=RequestContext(request))	