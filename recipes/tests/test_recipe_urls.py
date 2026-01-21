from modulefinder import replacePackageMap
from django.test import TestCase
from django.urls import reverse

from recipes.models import Recipe


class RecipoeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, "/")

    def test_recipe_category_url_is_correct(self):
        url = reverse("recipes:category", kwargs={"category_id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_recipe_detail_url_is_correct(self):
        url = reverse("recipes:recipe", kwargs={"pk": 1})
        self.assertEqual(url, "/recipes/1/")

    def test_recipe_search_url_is_correct(self):
        url = reverse("recipes:search")
        self.assertEqual(url, "/recipes/search/")

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse("recipes:search") + "?q=teste")
        self.assertTemplateUsed(response, "recipes/pages/search.html")

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse("recipes:search")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse("recipes:search") + "?q=<Teste>"
        response = self.client.get(url)
       
        self.assertIn(
            "Search for &quot;&lt;Teste&gt;&quot;", response.content.decode("utf-8")
        )
