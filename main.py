from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, select
from models import User, Address

# datatabse in memory - does not exist after program finishes running
memory_engine = create_engine('sqlite:///:memory:', echo=True)

# database in filesystem - keeps existing
file_engine = create_engine('sqlite:///db.sqlite3', echo=True)


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

metadata.create_all(memory_engine)

metadata.create_all(file_engine)

# statements

my_user = User(name='PR', fullname='Pablo Rivera')
my_other_user = User(name='goishen', fullname='goishen the barbarian')

insert_user = users.insert().values(name=my_user.name, fullname=my_user.fullname)
insert_other_user = users.insert().values(name=my_other_user.name, fullname=my_other_user.fullname)

# execute insert statements statements

memory_conn = memory_engine.connect()

file_conn = file_engine.connect()

result_one = memory_conn.execute(insert_user)
result_two = memory_conn.execute(insert_other_user)

result_three = file_conn.execute(insert_user)
result_four = file_conn.execute(insert_other_user)

print(result_one.inserted_primary_key)
print(result_two.inserted_primary_key)
print(result_three.inserted_primary_key)
print(result_four.inserted_primary_key)



# execute select statements

select_users = select([users])
users_result = memory_conn.execute(select_users)

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


# select where

select_where = select([users]).where(users.c.name == my_other_user.name )

for row in memory_conn.execute(select_where):
    print(row)


# delete 

delete_where = users.delete().where(users.c.name == my_user.name)
memory_conn.execute(delete_where)


# select again to see that the user was deleted

select_users = select([users])
users_result = memory_conn.execute(select_users)

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



# check database in file

select_users = select([users])
users_result = file_conn.execute(select_users)

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