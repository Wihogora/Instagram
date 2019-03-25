from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = "images/",null = True)
    user = models.ForeignKey(User,null=True)
    image_name = models.CharField(max_length = 40,null = True)
    likes = models.IntegerField(default=0)
    image_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    # profile = models.ForeignKey(Profile, null=True) 
    comments = models.IntegerField(default=0)


    def __str__(self):
    	return self.image_name

    def delete_image(self):
    	self.delete()

    def save_image(self):
    	self.save()

    def update_caption(self,new_caption):
    	self.image_caption = new_caption
    	self.save()