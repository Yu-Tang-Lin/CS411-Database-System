import pymysql

db = pymysql.connect(host='localhost',
                user='root',
                password='zy749097',
                database='academicworld',
                charset='utf8mb4',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor)


def get_university(input_value):
    with db.cursor() as cursor:
        sql = 'select id, name from university where name like "%' + input_value + '%";'

        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()

        print(result)
        return result

def faculty_count(input_value):
   with db.cursor() as cursor:
       sql = """
       SELECT COUNT(u.name) AS count1, u.name
       FROM faculty f
       INNER JOIN university u ON f.university_id = u.id
       WHERE u.name like "%""" + input_value + '%"  GROUP BY u.name;'
       cursor.execute(sql)
       result = cursor.fetchall()
       print(result)
       return result

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

def publication_count_year(input_value,yr):
    with db.cursor() as cursor:
        sql = """
            select u.name, count(p.id) as count4 from faculty f
            inner join university u on u.id=f.university_id
            inner join faculty_publication fp on f.id=fp.faculty_id
            inner join publication p on fp.publication_id=p.id
            where u.name like "%"""+ input_value + '%" and p.year between 0 and ' +str(yr)+ ' group by u.name ;'

        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        return result

#input_value = 'University of Rochester'
#result = get_university(input_value)
#select id, name from university where name like "%University of Rochester%";
#result = publication_count(input_value)
#result = publication_count_year(input_value,yr=2000)