#! /usr/bin/env python3
import psycopg2

# Database
DBNAME = "news"

try:
    db = psycopg2.connect(database=DBNAME)
except psycopg2.DatabaseError as e:
    print("error connecting to database")
c = db.cursor()


# Query 1 :  The most popular three articles of all time
query1 = "SELECT path, count(path)\
          FROM log join new_articles\
            ON log.path = new_articles.concat\
            GROUP BY path order by count(path) desc limit 3"
# Title for query 1
title1 = "\n1:What are the most popular three articles of all time? \n "


# Query 2: The most popular article authors of all time
query2 = ("SELECT name, sum(count)\
            FROM authors a inner join new_articles n\
             ON a.id = n.author\
              INNER JOIN view2 v\
               ON v.path = n.concat\
                GROUP BY a.name\
                 ORDER BY sum(count) desc;")
# Title for query 2
title2 = "\n2. Who are the most popular article authors of all time? \n"


# Query 3 :  On which days did more than 1% of requests lead to errors
query3 = ("SELECT num_errors.date,(error*1.0/total_requests)*100 as percent_errors\
            FROM num_errors join num_requests\
             ON num_errors.date = num_requests.date\
              WHERE (error*1.0/total_requests)*100>1.0;")
# Title for query 2
title3 = "\n3. On which days did more than 1% of requests lead to errors?  \n"


def query_get(query):
    """
    Connects to the database and executes the query
        Takes the query as argument
        and returns the results from the 'database'.
    """
    db = psycopg2.connect(dbname=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def format_output(raw_data):
    """
    Formats the raw data
      Takes the query_result in array format as argument
      and returns the fFormatted result in form of string.
    """
    for i in range(len(raw_data)):
        print(raw_data[i][0] + ' -- ' + str(raw_data[i][1]) + ' views')


def format_output_query3(raw_data):
    """
    Formats the raw data
      Takes the query_result in array format as argument
      and returns the fFormatted result in form of string.
    """
    for i in range(len(raw_data)):
        print(str(raw_data[i][0]) + ' -- ' + str(raw_data[i][1]) + ' %')


# execution
if __name__ == '__main__':
    query_result1 = query_get(query1)
    query_result2 = query_get(query2)
    query_result3 = query_get(query3)

    # print formatted data
    print(title1)
    format_output(query_result1)
    print("-" * 70)
    print(title2)
    format_output(query_result2)
    print("-" * 70)
    print(title3)
    format_output_query3(query_result3)
    print("-" * 70)

db.close()
