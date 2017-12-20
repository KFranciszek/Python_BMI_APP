import psycopg2
from dicBMI  import team

try:
    for bmiDic  in team:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgresq123'")
        print("Dobre połączenie do bazy postgres")
        cur = conn.cursor()
        cur.execute("""INSERT INTO bmi(name,weight,height,bmi) VALUES (%(name)s,%(weight)s, %(height)s,%(bmi)s)""", bmiDic)
        # cur.execute("INSERT INTO public.bmi (name) VALUES  ((weight))", dict[bmiDic])
        conn.commit()
        cur.close()

except:
    print ("I am unable to connect to the database")
