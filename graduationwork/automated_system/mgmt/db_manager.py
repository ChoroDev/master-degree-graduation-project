from .. import models
from datetime import datetime
from datetime import date
from datetime import timedelta
import random


def restore_db():
    models.Product.objects.all().delete()
    models.Storage.objects.all().delete()
    models.Store.objects.all().delete()
    models.Stock.objects.all().delete()
    models.Statistics.objects.all().delete()
    fill_in_products()
    fill_in_storage()
    fill_in_store()
    fill_in_stocks()
    fill_in_statistics()


def fill_in_products():
    models.Product.objects.create(
        name="Apple",
        digit_code="00000-0001",
        shelf_life=10,
        width=200.0,
        height=100.0,
        length=150.0,
        weight=500.0,
        price=2.1,
        stackable=True)
    models.Product.objects.create(
        name="Pineapple",
        digit_code="00000-0002",
        shelf_life=10,
        width=150.0,
        height=300.0,
        length=150.0,
        weight=1500.0,
        price=1.1,
        stackable=True)
    models.Product.objects.create(
        name="Orange Juice",
        digit_code="00000-0003",
        shelf_life=10,
        width=100.0,
        height=200.0,
        length=50.0,
        weight=1000.0,
        price=1.2,
        stackable=True)
    models.Product.objects.create(
        name="Milk",
        digit_code="00000-0004",
        shelf_life=10,
        width=100.0,
        height=200.0,
        length=50.0,
        weight=950.0,
        price=0.9,
        stackable=True)
    models.Product.objects.create(
        name="Carrot",
        digit_code="00000-0005",
        shelf_life=10,
        width=90.0,
        height=60.0,
        length=150.0,
        weight=500.0,
        price=1.5,
        stackable=True)
    models.Product.objects.create(
        name="Cucumber",
        digit_code="00000-0007",
        shelf_life=10,
        width=80.0,
        height=80.0,
        length=100.0,
        weight=500.0,
        price=1.3,
        stackable=True)
    models.Product.objects.create(
        name="Potato",
        digit_code="00000-0008",
        shelf_life=10,
        width=150.0,
        height=75.0,
        length=80.0,
        weight=500.0,
        price=1.1,
        stackable=True)
    models.Product.objects.create(
        name="Tomato",
        digit_code="00000-0009",
        shelf_life=10,
        width=200.0,
        height=100.0,
        length=50.0,
        weight=500.0,
        price=1.4,
        stackable=True)


def fill_in_storage():
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Apple'),
        product_count=100,
        delivery_timestamp=datetime.now())
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Pineapple'),
        product_count=25,
        delivery_timestamp=datetime.now())
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Orange Juice'),
        product_count=50,
        delivery_timestamp=datetime.now())
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Milk'),
        product_count=30,
        delivery_timestamp=datetime.now())
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Carrot'),
        product_count=40,
        delivery_timestamp=datetime.now())
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Cucumber'),
        product_count=35,
        delivery_timestamp=datetime.now())
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Potato'),
        product_count=50,
        delivery_timestamp=datetime.now())
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Tomato'),
        product_count=40,
        delivery_timestamp=datetime.now())


