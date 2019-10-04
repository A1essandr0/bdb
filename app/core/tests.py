from django.test import TestCase
from .models import Country, Currency, BondIssue, Comment


class TestModels(TestCase):
    def setUp(self):
        Country.objects.create(abbr="GV", name="Genovia")
        Currency.objects.create(abbr="SP", name="Genovian sepulka", country=Country.objects.get(name="Genovia"))

    def test_create_country_currency(self):
        """ Создание моделей Country и Currency """
        genovia = Country.objects.get(name="Genovia")
        sepulka = Currency.objects.get(name="Genovian sepulka")
        self.assertEqual(genovia.abbr, "GV")
        self.assertEqual(sepulka.abbr, "SP")

# Добавить юниттесты для: 
# - список выпусков и пагинации по ним
# - индивидуальный выпуск
# - логина как va, добавления комментария к некоторому выпуску, логаута
# - несколько вариантов поиска по базе: пустой/конкретный/етц
# - авторизация как админ и загрузка новых выпусков (малого/большого объема)

# - загрузка статьи в блог, в новости
# - список статей, новостей
# - индивидуальная статья, новость

