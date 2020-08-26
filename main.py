from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, select
from models import User, Address

engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
)

metadata.create_all(engine)

# statements

my_user = User(name='PR', fullname='Pablo Rivera')
my_other_user = User(name='goishen', fullname='goishen the barbarian')

insert_user = users.insert().values(name=my_user.name, fullname=my_user.fullname)
insert_other_user = users.insert().values(name=my_other_user.name, fullname=my_other_user.fullname)

# execute insert statements statements

conn = engine.connect()

result_one = conn.execute(insert_user)
result_two = conn.execute(insert_other_user)

print(result_one.inserted_primary_key)
print(result_two.inserted_primary_key)


# execute select statements

select_users = select([users])
users_result = conn.execute(select_users)

users_list = []
for row in users_result:
    users_list.append(
        User(
            id=row[0],
            name=row[1],
            fullname=row[2]
        )
    )

for my_list_user in users_list:
    print(my_list_user.id, my_list_user.name, my_list_user.fullname)