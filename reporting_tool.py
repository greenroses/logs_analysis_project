#!/usr/bin/env python3

import psycopg2

# Most popular 3 articles
sql_command_1 = """
select title, count(*) as num
from articles, log
where log.path = CONCAT('/article/', articles.slug)
group by title
order by num desc
limit 3;"""

# Most popular 3 authors
sql_command_2 = """
select name, count(*) as num
from log,
    (select name, slug
        from articles, authors
        where articles.author = authors.id) as authors_articles
where log.path = CONCAT('/article/', authors_articles.slug)
group by name
order by num desc
limit 3;"""

# on Which days did more than 1% of requests lead to errors.
sql_command_3 = """
select date, cast(round(error * 100.0 / total, 2) as decimal(5,2)) as percent
from (select date,
        count(*) total,
        sum(case when status like '4%' then 1 else 0 end) error
        from (select to_char(time, 'YYYY-MM-DD') as date, status
            from log) as date_log
        group by date) as date_count
where (error * 1.0 / total) > 0.01;"""


db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(sql_command_1)
rows_1 = c.fetchall()
f = open('report.txt', 'w')
f.write('1. What are the most popular three articles of all time?\n')
for row in rows_1:
    f.write('  ' + u'\u2022 "' + row[0] + '" - ' + str(row[1]) + ' views\n')
c.execute(sql_command_2)
rows_2 = c.fetchall()
f.write('2. Who are the most popular article authors of all time?\n')
for row in rows_2:
    f.write('  ' + u'\u2022 ' + row[0] + ' - ' + str(row[1]) + ' views\n')
c.execute(sql_command_3)
rows_3 = c.fetchall()
f.write('3. On which days did more than 1% of requests lead to errors?\n')
for row in rows_3:
    f.write('  ' + u'\u2022 ' + row[0] + ' - ' + str(row[1]) + '% errors\n')
f.close()
db.close()
