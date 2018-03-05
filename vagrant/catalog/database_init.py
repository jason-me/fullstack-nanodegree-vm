from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Location, CharityItem

engine = create_engine('sqlite:///charitablegoodswithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


locations = [
    ['Austin, TX',
        [{'name': 'toothbrush',
          'description': '4 Pack Colgate Disposable Toothbrush',
          'quantity': '2000',
          'good': 'toiletries'},
         {'name': 'toilet paper',
          'description': '8 pack charmin ultra soft 3 ply toilet paper',
          'quantity': '3500',
          'good': 'toiletries'},
         {'name': 'Bar Soap',
          'description': '12 Pack Dove Skin Care bar soap',
          'quantity': '8900',
          'good': 'toiletries'},
         {'name': 'Wool Blanket',
          'description': '8x5 government issue wool blanket',
          'quantity': '10000',
          'good': 'bedding'}]],
    ['Beaumont, TX',
        [{'name': 'Bottled Water',
          'description': '36 Pack Ozarka Spring Water 16 fl oz.',
          'quantity': '4500',
          'good': 'non-perishables'},
         {'name': 'AA Batteries',
          'description': '8 pack energizer AA batteries',
          'quantity': '1600',
          'good': 'electronics'},
         {'name': 'Emergency Radio',
          'description': 'AM/FM/SW Belkin - Weather radio',
          'quantity': '1200',
          'good': 'electronics'},
         {'name': 'Flashlight',
          'description': 'LED Enerbright 1000W flashlight',
          'quantity': '5000',
          'good': 'electronics'}]],
    ['Conroe, TX',
        [{'name': 'Bottled Water',
          'description': '36 Pack Ozarka Spring Water 16 fl oz.',
          'quantity': '500',
          'good': 'non-perishables'},
         {'name': 'Pillow',
          'description': 'Single adult size cotton pillow',
          'quantity': '2000',
          'good': 'bedding'},
         {'name': 'Mens Socks',
          'description': '6 pack hanes black tube socks large mens',
          'quantity': '750',
          'good': 'clothing'},
         {'name': 'Womens Briefs',
          'description': '3 Pack womens brief underwear large',
          'quantity': '1100',
          'good': 'clothing'}]],
    ['Houston, TX',
        [{'name': 'Trash Bags',
          'description': '50 pack Hefty industrial 30 gal trash bags',
          'quantity': '10000',
          'good': 'cleaning'},
         {'name': 'Mop',
          'description': 'Great Value cotton braid idustrial floor mop',
          'quantity': '50000',
          'good': 'cleaning'},
         {'name': 'D Batteries',
          'description': '6 pack Duracell size D batteries',
          'quantity': '9700',
          'good': 'electronics'},
         {'name': 'T-shirts',
          'description': '4 ct Froot of the Loom unisex large white t-shirts',
          'quantity': '30000',
          'good': 'clothing'}]],
    ['Rockport, TX',
        [{'name': 'Generator',
          'description': 'Duromax 4,000 watt gas generator',
          'quantity': '700',
          'good': 'construction'},
         {'name': 'Rags',
          'description': '50 pack lighthouse for the blind resale rags',
          'quantity': '500',
          'good': 'cleaning'},
         {'name': 'Canned Soup',
          'description': '12 pack Multi-flavor Campbells Soup',
          'quantity': '10000',
          'good': 'non-perishables'},
         {'name': 'Tuna Fish',
          'description': '3 pack can Starkist tuna 3.5 oz',
          'quantity': '500',
          'good': 'non-perishables'}]]
]

current_user = User(name="Jason Hester", email="mail@jason-hester.me")
session.add(current_user)
session.commit()

for location in locations:
    current_location = Location(name=location[0], user=current_user)
    session.add(current_location)
    session.commit()

    for charityitem in location[1]:
        current_charityitem = CharityItem(
                              name=charityitem['name'],
                              description=charityitem['description'],
                              quantity=charityitem['quantity'],
                              good=charityitem['good'],
                              location=current_location,
                              user=current_user)
        session.add(current_charityitem)
        session.commit()
