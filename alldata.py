from main import db
from models import Category, Item



def categorydata(data):
    for c in data:
        cat = Category(c)
        db.session.add(cat)
        db.session.commit()



def itemdata(data):
   for i in range(10):
      for t, p, op, q, c, d in data:
         item = Item(t, p, op, q, c, d)
         db.session.add(item)
         db.session.commit()
        




'''


title         
price        150.00
oldprice     200.00
image        "../static/img/pr-' + {n} + '.webp"
quantity     n
category_id  n
description  'Volup erat ipsum diam elitr rebum et dolor. Est nonumy elitr erat
             diam stet sit clita ea. Sanc invidunt ipsum et, labore clita lorem
             magna lorem ut. Erat lorem duo dolor no sea nonumy. Accus labore
             stet, est lorem sit diam sea et justo, amet at lorem et eirmod ipsum
             diam et rebum kasd rebum.

            <p>
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
            </p>'


title        Colorful Stylish Shirt
price        $123.00
image        ../static/img/pr-1.webp
quantity     
description  
category     Shirt


title        Colorful Stylish Shirt
price        123
image        ../static/img/pr-2.webp
quantity     
description  
category     Shirt
'''