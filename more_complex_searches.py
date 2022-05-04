from pymongo import DESCENDING
from mongo_handler import MongoHandler
from datetime import datetime

handler = MongoHandler("ecbd")
user_collection = handler.get_collection("users")
channel_collection = handler.get_collection("channels")
comment_collection = handler.get_collection("comments")


def print_output_separator():
    print("\n\n#####################################")


# nr de like-uri pe fiecare canal
print(list(comment_collection.aggregate([
    {"$group": {"_id": "$channel", "total_likes": {"$sum": "$likes"}}},
])))

# nr de like-uri pe fiecare canal + datele efective ale canalului
print(list(comment_collection.aggregate([
    {
        "$lookup":
            {
                "from": "channels",
                "localField": "channel",
                "foreignField": "_id",
                "as": "ch"
            }
    },
    {"$group": {"_id": "$ch", "total_likes": {"$sum": "$likes"}}},
])))

# nr de like-uri al fiecarui utilizator + lookup + proiectie + sortare descendenta
print(list(comment_collection.aggregate([
    {
        "$lookup":
            {
                "from": "users",
                "localField": "user",
                "foreignField": "_id",
                "as": "user_doc"
            }
    },
    {"$group": {"_id": "$user_doc", "total_likes": {"$sum": "$likes"}}},
    {"$project": {"_id.first_name": 1, "_id.last_name": 1, "total_likes": 1}},
    {"$sort": {"total_likes": -1}}
])))

# nr de like-uri al fiecarui utilizator pe fiecare canal + lookup + proiectie + sortare descendenta
print_output_separator()
print(list(comment_collection.aggregate([
    {
        "$lookup":
            {
                "from": "users",
                "localField": "user",
                "foreignField": "_id",
                "as": "user_doc"
            }
    },
    {
        "$lookup":
            {
                "from": "channels",
                "localField": "channel",
                "foreignField": "_id",
                "as": "channel_doc"
            }
    },
    {"$group": {"_id": {"channel": "$channel_doc", "user": "$user_doc"}, "total_likes": {"$sum": "$likes"}}},
    {"$project": {"_id.user.first_name": 1, "_id.user.last_name": 1, "_id.channel.name": 1, "total_likes": 1}},
    {"$sort": {"total_likes": -1}}
])))

# sau numarul efectiv de comentarii al fiecarui user pe fiecare canal + lookup + proiectie + sortare descendenta
print_output_separator()
print(list(comment_collection.aggregate([
    {
        "$lookup":
            {
                "from": "users",
                "localField": "user",
                "foreignField": "_id",
                "as": "user_doc"
            }
    },
    {
        "$lookup":
            {
                "from": "channels",
                "localField": "channel",
                "foreignField": "_id",
                "as": "channel_doc"
            }
    },
    {"$group": {"_id": {"channel": "$channel_doc", "user": "$user_doc"}, "total_comments": {"$sum": 1}}},
    {"$project": {"_id.user.first_name": 1, "_id.user.last_name": 1, "_id.channel.name": 1, "total_comments": 1}},
    {"$sort": {"total_comments": -1}}
])))

# toate fosturile joburi ale angajatilor ordonate alfabetic
print_output_separator()
print(list(user_collection.aggregate([
    {
        "$unwind": "$ex_jobs"
    },
    {
        "$project": {
            "ex_jobs.name": 1
        }
    },
    {
        "$group": {"_id": "$ex_jobs.name"}
    },
    {
        "$sort": {"_id": 1}
    }
])))
