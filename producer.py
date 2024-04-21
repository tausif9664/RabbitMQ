import pika,time,random

canect_para = pika.ConnectionParameters('localhost')

conn = pika.BlockingConnection(canect_para)

channel = conn.channel()

channel.queue_declare(queue='letterbox')
message_id = 1
while(True):
    message = f"{message_id}"

    channel.basic_publish(exchange='', routing_key='letterbox', body= message)
    print(f"sent message:{message}")
    time.sleep(random.randint(1,4))
    message_id +=1
