import psycopg2

symbol =['!','@',"#","$","%","&","*","/","?"]
def account ():

    login = str(input("Your email"))

    while True:
        password = str(input("Your paswords, Must have 6 char, big lliter, special symbol"))
        if len(password)  < 6:
            print("Pasword must have minimum 6")

        elif sum(1 for i in password if i.isupper()) < 1:
            print("Password must have one big litter")
        elif sum(1 for i in password if i in symbol) < 1:
            print("Password must have special symbol")
        else:
            break

    conn = psycopg2.connect("dbname='postgres' user='xyz' host='localhost' password='xyz'")
    print("Succes connect")
    cur = conn.cursor()
    cur.execute("""INSERT INTO users(login, password) VALUES (%(login)s,%(password)s)""",
                {'login': login, 'password': password})
    conn.commit()
    cur.close()
    # except:

account()
