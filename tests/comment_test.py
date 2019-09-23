import unittest
from app.models import Comment,User,Blog
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_user = User(firstname = 'audrey',password = 'njiraini')
        self.new_comment = Comment(id=12345,post_id='2',user_id='2',post_comment='what food do you eat food?',user= self.new_user)
        
    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,12345)
        self.assertEquals(self.new_comment.blog_id,'2')
        self.assertEquals(self.new_comment.user_id,'2')
        self.assertEquals(self.new_comment.pitch_comment,'what foot do you eat food?')
        self.assertEquals(self.new_comment.user,self.new_user,self.new_post)


    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.query.all()
        self.assertTrue(len(comments)>0)