def fill_in_store():
    models.Store.objects.create(
        product=models.Product.objects.get(name='Apple'),
        product_count=1,
        width=1000.0,
        height=400.0,
        length=500.0,
        carrying_capacity=100000.0,
        shelf_name='Apples_1',
        section_name='Fruits_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Pineapple'),
        product_count=1,
        width=1000.0,
        height=400.0,
        length=500.0,
        carrying_capacity=100000.0,
        shelf_name='Pineapples_1',
        section_name='Fruits_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Orange Juice'),
        product_count=1,
        width=2000.0,
        height=300.0,
        length=300.0,
        carrying_capacity=200000.0,
        shelf_name='Juices_1',
        section_name='Drinks_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Milk'),
        product_count=1,
        width=1000.0,
        height=300.0,
        length=300.0,
        carrying_capacity=50000.0,
        shelf_name='Milk_1',
        section_name='Milk_Products_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Milk'),
        user=models.User.objects.get(id=6),
        product_count=1,
        width=1000.0,
        height=300.0,
        length=300.0,
        carrying_capacity=50000.0,
        shelf_name='Milk_2',
        section_name='Milk_Products_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Carrot'),
        product_count=1,
        width=500.0,
        height=400.0,
        length=500.0,
        carrying_capacity=50000.0,
        shelf_name='Carrots_1',
        section_name='Vegetables_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Cucumber'),
        product_count=1,
        width=1000.0,
        height=500.0,
        length=700.0,
        carrying_capacity=100000.0,
        shelf_name='Cucumbers_1',
        section_name='Vegetables_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Potato'),
        product_count=1,
        width=1500.0,
        height=400.0,
        length=500.0,
        carrying_capacity=150000.0,
        shelf_name='Potatoes_1',
        section_name='Vegetables_1')
    models.Store.objects.create(
        product=models.Product.objects.get(name='Tomato'),
        user=models.User.objects.get(id=7),
        product_count=1,
        width=1000.0,
        height=500.0,
        length=700.0,
        carrying_capacity=100000.0,
        shelf_name='Tomatoes_1',
        section_name='Vegetables_1')


def fill_in_failures():
    models.Failure.objects.create(
        text="Shelf should be filled in by 10 products. Shelf name: Potatoes_1, section name: Vegetables_1.",
        severity=4,
        possible_cause="Customers bought a lot of products from that shelf.",
        possible_solution="Fill shelf in."
    )
    models.Failure.objects.create(
        text="Shelf should be filled in by 5 products. Shelf name: Cucumbers_1, section name: Vegetables_1.",
        severity=3,
        possible_cause="Customers bought a lot of products from that shelf.",
        possible_solution="Fill shelf in."
    )
    models.Failure.objects.create(
        text="2 products should be transferred to the storage. Shelf name: Juices_1, section name: Drinks_1.",
        possible_cause="Customers didn't buy a lot of products from that shelf.",
        possible_solution="Transfer products to the storage."
    )
    models.Failure.objects.create(
        text="Shelf should be filled in by 9 products. Shelf name: Milk_1, section name: Milk_Products_1.",
        severity=3,
        possible_cause="Customers bought a lot of products from that shelf.",
        possible_solution="Fill shelf in."
    )
    models.Failure.objects.create(
        text="Number of products should be clarified. Shelf name: Potatoes_1, section name: Vegetables_1",
        severity=2,
        possible_cause="A lot of time has passed since the last update.",
        possible_solution="Clarify the number of products."
    )
    models.Failure.objects.create(
        text="Number of products should be clarified. Shelf name: Tomatoes_1, section name: Vegetables_1",
        severity=2,
        possible_cause="A lot of time has passed since the last update.",
        possible_solution="Clarify the number of products.",
        assignee=models.User.objects.get(id=7)
    )
    models.Failure.objects.create(
        text="Shelf should be filled in by 5 products. Shelf name: Milk_2, section name: Milk_Products_1.",
        severity=3,
        possible_cause="A lot of time has passed since the last update.",
        possible_solution="Clarify the number of products.",
        assignee=models.User.objects.get(id=6)
    )
    models.Failure.objects.create(
        text="Shelf should be filled in by 15 products. Shelf name: Carrots_1, section name: Vegetables_1.",
        severity=4,
        possible_cause="Customers bought a lot of products from that shelf.",
        possible_solution="Fill shelf in.",
        is_solved=True,
        assignee=models.User.objects.get(id=8)
    )
    models.Failure.objects.create(
        text="Number of products should be clarified. Shelf name: Carrots_1, section name: Vegetables_1.",
        severity=2,
        possible_cause="A lot of time has passed since the last update.",
        possible_solution="Clarify the number of products.",
        is_solved=True,
        assignee=models.User.objects.get(id=8)
    )
    models.Failure.objects.create(
        text="3 products should be transferred to the storage. Shelf name: Juices_1, section name: Drinks_1.",
        possible_cause="Customers didn't buy a lot of products from that shelf.",
        possible_solution="Transfer products to the storage.",
        is_solved=True
    )


