from django.test import TestCase
from django.test import TestCase

from .models import Neighborhood, Business, PostType,Post,Profile
# Create your tests here.

class NeighborhoodTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.hood = Neighborhood(name="Srilanka")
        self.hood.save_neighborhood()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Neighborhood))

    def test_save_method(self):
        self.hood.save_neighborhood()
        neigborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neigborhoods) > 0)

    def test_delete_method(self):
        self.hood.save_neigborhood()
        self.hood.delete_neigborhood()
        neigborhood = neigborhood.objects.all()
        self.assertTrue(len(neigborhood) == 0)

    def test_update(self):
        neigborhood = neigborhood.get_neigborhood_id(self.hood.id)
        neigborhood.update_neigborhood('Mesopotamia')
        neigborhood = neigborhood.get_neigborhood_id(self.hood.id)
        self.assertTrue(neigborhood.name == 'Mesopotamia')


 
 #test for Business Model

class BusinessTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.bus = Business(name="pub shoes")
        self.bus.save_business()

    def test_instance(self):
        self.assertTrue(isinstance(self.bus, Business))

    def test_save_method(self):
        self.bus.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_method(self):
        self.bus.save_business()
        self.bus.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

    def test_update(self):
        business = Business.get_business_id(self.bus.id)
        business.update_business('shoes')
        business = Business.get_business_id(self.bus.id)
        self.assertTrue(Business.name == 'shoes')

 #test for Post Model

class PostTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.post = Post(name="fashion")
        self.post.save_post()

        self.Post = Post(name='Post test', description='my test',Post_neigborhood=self.hood, Post_image='default.jpg')
        self.Post.save_Post()

    def test_instance(self):
        self.assertTrue(isinstance(self.Post, Post))

    def tearDown(self):
        self.Post.delete_Post()
        self.bus.delete_Business()
        self.hood.delete_neigborhood()


    def test_save_method(self):
        self.Post.save_Post()
        Posts  = Post.objects.all()
        self.assertTrue(len(Posts)>0)


    def test_get_all_Posts(self):
        Posts = Post.get_all_Posts()
        self.assertTrue(len(Posts)>0)

    def test_get_Post_by_id(self):
        Posts= Post.get_Post_by_id(self.Post.id)
        self.assertTrue(len(Posts) == 1)

    def test_search_by_Business(self):
        businesses = Business.search_by_Business('fashion')
        self.assertTrue(len(businesses)>0)


    def test_update_Post(self):
        self.Post.save_Post()
        Post = Post.update_Post( self.Post.id, 'test update', 'my test',self.hood, self.bus)
        upPost = Post.objects.filter(id = self.Post.id)
        print(upPost)
        self.assertTrue(Post.name == 'test update')

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        self.prof = Profile(name="Liz")
        self.prof.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_method(self):
        self.prof.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.prof.save_profile()
        self.prof.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

    def test_update(self):
        profile = Profile.get_profile_id(self.prof.id)
        profile.update_profile('liz')
        profile = Profile.get_profile_id(self.prof.id)
        self.assertTrue(profile.username == 'liz')

class PostTypeTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.type = PostType(name="liz")
        self.type.save_type()


    def test_instance(self):
        self.assertTrue(isinstance(self.type, PostType))

#     

    def test_save_method(self):
        self.like.save_like()
        types  = PostType.objects.all()
        self.assertTrue(len(types)>0)
