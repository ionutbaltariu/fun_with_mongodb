from mongo_handler import MongoHandler
from datetime import datetime
from fake_data_gen import get_fake_users
from pymongo import InsertOne, DeleteMany, UpdateMany, UpdateOne

handler = MongoHandler("ecbd")
user_collection = handler.get_collection("users")
channel_collection = handler.get_collection("channels")
comment_collection = handler.get_collection("comments")

channel_ids = [x["_id"] for x in channel_collection.find({})]

user_collection.bulk_write([
    DeleteMany({"current_job.years_of_experience": {"$lte": 1}}),
    InsertOne(get_fake_users(channel_ids, 1)[0]),
    InsertOne(get_fake_users(channel_ids, 1)[0]),
    UpdateMany({"personal_information.zodiac": "Gemini"}, {"$set": {"personal_information.zodiac": "N/A"}}),
    UpdateMany({"ex_jobs.company": "Popa"}, {"$set": {"ex_jobs.$.company": "S.C Popa Industries SRL"}}),
    InsertOne(get_fake_users(channel_ids, 1)[0]),
    InsertOne(get_fake_users(channel_ids, 1)[0]),
    UpdateOne({"first_name": "Loredana"}, {"$set": {"first_name": "Bulk Ops Test"}})
])

channel_collection.bulk_write([
    InsertOne({
        "name": "#teambuilding-2022",
        "type": "public",
        "creation_date": datetime(year=2022, month=3, day=25, hour=8, minute=32, second=58).replace(microsecond=0),
        "meta": {
            "archived": True
        }
    }),
    DeleteMany({"meta.archived": True}),
    UpdateMany({"type": "private"}, {"$set": {"type": "public"}})
])