def fill_in_stocks():
    firstShelf = models.Store.objects.order_by('id').first()

    stockProduct = models.Store.objects.get(id=firstShelf.id).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.1),
        start_timestamp=date.today() - timedelta(days=5),
        end_timestamp=date.today() - timedelta(days=3)
    )
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price * 0.9 - stockProduct.price * 0.15),
        start_timestamp=date.today() - timedelta(days=366+9),
        end_timestamp=date.today() - timedelta(days=366+6)
    )

    stockProduct = models.Store.objects.get(id=firstShelf.id+1).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.25),
        start_timestamp=date.today() - timedelta(days=10),
        end_timestamp=date.today() - timedelta(days=7)
    )

    stockProduct = models.Store.objects.get(id=firstShelf.id+3).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.2),
        start_timestamp=date.today() - timedelta(days=2),
        end_timestamp=date.today() - timedelta(days=1)
    )
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price * 0.8 - stockProduct.price * 0.25),
        start_timestamp=date.today() - timedelta(days=365+366+6),
        end_timestamp=date.today() - timedelta(days=365+366+4)
    )

    stockProduct = models.Store.objects.get(id=firstShelf.id+5).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.15),
        start_timestamp=date.today() - timedelta(days=9),
        end_timestamp=date.today() - timedelta(days=7)
    )

    stockProduct = models.Store.objects.get(id=firstShelf.id+8).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.1),
        start_timestamp=date.today() - timedelta(days=3),
        end_timestamp=date.today()
    )


