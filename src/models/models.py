from sqlalchemy import Integer, String, MetaData, ForeignKey, TIMESTAMP, Table, Column, Boolean, CheckConstraint

metadata = MetaData()


type_room = Table(
    'type_room',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

room = Table(
    'room',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('price', String, nullable=False),
    Column('is_booking', Boolean, default=False),
    Column('guests', Integer, CheckConstraint('guests>=1 AND guests<=6')),
    Column('type_id', Integer, ForeignKey(type_room.c.id)),
)

service = Table(
    'service',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String, nullable=False),
    Column('lastname', String, nullable=False),
    Column('room_id', Integer, ForeignKey(room.c.id)),
    Column('email', String(length=320), unique=True, index=True, nullable=False),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)

reviews = Table(
    'reviews',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', Integer, ForeignKey(user.c.id)),
    Column('description', String, nullable=False),
    Column('estimate', Integer, CheckConstraint('estimate >= 1 AND estimate <= 5')),
)

cart = Table(
    'cart',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey(user.c.id)),
)

booking = Table(
    'booking',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey(user.c.id)),
    Column('room_id', Integer, ForeignKey(room.c.id)),
    Column('arrival', TIMESTAMP),
    Column('departure', TIMESTAMP)
)