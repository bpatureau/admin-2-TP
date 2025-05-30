import pika
import json
import time
import sys
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Simulated external module with processing
class Woody:
    def make_heavy_validation(self, order):
        print(f"[~] Validating order for {order}...")
        time.sleep(5)  # Simulate slow process
        return "validated"

    def save_order(self, order_id, status, product):
        print(f"[✓] Order {order_id} ({product}) saved with status: {status}")

woody = Woody()

def process_order(order_id, product):
    # Simulated heavy logic
    status = woody.make_heavy_validation(product)
    woody.save_order(order_id, status, product)

def callback(ch, method, properties, body):
    data = json.loads(body)
    order_id = data.get("order_id")
    product = data.get("product")
    print(f"[x] Received order {order_id} for product {product}")
    process_order(order_id, product)

def connect_to_rabbitmq(max_retries=5, delay=3):
    """Tente de se connecter à RabbitMQ avec retry"""
    for attempt in range(max_retries):
        try:
            logger.info(f"Tentative de connexion {attempt + 1}/{max_retries}")
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='rabbitmq',
                    credentials=pika.PlainCredentials('user', 'password'),
                    heartbeat=600,
                    blocked_connection_timeout=300,
                )
            )
            logger.info("Connexion à RabbitMQ réussie !")
            return connection
        except (pika.exceptions.AMQPConnectionError, Exception) as e:
            logger.error(f"Erreur de connexion (tentative {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                logger.info(f"Nouvelle tentative dans {delay} secondes...")
                time.sleep(delay)
            else:
                logger.error("Impossible de se connecter à RabbitMQ après toutes les tentatives")
                sys.exit(1)

# Connexion avec retry
connection = connect_to_rabbitmq()
channel = connection.channel()

# Déclarer la queue (idempotent) - doit correspondre au service
channel.queue_declare(queue='order_queue', durable=False)

# Configuration du consumer
channel.basic_consume(queue='order_queue', on_message_callback=callback, auto_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('[!] Interrupted')
    channel.stop_consuming()
    connection.close()