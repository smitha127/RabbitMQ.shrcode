import pika
from Automation.rabbitmq.scrapy import card
from Automation.rabbitmq.ServiceVo import ServiceVo

class producer:
    #object = repositry()
    asd = object.objetcreation()
    for asd1 in card_Details_data:
       assert isinstance(asd1._dict_, object)
       asd2 = json.dumps(asd1._dict_)
       connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
       channel = connection.channel()
       channel.queue_declare(queue="cards")
       channel.basic_publish(exchange='', routing_key='cards', body=asd2)
       print("[x] Card Details are successfuly sent to queue")
       connection.close()

