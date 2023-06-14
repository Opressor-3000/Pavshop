from models import Category, Item


def categorydata(data):
    for c in data:
        cat = Category(c)
        cat.save()


def ncount(n, d):
    itemdat = ('Colorful Stylish Shirt', '150.00', '200.00', f"../static/img/pr-{n}.webp", n, n, d)
    return itemdat


def itemdata(discript):
   for i in range(1, 9):
        ncoun = ncount(i, discript)
        itmd = Item(ncoun)
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
