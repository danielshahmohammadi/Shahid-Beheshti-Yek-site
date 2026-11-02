from django.test import SimpleTestCase


class HomeNavigationTests(SimpleTestCase):
    def test_menu_links_open_their_pages(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'style="font-family:Lalezar;">درباره ما</a>')

        paths = (
            "/about/",
            "/gallerylist/",
            "/contanct_use/",
            "/newslist/",
            "/login/",
            "/honnors/",
            "/school_staff/",
            "/weblog/",
            "/facilitys/",
        )
        for path in paths:
            with self.subTest(path=path):
                self.assertContains(response, f'href="{path}"')
                self.assertEqual(self.client.get(path).status_code, 200)
