from main import app
from models import *
from main import *


def categorydata(data):
    for c in data:
        cat = Category(c)
        cat.save()


def ncount(n, d):
    itemdat = Item('Colorful Stylish Shirt', '150.00', '200.00', f"../static/img/pr-{n}.webp", n, n, d)
    return itemdat


def itemdata(discript):
   for i in range(4, 9):
        itmd = ncount(i, discript)
        itmd.save()
        

d =  '''<p>
            Eos no lorem eirmod diam diam, eos elitr et gubergren diam sea.
            Consetetur vero aliquyam invidunt duo dolores et duo sit. Vero
            diam ea vero et dolore rebum, dolor rebum eirmod consetetur
            invidunt sed sed et, lorem duo et eos elitr, sadipscing kasd
            ipsum rebum diam. Dolore diam stet rebum sed tempor kasd eirmod.
            Takimata kasd ipsum accusam sadipscing, eos dolores sit no ut
            diam consetetur duo justo est, sit sanctus diam tempor aliquyam
            eirmod nonumy rebum dolor accusam, ipsum kasd eos consetetur at
            sit rebum, diam kasd invidunt tempor lorem, ipsum lorem elitr
            sanctus eirmod takimata dolor ea invidunt.
        </p>
        <p>
            Dolore magna est eirmod sanctus dolor, amet diam et eirmod et
            ipsum. Amet dolore tempor consetetur sed lorem dolor sit lorem
            tempor. Gubergren amet amet labore sadipscing clita clita diam
            clita. Sea amet et sed ipsum lorem elitr et, amet et labore
            voluptua sit rebum. Ea erat sed et diam takimata sed justo.
            Magna takimata justo et amet magna et.
        </p>'''
catdata = ['Shirts', 'Jeans', 'Swimwear', 'Sleepwear', 'Sportswear', 'Jumpsuits', 'Blazers', 'Jackets', 'Shoes']


def datarecord():
    categorydata(catdata)
    itemdata(d)

with app.app_context():
    item = Item('Colorful Stylish Sweaters pink', '200.00', '300.00', "../static/img/pr-8.webp", 3, 11, d)
    item.save()
    # item = Item()
