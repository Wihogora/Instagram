from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment, Follow, Unfollow, Likes
from . forms import ProfileUploadForm,CommentForm,ProfileForm
from django.http  import HttpResponse
from django.conf import settings


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title = 'Instagram'
    image_posts = Image.objects.all()
    # comments = Comment.objects.all()

    print(image_posts)
    return render(request, 'index.html', {"title":title,"image_posts":image_posts})


@login_required(login_url='/accounts/login/')
def comment(request,id):
	
	post = get_object_or_404(Image,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.image = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request,'comment.html',{"form":form})  


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    follower = Follow.objects.filter(user = profile)

    return render(request, 'profile.html',{"current_user":current_user,"profile":profile,"follower":follower})

@login_required(login_url='/accounts/login/')
def timeline(request):
	current_user = request.user 
	Myprofile = Profile.objects.order_by('-time_uploaded')
	comment = Comment.objects.order_by('-time_comment')
	

	return render(request, 'my-inst/timeline.html',{"Myprofile":Myprofile,"comment":comment})

@login_required(login_url='/accounts/login/')
def single_image(request,image_id):
	image = image.objects.get(id= image_id)

	return render(request, 'my-inst/single_image.html',{"image":image})


@login_required(login_url='/accounts/login/')
def like(request,image_id):
	Image = Image.objects.get(id=image_id)
	like +=1
	save_like()
	return redirect(timeline)
