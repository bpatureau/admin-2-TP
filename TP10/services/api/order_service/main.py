from flask import Flask, request
import uuid
import pika
import json
import logging
import time

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def get_rabbitmq_connection(max_retries=3, delay=2):
    """Obtient une connexion RabbitMQ avec retry"""
    for attempt in range(max_retries):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='rabbitmq',
                    credentials=pika.PlainCredentials('user', 'password'),
                    heartbeat=600,
                    blocked_connection_timeout=300,
                )
            )
            return connection
        except Exception as e:
            logger.error(f"Tentative de connexion {attempt + 1}/{max_retries} échouée: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                logger.error("Impossible de se connecter à RabbitMQ")
                raise e

def publish_order(order_id, product):
    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()

        # Déclarer la queue (idempotent)
        channel.queue_declare(queue='order_queue', durable=False)

        message = {
            "order_id": order_id,
            "product": product
        }

        channel.basic_publish(
            exchange='',
            routing_key='order_queue',
            body=json.dumps(message)
        )

        logger.info(f"[x] Published order {order_id}")
        connection.close()
        return True

    except Exception as e:
        logger.error(f"Erreur lors de la publication: {e}")
        return False

@app.route('/api/orders/do', methods=['GET'])
def create_order():
    try:
        product = request.args.get('order')
        if not product:
            return "Paramètre 'order' manquant", 400

        order_id = str(uuid.uuid4())

        # Publier vers RabbitMQ
        success = publish_order(order_id, product)

        if success:
            return f"Your process {order_id} has been created with this product: {product}"
        else:
            return f"Erreur lors de la création de la commande", 500

    except Exception as e:
        logger.error(f"Erreur dans create_order: {e}")
        return f"Erreur serveur: {str(e)}", 500

@app.route('/health', methods=['GET'])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)