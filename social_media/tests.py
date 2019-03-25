from django.test import TestCase
from . models import Comment
# Create your tests here.

class CommentTestClass(TestCase):

    def setUp(self):
        
        self.new_comment = Comment(comment= "comment")
        self.new_comment.save()

