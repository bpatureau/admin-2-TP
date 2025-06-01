flask
flask-cors
redis
mysql-connector-python
pika
guy@swarm-manager-1:~/tp10/TP10/woodytoys/services/api/order_service$ cat woody.py
# Voici les différentes fonctions que l'api de Woody pourrait utiliser
#
# Il y a beacoup de "sleep", et de ralentissement qui ont pour but de simuler une grosse charge et/ou
# pour simuler des requètes qui seraient (dans un cas réel) plus lourde..
#
# Ce fichier ne peut pas être modifié (du moins pas pour "fixer" les limitations qu'il introduit ;)
# ( ce fichier sera, à terme dans une lib externe pour rendre plus clair la séparation)


from mysql.connector import connect, Error


def my_connect():
    # note, c'est une mauvaise idée de recréer la connection à chaque requète
    # (c'est surtt pour une question de performance)
    # Mais ici, ce n'est pas la performance qu'on cherche ;)

    try:
        mydb = connect(host='db', user='root', password='pass', database='woody', port=3306)
        mycursor = mydb.cursor()
    except Error as e:
        print(e)
        return None, None
    return mydb, mycursor


def get_order(order_id):
    mydb, mycursor = my_connect()
    query = f"SELECT status FROM woody.order WHERE order_id='{order_id}';"

    mycursor.execute(query)

    order_status = mycursor.fetchone()

    mycursor.close()
    mydb.close()
    return order_status
