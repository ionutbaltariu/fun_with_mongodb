from mongo_handler import MongoHandler
from datetime import datetime

handler = MongoHandler("ecbd")
user_collection = handler.get_collection("users")
channel_collection = handler.get_collection("channels")
comment_collection = handler.get_collection("comments")

# update la tipul canalului
channel_collection.update_one({"name": "#teambuilding-2020"}, {"$set": {"type": "private"}})

# toate comentariile dupa 31-05-2020 vor avea 0 likes
comment_collection.update_many(
    {"sent_at": {"$gt": datetime(year=2020, month=5, day=31, hour=0, minute=0, second=0).replace(microsecond=0)}},
    {"$set": {"likes": 0}})

# toti userii cu zodia gemeni nu cred in zodii
user_collection.update_many({"personal_information.zodiac": "Gemini"},
                            {"$set": {"personal_information.zodiac": "N/A"}})

# fiecare companie "Popa" din toate "ex_jobs" se va transforma in "S.C Popa Industries SRL" (user)
user_collection.update_many({"ex_jobs.company": "Popa"},
                            {"$set": {"ex_jobs.$.company": "S.C Popa Industries SRL"}})

# situatia tuturor utilizatorilor intr-un cuplu se va considera necunoscuta
user_collection.update_many({"personal_information.relationship_status": "in a couple"},
                            {"$set": {"personal_information.relationship_status": "N/A"}})
