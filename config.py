import os

MONGO_CONN_URI = f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@" \
                 f"{os.getenv('MONGO_DB_HOST')}/{os.getenv('USED_MONGO_DB')}" \
                 f"?replicaSet={os.getenv('MONGO_DB_REPLICA_SET')}" \
    if os.getenv("MONGO_DB_URI") is None else os.getenv("MONGO_DB_URI")
