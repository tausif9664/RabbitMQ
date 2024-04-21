import pika
import time
import random
from mongo_connect import mongo_connection


def on_msg_recived(ch, method, properties, body):
    processing_time = random.randint(1,6)
    data = f"received new message:{body},will take {processing_time}"
    print(f"received new message:{body},will take {processing_time}")
    mongo_connection(f"{body}",data)
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Fineshed Process")

canect_para = pika.ConnectionParameters('localhost')

conn = pika.BlockingConnection(canect_para)

channel = conn.channel()

channel.queue_declare(queue='letterbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox',
 on_message_callback= on_msg_recived)

print("starting Consuming")
channel.start_consuming()