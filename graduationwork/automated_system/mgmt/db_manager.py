from .. import models
from datetime import datetime
from datetime import date
from datetime import timedelta


def fill_in_products():
    models.Product.objects.create(
        name="Apple",
        digit_code="00000-0001",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=200.0,
        height=100.0,
        length=150.0,
        weight=500.0,
        price=2.1,
        stackable=True)
    models.Product.objects.create(
        name="Pineapple",
        digit_code="00000-0002",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=150.0,
        height=300.0,
        length=150.0,
        weight=1500.0,
        price=1.1,
        stackable=True)
    models.Product.objects.create(
        name="Orange Juice",
        digit_code="00000-0003",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=100.0,
        height=200.0,
        length=50.0,
        weight=1000.0,
        price=1.2,
        stackable=True)
    models.Product.objects.create(
        name="Milk",
        digit_code="00000-0004",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=100.0,
        height=200.0,
        length=50.0,
        weight=950.0,
        price=0.9,
        stackable=True)
    models.Product.objects.create(
        name="Carrot",
        digit_code="00000-0005",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=90.0,
        height=60.0,
        length=150.0,
        weight=500.0,
        price=1.5,
        stackable=True)
    models.Product.objects.create(
        name="Cucumber",
        digit_code="00000-0007",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=80.0,
        height=80.0,
        length=100.0,
        weight=500.0,
        price=1.3,
        stackable=True)
    models.Product.objects.create(
        name="Potato",
        digit_code="00000-0008",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=150.0,
        height=75.0,
        length=80.0,
        weight=500.0,
        price=1.1,
        stackable=True)
    models.Product.objects.create(
        name="Tomato",
        digit_code="00000-0009",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=200.0,
        height=100.0,
        length=50.0,
        weight=500.0,
        price=1.4,
        stackable=True)


def fill_in_storage():
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Apple'),
        product_count=100)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Pineapple'),
        product_count=25)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Orange Juice'),
        product_count=50)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Milk'),
        product_count=30)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Carrot'),
        product_count=40)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Cucumber'),
        product_count=35)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Potato'),
        product_count=50)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Tomato'),
        product_count=40)


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
    stockProduct = models.Store.objects.get(id=1).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.1),
        start_timestamp=date.today() - timedelta(days=5),
        end_timestamp=date.today() - timedelta(days=3)
    )

    stockProduct = models.Store.objects.get(id=2).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.25),
        start_timestamp=date.today() - timedelta(days=10),
        end_timestamp=date.today() - timedelta(days=7)
    )

    stockProduct = models.Store.objects.get(id=4).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.2),
        start_timestamp=date.today() - timedelta(days=2),
        end_timestamp=date.today() - timedelta(days=1)
    )

    stockProduct = models.Store.objects.get(id=6).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.15),
        start_timestamp=date.today() - timedelta(days=9),
        end_timestamp=date.today() - timedelta(days=7)
    )

    stockProduct = models.Store.objects.get(id=9).product
    models.Stock.objects.create(
        product=stockProduct,
        stock_price=(stockProduct.price - stockProduct.price * 0.1),
        start_timestamp=date.today() - timedelta(days=3),
        end_timestamp=date.today()
    )


