from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import PostModel


# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="secret",
        )
        cls.post = PostModel.objects.create(
            author=cls.user,
            title="A good title",
            body="Text body here"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Text body here")
        self.assertEqual(str(self.post), "A good title")
