from kafka.admin import KafkaAdminClient, NewTopic
from configs import kafka_config

topic_names = ["building_sensors", "temperature_alerts", "humidity_alerts"]

admin_client = KafkaAdminClient(
    bootstrap_servers=kafka_config["bootstrap_servers"],
    security_protocol=kafka_config["security_protocol"],
    sasl_mechanism=kafka_config["sasl_mechanism"],
    sasl_plain_username=kafka_config["username"],
    sasl_plain_password=kafka_config["password"]
)

topics ={topic: NewTopic(name=topic, num_partitions=2, replication_factor=1) for topic in topic_names}

try:

except Exception as e:
    print()