class Settings:
    CASSANDRA_HOSTS = ["127.0.0.1"]  # Možeš dodati više nodova ako treba
    CASSANDRA_PORT = 9042
    CASSANDRA_KEYSPACE = "warehouse"  # Novi keyspace naziv
    
    DEBUG = True  # Možeš postaviti na False u produkciji

settings = Settings()
