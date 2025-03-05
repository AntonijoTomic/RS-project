from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])  # Lokalni host
session = cluster.connect()

session.set_keyspace('system')
rows = session.execute('SELECT release_version FROM system.local')
for row in rows:
    print(f"Cassandra verzija: {row.release_version}")
