import requests
from django.core.management.base import BaseCommand

from products.models import Product, Category


class Command(BaseCommand):
#test travis
    def __init__(self):
        self.CATEGORIES_ARRAY = ['petit-dejeuners', 'plats-prepares',
                                  'snacks-sales', 'biscuits-et-gateaux',
                                  'snacks-sucres', 'produits-laitiers',
                                  'epicerie', 'desserts', 'charcuteries',
                                  'cereales-et-derives', 'boissons', 'fromages',
                                  'fruits', 'soupes',
                                  'pizzas-tartes-salees-et-quiches',
                                  'bieres', 'pates-a-tartiner',
                                  'boissons-chaudes', 'graines', 'biscuits']
    """
    def get_categories(self):
        categories = openfoodfacts.facets.get_categories()
        category_id = list()
        for i in categories:
            if "fr:" in i["id"]:
                category_id.append(i["id"])
        cat = [c.replace('fr:', '') for c in category_id]
        cat = random.choices(cat, k=50)
        return cat
    """

    def fill_categories(self, cat):
        for index, value in enumerate(cat):
            try:
                categories = Category(name=value)
                if Category.objects.filter(name=value).exists():
                    continue
                else:
                    categories.save()
            except KeyError as e:
                print(e)

    # get id and name from categories to populate products table
    def fill_products(self, cat):
        for index, value in enumerate(cat):

            temp_var = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=labels&tag_contains_0=contains&tag_0=sans%20gluten&tagtype_1=categories&tag_contains_1=contains&tag_1={}&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1".format(
                    value)).json()
            for x, i in enumerate(temp_var['products']):
                category_id = Category.objects.get(name=value)
                try:
                    products = Product(product_name=i['product_name_fr'],
                                       nutriscore_grade=i['nutrition_grades'],
                                       store=i['stores_tags'],
                                       url_picture=i['selected_images']['front']['display']['fr'],
                                       url_picture_small=i['selected_images']['front']['small']['fr'],
                                       url_product=i['url'],
                                       description=i['generic_name_fr'],
                                       category_id=category_id.pk)
                    if Product.objects.filter(
                            product_name=i['product_name_fr']).exists():
                        continue
                    else:
                        products.save()
                except KeyError as e:
                    print(e)
                if x == 200:
                    break

    def handle(self, *args, **options):
        categories = self.CATEGORIES_ARRAY
        self.fill_categories(categories)
        self.fill_products(categories)