def fill_in_statistics():
    # Store obj with id = 1
    shelf = models.Store.objects.get(id=1)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=34,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=33,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=35,
        failures_count=2,
        price_that_day=shelf.product.price,
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=31,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=34,
        failures_count=0,
        price_that_day=shelf.product.price
    )

    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=5),
            datetime.min.time()
        )
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=39,
        stock=stockStats,
        failures_count=4,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=41,
        stock=stockStats,
        failures_count=5,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=38,
        stock=stockStats,
        failures_count=3,
        price_that_day=shelf.product.price
    )

    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=27,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=29,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=31,
        failures_count=2,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 2
    shelf = models.Store.objects.get(id=2)
    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=10),
            datetime.min.time()
        )
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=11,
        stock=stockStats,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=12,
        stock=stockStats,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=9,
        stock=stockStats,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=8,
        stock=stockStats,
        failures_count=0,
        price_that_day=shelf.product.price
    )

    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=4,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=5,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=5,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=6,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=4,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=6,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=5,
        failures_count=1,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 3
    shelf = models.Store.objects.get(id=3)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=11,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=13,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=9,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=12,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=13,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=14,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=10,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=17,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=14,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=16,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=15,
        failures_count=1,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 4
    shelf = models.Store.objects.get(id=4)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=15,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=17,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=19,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=12,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=15,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=14,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=13,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=17,
        failures_count=2,
        price_that_day=shelf.product.price
    )

    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=2),
            datetime.min.time()
        )
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=21,
        stock=stockStats,
        failures_count=3,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=24,
        stock=stockStats,
        failures_count=4,
        price_that_day=shelf.product.price
    )

    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=15,
        failures_count=1,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 5
    shelf = models.Store.objects.get(id=5)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=16,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=19,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=20,
        failures_count=3,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=17,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=19,
        failures_count=3,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=17,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=18,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=22,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=21,
        failures_count=3,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=17,
        failures_count=3,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=14,
        failures_count=2,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 6
    shelf = models.Store.objects.get(id=6)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=6,
        failures_count=0,
        price_that_day=shelf.product.price
    )

    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=9),
            datetime.min.time()
        )
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=12,
        stock=stockStats,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=14,
        stock=stockStats,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=15,
        stock=stockStats,
        failures_count=1,
        price_that_day=shelf.product.price
    )

    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=4,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=7,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=8,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=5,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=11,
        failures_count=0,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=7,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=4,
        failures_count=0,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 7
    shelf = models.Store.objects.get(id=7)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=8,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=12,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=11,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=9,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=14,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=7,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=8,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=15,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=11,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=17,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=14,
        failures_count=2,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 8
    shelf = models.Store.objects.get(id=8)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=18,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=15,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=14,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=19,
        failures_count=3,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=14,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=17,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=18,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=15,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=17,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=15,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=14,
        failures_count=1,
        price_that_day=shelf.product.price
    )

    # Store obj with id = 9
    shelf = models.Store.objects.get(id=9)
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=10),
        shelf=shelf,
        sold_count=12,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=9),
        shelf=shelf,
        sold_count=15,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=8),
        shelf=shelf,
        sold_count=7,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=7),
        shelf=shelf,
        sold_count=16,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=6),
        shelf=shelf,
        sold_count=12,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=5),
        shelf=shelf,
        sold_count=17,
        failures_count=1,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=4),
        shelf=shelf,
        sold_count=8,
        failures_count=1,
        price_that_day=shelf.product.price
    )

    stockStats = models.Stock.objects.get(
        product=shelf.product,
        start_timestamp=datetime.combine(
            date.today() - timedelta(days=3),
            datetime.min.time()
        )
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=3),
        shelf=shelf,
        sold_count=15,
        stock=stockStats,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=2),
        shelf=shelf,
        sold_count=17,
        stock=stockStats,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today() - timedelta(days=1),
        shelf=shelf,
        sold_count=18,
        stock=stockStats,
        failures_count=2,
        price_that_day=shelf.product.price
    )
    models.Statistics.objects.create(
        day=date.today(),
        shelf=shelf,
        sold_count=16,
        stock=stockStats,
        failures_count=2,
        price_that_day=shelf.product.price
    )


# def fill_in_staff():
#     models.Staff.objects.create(
#         name = "John", surname = "Doe", position = "Business manager")
#     models.Staff.objects.create(
#         name = "Jane", surname = "Doe", position = "Store manager")
#     models.Staff.objects.create(
#         name = "Mike", surname = "Smith", position = "Merchandizer")
#     models.Staff.objects.create(
#         name = "Tom", surname = "Heinz", position = "Merchandizer")
#     models.Staff.objects.create(
#         name = "Hacker", surname = "Man", position = "System administrator")
#     models.Staff.objects.create(
#         name = "Vasya", surname = "Sidorov", position = "Driver")


# def fill_in_equipment():
#     models.Equipment.objects.create(name = "Automated System", equipment_type = "Enterprise",
#                                     cost = "99999.9", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 1", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 2", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 3", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 4", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 5", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 6", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 7", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Shelf 8", equipment_type = "Store Component",
#                                     cost = "150.5", last_maintainance_date = datetime.now(), warranty_period_years = 228)
#     models.Equipment.objects.create(name = "Truck", equipment_type = "Car",
#                                     cost = "6500.2", last_maintainance_date = datetime.now(), warranty_period_years = 10)


# def remove_product():
#     models.Product.objects.filter(id = 1).delete()


# def update_store():
#     models.Store.objects.filter(id = 1).update(product_count = 9)
#     models.Store.objects.filter(id = 2).update(product_count = 5)
#     models.Store.objects.filter(id = 3).update(product_count = 7)
#     models.Store.objects.filter(id = 4).update(product_count = 5)
#     models.Store.objects.filter(id = 5).update(product_count = 8)
#     models.Store.objects.filter(id = 6).update(product_count = 9)
#     models.Store.objects.filter(id = 7).update(product_count = 9)
#     models.Store.objects.filter(id = 8).update(product_count = 6)


