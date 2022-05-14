import psycopg2

connection = psycopg2.connect('dbname=postgres password=oyinlola host=localhost')

cursor = connection.cursor()

cursor.execute('Drop table if exists test')

cursor.execute('''
    create table Test(
        id int generated by default as identity primary key,
        details varchar,
        date_created timestamp
    );

''')

cursor.execute('''

insert into Test(details, date_created)
values('First Test',now()),('Second Test',(select now() + interval '1 hour'));

''')

sql_Template = 'insert into Test(details, date_created) values(%s, %s);'

cursor.execute(sql_Template,('Third Test', '2022-05-17 00:20:09.751066'))

data = {
    'details': 'Fourth Test',
    'date_created': '2022-05-18 00:20:09.751066'
}

cursor.execute('''

insert into Test(details, date_created)
values(%(details)s, %(date_created)s);

''',data)

connection.commit()
connection.close()
