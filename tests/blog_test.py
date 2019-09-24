import unittest
from app.models import User,Blog
from app import db

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.user_audrey = User(firstname = 'audrey',password = 'chapati')
        self.new_blog = Blog(id=12345,text='vegetable',user_id=1,category='nutrition',user = self.user_happiness)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
        def test_check_instance_variables(self):
            self.assertEquals(self.new_blog.id,12345)
            self.assertEquals(self.new_blog.user_id,1)
            self.assertEquals(self.new_blog.category,'nutrition')
            self.assertEquals(self.new_blog.user,self.user_audrey)


    def test_save_post(self):
        self.new_blog.save_blog()
        blogs = Blog.query.all()
        self.assertTrue(len(blogs)>0)