# def update_store_products(product_id, product_count):
#     models.Store.objects.filter(id = product_id).update(
#         product_count = product_count)


# def update_storage_products(product_id, product_count):
#     models.Storage.objects.filter(id = product_id).update(
#         product_count = product_count)


# def update_references():
#     models.Store.objects.filter(id = 1).update(maintainer_id = 3)


# def checkStore():
#     statusString = ""
#     status = "fine"
#     shelf = models.Store.objects.all()
#     for product in shelf:
#         currentProduct = models.Product.objects.get(id = product.product_id)
#         if product.product_count < 5:
#             statusString = "Product: " + currentProduct.name + \
#                 ": insufficient count of product on shelf"
#             if status != "error":
#                 status = "warning"
#             print(product.product_count)
#             # externalModule.orderProductFromStorage
#         elif product.product_count == 0:
#             statusString = "Product: " + currentProduct.name + ": shelf is out of this product"
#             status = "error"
#             # externalModule.orderProductFromStorage
#     if not statusString:
#         statusString = "fine"
#     return {"data": "Store: " + statusString + "; ", "status": status}


# def checkStorage():
#     statusString = ""
#     status = "fine"
#     storage = models.Storage.objects.all()
#     for product in storage:
#         currentProduct = models.Product.objects.get(id = product.product_id)
#         if product.product_count < 50:
#             statusString = "Product: " + currentProduct.name + \
#                 ": insufficient count of product in storage"
#             if status != "error":
#                 status = "warning"
#             print(product.product_count)
#             # externalModule.orderProductFromExternal
#         elif product.product_count == 0:
#             statusString = "Product: " + currentProduct.name + \
#                 ": storage is out of this product"
#             status = "error"
#             # externalModule.orderProductFromExternal
#             # externalModule.notifyManagement
#     if not statusString:
#         statusString = "fine"
#     return {"data": "Storage: " + statusString + "; ", "status": status}


# def checkEquipment():
#     statusString = ""
#     status = "fine"
#     equipment = models.Equipment.objects.all()
#     for item in equipment:
#         currentDate = datetime.now()
#         lastMaintainanceYear = item.last_maintainance_date.year
#         warrantyExpirationDate = item.last_maintainance_date.replace(
#             year = lastMaintainanceYear+item.warranty_period_years, tzinfo = None)
#         daysToExpire = abs((currentDate-warrantyExpirationDate).days)
#         if daysToExpire < 30 and daysToExpire > 0:
#             statusString = "Equipment: " + item.name + \
#                 ": warranty is about to expire"
#             if status != "error":
#                 status = "warning"
#             # externalModule.notifyManagement
#         elif daysToExpire < 0:
#             statusString = "Equipment: " + item.name + \
#                 ": warranty expired"
#             status = "error"
#             # externalModule.notifyManagement
#     if not statusString:
#         statusString = "fine"
#     return {"data": "Equipment: " + statusString + "; ", "status": status}


# def get_current_status():
#     storeStatus = checkStore()
#     storageStatus = checkStorage()
#     equipmentStatus = checkEquipment()
#     return {"store": storeStatus, "storage": storageStatus, "equipment": equipmentStatus}


# def get_storage_products():
#     return models.Storage.objects.all()


# def get_storage_products_for_page():
#     storageProduct = []
#     for item in models.Storage.objects.all():
#         product_name = models.Product.objects.get(id = item.product_id).name
#         product_count = models.Storage.objects.get(id = item.id).product_count
#         last_delivery = models.CargoTransportation.objects.get(
#             id = item.delivery_id).delivery_date
#         image_name = product_name.lower().replace(' ', '_')
#         storageProduct.append({"product_name": product_name, "product_count": product_count,
#                                "last_delivery": last_delivery, "image_name": image_name})
#     return storageProduct


# def get_store_products():
#     return models.Store.objects.all()


# def get_transportations_info():
#     transpos = []
#     for transp in models.CargoTransportation.objects.all():
#         product_name = models.Product.objects.get(id = transp.product_id).name
#         transpos.append({"product_name": product_name, "company_name": transp.company_name,
#                          "delivery_date": transp.delivery_date, "delivered_count": transp.delivered_count})
#     return transpos
