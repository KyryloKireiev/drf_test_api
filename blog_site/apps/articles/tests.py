from django.test import TestCase

lst = [
        {
            "id": 1,
            "title": "Acer UPDATE",
            "cat": "PC"
        },
        {
            "id": 2,
            "title": "Samsung Note 10",
            "cat": "PC"
        },
        {
            "id": 3,
            "title": "Mac",
            "cat": "PC"
        },
        {
            "id": 4,
            "title": "Toyota",
            "cat": "PC"
        },
        {
            "id": 5,
            "title": "renault",
            "cat": "PC"
        },
        {
            "id": 6,
            "title": "Nissan Update",
            "cat": "PC"
        },
        {
            "id": 7,
            "title": "Nissan",
            "cat": "PC"
        },
        {
            "id": 8,
            "title": "nokia",
            "cat": "PC"
        },
        {
            "id": 9,
            "title": "nokia",
            "cat": "PC"
        },
        {
            "id": 10,
            "title": "nokia",
            "cat": "PC"
        },
        {
            "id": 16,
            "title": "new obj 2 Update",
            "cat": "PC"
        }
    ]

for elem in lst:
    print(elem["cat"])
