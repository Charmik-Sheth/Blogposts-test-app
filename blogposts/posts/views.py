from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, User
from django.utils import timezone
from django.core.urlresolvers import reverse

def index(request, user_id):
	try:
		if(request.session['user_id']==int(user_id)):
			#print "in if"
			post_list = Post.objects.order_by('pub_date')
			return render(request, 'posts/index.html', {'post_list': post_list, 'user_id': user_id})
		else:
			#print "in else"
			return render(request, 'posts/login_page.html', {})

	except (KeyError):
		return render(request, 'posts/login_page.html', {})

def comment(request, post_id, user_id):
	try:
		if(request.session['user_id']==int(user_id)):
			post = get_object_or_404(Post, pk=post_id)
			return render(request, 'posts/comment.html', {'post': post, 'user_id': user_id})

		else:
			return render(request, 'posts/login_page.html', {})

	except (KeyError):
		return render(request, 'posts/login_page.html', {})

def new_post(request, user_id):
	try:
		if(request.session['user_id']==int(user_id)):	
			post_text = request.POST['post']
			if (post_text != "Post Something...") and (post_text != ""):
				new_post = Post(post_text=post_text, pub_date=timezone.now())
				new_post.save()

			return HttpResponseRedirect(reverse('posts:index', args=(user_id,)))

		else:
			return render(request, 'posts/login_page.html', {})

	except (KeyError):
		return render(request, 'posts/login_page.html', {})

def new_comment(request, post_id, user_id):
	try:
		if(request.session['user_id']==int(user_id)):
			post = Post.objects.get(pk=post_id)
			comment_text = request.POST['comment']
			if (comment_text != "Write your comment here...") and (comment_text != ""):
				post.comment_set.create(comment_text=comment_text, pub_date=timezone.now())

			return HttpResponseRedirect(reverse('posts:comment', args=(post.id, user_id,)))

		else:
			return render(request, 'posts/login_page.html', {})

	except (KeyError):
		return render(request, 'posts/login_page.html', {})

def login_page(request):
	#print "i am here"
	return render(request, 'posts/login_page.html', {})

def new_login(request):
	#print "I am here"
	username = request.POST['username']
	password = request.POST['password']
	try:
		user = User.objects.get(user_name=username)
		if (user.password == request.POST['password']):
			request.session['user_id'] = user.id
			request.session.set_expiry(1200)
			return HttpResponseRedirect(reverse('posts:index', args=(user.id,)))
		else:
			return render(request, 'posts/login_page.html', {'error_message': "Your password is incorrect."})
	
	except (User.DoesNotExist):
		return render(request, 'posts/login_page.html', {'error_message': "Your username is incorrect."})


def logout(request, user_id):
	try:
		del request.session['user_id']
		return render(request, 'posts/login_page.html', {})
	except (KeyError):
		return render(request, 'posts/login_page.html', {})


