from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # Declare variable untuk test function nanti
    # self.user
    # self.client
    # self.admin_user
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='test1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='password1234',
            name='Metal Head'
        )

    def test_user_listed(self):
        """
        Test yang user tersenarai dalam User Page
        Input: res
        Output: check yang res ada self.user.name && self.user.email
        """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """
        Test yang 'User Edit Page' dapat guna
        Input : extract (get) self.client produce reverse url
        Output: status code = 200
        """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """
        Test yang Create User Page dapat guna
        Input: Retrieve/get admin:core_user_add
        Output: status code = 200
        """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
