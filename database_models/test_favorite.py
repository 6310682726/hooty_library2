from django.db import IntegrityError
from django.test import TestCase
from .models import *
from datetime import datetime, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile


class FavoriteTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='password',
            email='user1@email.email'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='password',
            email='user2@email.email'
        )
        self.genre1 = Genre.objects.create(
            genre_list='genre1'
        )
        self.genre2 = Genre.objects.create(
            genre_list='genre2'
        )
        self.book1 = Book.objects.create(
            book_name='book1',
            author=self.user2,
            book_type=1,
            genres=('genre1', 'genre2'),
            description='This is book1 description',
            thumbnail=SimpleUploadedFile(name='RH_StudyGuide.jpg', content=open(
                'database_models/data_test/RH_StudyGuide.jpg', 'rb').read(), content_type='image/jpeg'),
            pdf_files=SimpleUploadedFile(name='RH_StudyGuide_V2.pdf', content=open(
                'database_models/data_test/RH_StudyGuide_V2.pdf', 'rb').read(), content_type='application/pdf'),
        )
        self.favorite1 = Favorite.objects.create(
            user_refer=self.user1,
            book_refer=self.book1,
        )

    def test_create_favorite_correct(self):
        # test favorite created correctly
        with self.subTest():
            self.assertEqual(self.favorite1.user_refer, self.user1)
        with self.subTest():
            self.assertEqual(self.favorite1.book_refer, self.book1)

    def test_pair_of_user_book_is_unique(self):
        # test favorite has pair of user_refer, book_refer uniquely
        with self.subTest():
            with self.assertRaises(Exception) as raised:

                self.read2 = Favorite.objects.create(
                    user_refer=self.user1,
                    book_refer=self.book1,
                )
            self.assertEqual(IntegrityError, type(raised.exception))

    def test_favorite_on_user_refer_deleted(self):
        # test favorite when user_refer was deleted
        self.user1.delete()
        with self.assertRaises(Exception) as raised:
            Favorite.objects.get(user_refer=self.user1, book_refer=self.book1)
        self.assertEqual(Favorite.DoesNotExist, type(raised.exception))

    def test_read_on_book_refer_deleted(self):
        # test favorite when book_refer was deleted
        self.book1.delete()
        with self.assertRaises(Exception) as raised:
            Favorite.objects.get(user_refer=self.user1, book_refer=self.book1)
        self.assertEqual(Favorite.DoesNotExist, type(raised.exception))