def fill_in_statistics():
    firstShelf = models.Store.objects.order_by('id').first()
    #
    # Store obj with id = 1
    #
    shelf = models.Store.objects.get(id=firstShelf.id)

    # 2020
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=5),
            datetime.min.time()
        )
    )
    for i in range(10, -1, -1):
        if i <= 5 and i >= 3:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(30, 42),
                stock=stockStats,
                failures_count=random.randint(1, 5),
                price_that_day=shelf.product.price
            )
        else:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(27, 37),
                failures_count=random.randint(0, 4),
                price_that_day=shelf.product.price
            )

    # 2019
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=366+9),
            datetime.min.time()
        )
    )
    for i in range(10, -1, -1):
        if i <= 9 and i >= 6:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=366+i),
                shelf=shelf,
                sold_count=random.randint(31, 41),
                stock=stockStats,
                failures_count=random.randint(1, 5),
                price_that_day=shelf.product.price * 0.9
            )
        else:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=366+i),
                shelf=shelf,
                sold_count=random.randint(28, 36),
                failures_count=random.randint(0, 4),
                price_that_day=shelf.product.price * 0.9
            )

    #
    # Store obj with id = 2
    #
    shelf = models.Store.objects.get(id=firstShelf.id+1)

    # 2020
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=10),
            datetime.min.time()
        )
    )
    for i in range(10, -1, -1):
        if i <= 10 and i >= 7:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(5, 12),
                stock=stockStats,
                failures_count=random.randint(1, 3),
                price_that_day=shelf.product.price
            )
        else:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(4, 9),
                failures_count=random.randint(0, 2),
                price_that_day=shelf.product.price
            )

    #
    # Store obj with id = 3
    #
    shelf = models.Store.objects.get(id=firstShelf.id+2)

    # 2020
    for i in range(10, -1, -1):
        models.Statistics.objects.create(
            day=date.today() - timedelta(days=i),
            shelf=shelf,
            sold_count=random.randint(9, 17),
            failures_count=random.randint(0, 2),
            price_that_day=shelf.product.price
        )

    #
    # Store obj with id = 4
    #
    shelf = models.Store.objects.get(id=firstShelf.id+3)

    # 2020
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=2),
            datetime.min.time()
        )
    )
    for i in range(10, -1, -1):
        if i <= 2 and i >= 1:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(21, 24),
                stock=stockStats,
                failures_count=random.randint(1, 3),
                price_that_day=shelf.product.price
            )
        else:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(12, 19),
                failures_count=random.randint(0, 2),
                price_that_day=shelf.product.price
            )

    # 2019
    for i in range(10, -1, -1):
        models.Statistics.objects.create(
            day=date.today() - timedelta(days=366+i),
            shelf=shelf,
            sold_count=random.randint(14, 21),
            failures_count=random.randint(0, 3),
            price_that_day=shelf.product.price * 0.95
        )

    # 2018
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=365+366+6),
            datetime.min.time()
        )
    )
    for i in range(10, -1, -1):
        if i <= 6 and i >= 4:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=365+366+i),
                shelf=shelf,
                sold_count=random.randint(18, 25),
                stock=stockStats,
                failures_count=random.randint(1, 4),
                price_that_day=shelf.product.price * 0.8
            )
        else:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=365+366+i),
                shelf=shelf,
                sold_count=random.randint(13, 20),
                failures_count=random.randint(0, 2),
                price_that_day=shelf.product.price * 0.8
            )

    #
    # Store obj with id = 5
    #
    shelf = models.Store.objects.get(id=firstShelf.id+4)

    # 2020
    for i in range(10, -1, -1):
        models.Statistics.objects.create(
            day=date.today() - timedelta(days=i),
            shelf=shelf,
            sold_count=random.randint(14, 22),
            failures_count=random.randint(0, 3),
            price_that_day=shelf.product.price
        )

    #
    # Store obj with id = 6
    #
    shelf = models.Store.objects.get(id=firstShelf.id+5)

    # 2020
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=9),
            datetime.min.time()
        )
    )
    for i in range(10, -1, -1):
        if i <= 9 and i >= 7:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(8, 15),
                stock=stockStats,
                failures_count=random.randint(0, 2),
                price_that_day=shelf.product.price
            )
        else:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(4, 11),
                failures_count=random.randint(0, 1),
                price_that_day=shelf.product.price
            )

    #
    # Store obj with id = 7
    #
    shelf = models.Store.objects.get(id=firstShelf.id+6)

    # 2020
    for i in range(10, -1, -1):
        models.Statistics.objects.create(
            day=date.today() - timedelta(days=i),
            shelf=shelf,
            sold_count=random.randint(7, 17),
            failures_count=random.randint(0, 2),
            price_that_day=shelf.product.price
        )

    #
    # Store obj with id = 8
    #
    shelf = models.Store.objects.get(id=firstShelf.id+7)

    # 2020
    for i in range(10, -1, -1):
        models.Statistics.objects.create(
            day=date.today() - timedelta(days=i),
            shelf=shelf,
            sold_count=random.randint(13, 20),
            failures_count=random.randint(0, 2),
            price_that_day=shelf.product.price
        )

    #
    # Store obj with id = 9
    #
    shelf = models.Store.objects.get(id=firstShelf.id+8)

    # 2020
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=3),
            datetime.min.time()
        )
    )
    for i in range(10, -1, -1):
        if i <= 3 and i >= 0:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(11, 22),
                stock=stockStats,
                failures_count=random.randint(0, 3),
                price_that_day=shelf.product.price
            )
        else:
            models.Statistics.objects.create(
                day=date.today() - timedelta(days=i),
                shelf=shelf,
                sold_count=random.randint(8, 17),
                failures_count=random.randint(0, 2),
                price_that_day=shelf.product.price
            )
