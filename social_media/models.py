from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
        username = models.CharField(default='User',max_length=40)
        profile_pic = models.ImageField(upload_to = "profile/",null=True)
        bio = models.TextField(default='',blank = True)
        first_name = models.CharField(max_length =40)
        last_name = models.CharField(max_length =40)


        def __str__(self):
            return self.username

        def delete_profile(self):
            self.delete()

        def save_profile(self):
            self.save()

        @classmethod
        def search_profile(cls,search_term):
            got_profiles = cls.objects.filter(first_name__icontains = search_term)
            return got_profiles



class Image(models.Model):
    image = models.ImageField(upload_to = "images/",null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)
    image_name = models.CharField(max_length = 40,null = True)
    
    image_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
    	return self.image_name

    def delete_image(self):
    	self.delete()

    def save_image(self):
    	self.save()

    def update_caption(self,new_caption):
    	self.image_caption = new_caption
    	self.save()

    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos

    @classmethod
    def get_images_by_user(cls,id):
        sent_images = Image.objects.filter(user_id=id)
        return sent_images

    @classmethod
    def get_images_by_id(cls,id):
        fetched_image = Image.objects.get(id = id)
        return  fetched_image

    class Meta:
    	ordering = ['-pub_date']


    
    def save_profile(self):
    	self.save()



class Comment(models.Model):
        user = models.ForeignKey(User,on_delete = models.CASCADE, null= True)
        image = models.ForeignKey(Image,on_delete = models.CASCADE, null= True,related_name='comment')
        comment= models.TextField( blank=True)
        
        def __str__(self):
            return self.comment


        def delete_comment(self):
            self.delete()

        def save_comment(self):
            self.save()


class Follow(models.Model):
	user = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete = models.CASCADE,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()


class Unfollow(models.Model):
	user = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete = models.CASCADE,null=True)

	def __int__(self):
		return self.name


class Likes(models.Model):
	user = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True)
	

	def __int__(self):
		return self.name

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save() 