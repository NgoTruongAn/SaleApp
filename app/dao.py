def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    }]


def get_products():
    products = [{
        "id":1,
        "name": "Iphone 13",
        "price": 2000000,
        "image": "https://res.cloudinary.com/dntsrn7mq/image/upload/v1695031567/apple-iphone-15-pro_vnojnd.jpg",
        "category_id": 1
    },{
        "id": 2,
        "name": "Iphone 14",
        "price": 2000000,
        "image": "https://res.cloudinary.com/dntsrn7mq/image/upload/v1695031567/apple-iphone-15-pro_vnojnd.jpg",
        "category_id": 2
    },{
        "id": 3,
        "name": "Iphone 15",
        "price": 2000000,
        "image": "https://res.cloudinary.com/dntsrn7mq/image/upload/v1695031567/apple-iphone-15-pro_vnojnd.jpg",
        "category_id": 3
    }]
    return products