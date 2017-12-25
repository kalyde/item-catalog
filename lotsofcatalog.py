from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, MenuItem, User

engine = create_engine('sqlite:///catalogwithusers.db')
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
category1 = Category(user_id=1, name="Audio")

session.add(category1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Speakers", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Headphones", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Home Theatre System", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="CD Player", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="iPod", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category1)

session.add(menuItem5)
session.commit()


# Menu for Cameras
category2 = Category(user_id=1, name="Cameras")

session.add(category2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Digital SLR Camera", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category2)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Camera Lens", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Instant Print Camera", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Memory Card", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Flash", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category2)

session.add(menuItem5)
session.commit()


# Menu for Computers
category3 = Category(user_id=1, name="Computers")

session.add(category3)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Desktop", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category3)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Laptop", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Monitor", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Software", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Keyboard", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category3)

session.add(menuItem5)
session.commit()


# Menu for TV & Home Theater
category4 = Category(user_id=1, name="TV & Home Theater")

session.add(category4)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Smart TV", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category4)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="4K TV", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="TV Stand", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Remote Control", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Cables", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category4)

session.add(menuItem5)
session.commit()


# Menu for Video Games
category5 = Category(user_id=1, name="Video Games")

session.add(category5)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Playstation", description="Lorem ipsum dolor sit amet",
                     price="$7.50", category=category5)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Xbox", description="Lorem ipsum dolor sit amet",
                     price="$2.99", category=category5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Nintendo", description="Lorem ipsum dolor sit amet",
                     price="$5.50", category=category5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="PC Gaming", description="Lorem ipsum dolor sit amet",
                     price="$3.99", category=category5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Atari", description="Lorem ipsum dolor sit amet",
                     price="$7.99", category=category5)

session.add(menuItem5)
session.commit()


print "added menu items!"
