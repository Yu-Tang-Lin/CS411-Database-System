import pymysql
#import mysql.connector


db = pymysql.connect(host='localhost',
                user='root',
                password='test_root',
                database='academicworld',
                charset='utf8mb4',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor)


#question a
def faculty_count(input_value):
   with db.cursor() as cursor:
       sql = """
       SELECT COUNT(u.name) AS count1, u.name
       FROM faculty f
       INNER JOIN university u ON f.university_id = u.id
       WHERE u.name like "%""" + input_value + '%"  GROUP BY u.name;'
       cursor.execute(sql)
       result = cursor.fetchall()
       # Implement index for faculty count 
       sql2=' DROP INDEX  IF EXISTS faculty_email_index ON faculty; '
       sql3='CREATE INDEX faculty_email_index ON faculty (email);'
       #cursor.execute(sql2)
       #cursor.execute(sql3)
       return result

#question b
def publication_count(input_value):
    with db.cursor() as cursor:
        sql = """
            select u.name, count(p.id) as count3 from faculty f
            inner join university u on u.id=f.university_id
            inner join faculty_publication fp on f.id=fp.faculty_id
            inner join publication p on fp.publication_id=p.id
            where u.name like "%"""+ input_value + '%" group by u.name ;'

        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        #print(result)
        return result

#question c


def insert_keyword(keyword_id, keyword):
    with db.cursor() as cursor:

        # SQL query to insert a new keyword into the 'keyword' table
        sql = """
        INSERT INTO keyword (id, name)
        VALUES (%s, %s)        
        """
        # Execute the query with parameters
        cursor.execute(sql, (keyword_id, keyword))
        # Commit the changes to the database
        db.commit()
        # Print the number of affected rows (should be 1)
        print(f"Inserted {cursor.rowcount} row(s).")
        print(f"add keyword",keyword )
        with db.cursor() as cursor:
            sql2 = """
             SELECT count(DISTINCT k.id) AS keyword_inserted_amount
             FROM keyword k;
             """
            cursor.execute(sql2)
            result = cursor.fetchall()
        # Return the last inserted ID
        return result


# adding constraint for unique keyword name
def add_constraint():
    with db.cursor() as cursor:
        # Add unique constraint for keyword name
        unique_keyword_name = """
        ALTER TABLE keyword
        ADD CONSTRAINT keyword_name_unique UNIQUE (name)
        """
        cursor.execute(unique_keyword_name)

        # Commit the changes to the database
        db.commit()
#constraint = add_constraint()

#question d
def delete_keyword( keyword):
    with db.cursor() as cursor:
        # SQL query to delete a row from the 'keyword' table based on the ID and name
        sql = """
        DELETE FROM keyword
        WHERE name = %s
        """
        # Execute the query with parameters
        cursor.execute(sql, ( keyword))
        # Commit the changes to the database
        db.commit()
        # Print the number of affected rows (should be 1)
        print(f"Deleted {cursor.rowcount} row(s).")
        print(f"delete keyword",keyword )
        # Return the number of deleted rows
        with db.cursor() as cursor:
            sql2 = """
             SELECT count(DISTINCT k.id) AS keyword_deleted_amount 
             FROM keyword k;
             """
            cursor.execute(sql2)
            result = cursor.fetchall()
        # Return the last inserted ID
        return result


"""
### Testing code
result = insert_keyword(keyword_id, keyword)
print(result)
result = delete_keyword( keyword)
print(result)
input_value = 'University of Rochester'
result = get_university(input_value)
select id, name from university where name like "%University of Rochester%";
result = publication_count(input_value)
result = publication_count_year(input_value,yr=2000)
#keyword_id = 1596911121
#keyword = 'meow'
"""


"""def get_university(input_value):
    with db.cursor() as cursor:
        sql = 'select id, name from university where name like "%' + input_value + '%";'

        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()

        print(result)
        return result"""

'''
def keyword_count(input_value):
   with db.cursor() as cursor:
       sql = """
       SELECT u.name, count(DISTINCT k.id) AS count2
       FROM faculty f
       INNER JOIN university u ON u.id=f.university_id
       INNER JOIN faculty_keyword fk ON f.id=fk.faculty_id
       INNER JOIN keyword k ON k.id=fk.keyword_id
       WHERE u.name like "%""" + input_value + '%" GROUP BY u.name ;'
       cursor.execute(sql)
       result = cursor.fetchall()
       print(result)
       return result

     
       
def publication_count_year(input_value,yr=2023):
    with db.cursor() as cursor:
        sql = """
            select u.name, count(p.id) as count4 from faculty f
            inner join university u on u.id=f.university_id
            inner join faculty_publication fp on f.id=fp.faculty_id
            inner join publication p on fp.publication_id=p.id
            where u.name like "%"""+ input_value + '%" and p.year between 0 and ' +str(yr)+ ' group by u.name ;'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

'''
