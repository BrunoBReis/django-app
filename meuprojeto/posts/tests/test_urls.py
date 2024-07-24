from django.test import TestCase, Client
from django.urls import reverse, resolve
from ..views import posts_list_view
from ..models import Post
from django.contrib.auth.models import User
from .. import urls


class UrlsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # Use the correct name with namespace 'posts:list'
        self.url = reverse('posts:list')

        # Create a user to associate with the posts
        self.user = User.objects.create_user(
            username='testuser', password='password')

        # Create some sample posts for testing
        self.post1 = Post.objects.create(
            title='Post 1',
            body='Content for post 1',
            slug='post-1',
            date='2023-07-01',
            author=self.user
        )
        self.post2 = Post.objects.create(
            title='Post 2',
            body='Content for post 2',
            slug='post-2',
            date='2023-07-02',
            author=self.user
        )

    def test_posts_list_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_posts_list_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'posts/posts_list.html')

    def test_posts_list_view_context_data(self):
        response = self.client.get(self.url)
        self.assertIn('posts', response.context)
        # Posts should be ordered by date descending
        self.assertEqual(list(response.context['posts']), [
                         self.post2, self.post1])
