from django.test import TestCase
from home.models import UserProfile, Reviews


class HomeTestCase(TestCase):

    """This is the test for the home app"""

    def test_user_profile(self):

        """This is the test for the user profile model"""

        profile = UserProfile(
            image="test",
            city="test",
            mobile="test",
            username="test",
        )
        profile.save()
        self.assertEqual(profile.image, "test")
        self.assertEqual(profile.city, "test")
        self.assertEqual(profile.mobile, "test")
        self.assertEqual(profile.username, "test")

    def test_reviews(self):

        """This is the test for the reviews model"""

        review = Reviews(
            business_id="test",
            username="test",
            image_url="test",
            review_text="test",
            timestamp="test",
        )
        review.save()
        self.assertEqual(review.business_id, "test")
        self.assertEqual(review.username, "test")
        self.assertEqual(review.image_url, "test")
        self.assertEqual(review.review_text, "test")
        self.assertEqual(review.timestamp, "test")
