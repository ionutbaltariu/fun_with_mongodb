import sys
from mongo_handler import MongoHandler
from datetime import datetime

handler = MongoHandler("ecbd")
user_collection = handler.get_collection("users")
channel_collection = handler.get_collection("channels")
comment_collection = handler.get_collection("comments")


# stergem tot
def delete_all() -> None:
    user_collection.delete_many({})
    channel_collection.delete_many({})
    comment_collection.delete_many({})


# stergem comentarii vechi
comment_collection.delete_many(
    {"sent_at": {"$lt": datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0).replace(microsecond=0)}})

# stergem comentarii nepopulare
comment_collection.delete_many({"likes": {"$lte": 100}})

# stergem canale vechi
channel_collection.delete_many({"meta.archived": True})

# stergem utilizatori care au mai putin de un an (inclusiv) experienta la jobul curent
user_collection.delete_many({"current_job.years_of_experience": {"$lte": 1}})

if sys.argv[1] == "all":
    delete_all()
