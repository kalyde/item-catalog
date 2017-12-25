from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, MenuItem

engine = create_engine('sqlite:///catalog1.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for Audio
category1 = Category(name="Audio")

session.add(category1)
session.commit()

menuItem1 = MenuItem(name="Speakers", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="Headphones", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Home Theatre System", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="CD Player", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="iPod", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category1)

session.add(menuItem5)
session.commit()


# Menu for Cameras
category2 = Category(name="Cameras")

session.add(category2)
session.commit()


menuItem1 = MenuItem(name="Digital SLR Camera", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category2)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="Camera Lens", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Instant Print Camera", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Memory Card", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Flash", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category2)

session.add(menuItem5)
session.commit()


# Menu for Computers
category3 = Category(name="Computers")

session.add(category3)
session.commit()


menuItem1 = MenuItem(name="Desktop", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category3)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="Laptop", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Monitor", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Software", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Keyboard", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category3)

session.add(menuItem5)
session.commit()


# Menu for TV & Home Theater
category4 = Category(name="TV & Home Theater")

session.add(category4)
session.commit()


menuItem1 = MenuItem(name="Smart TV", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category4)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="4K TV", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="TV Stand", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Remote Control", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Cables", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category4)

session.add(menuItem5)
session.commit()


# Menu for Video Games
category5 = Category(name="Video Games")

session.add(category5)
session.commit()


menuItem1 = MenuItem(name="Playstation", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category5)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="Xbox", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Nintendo", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="PC Gaming", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Atari", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category5)

session.add(menuItem5)
session.commit()


print "added menu items!"