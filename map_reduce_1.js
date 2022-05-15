// *** 3T Software Labs, Studio 3T: MapReduce Job ****

// Variable for db
var __3tsoftwarelabs_db = "ecbd";

// Variable for map
var __3tsoftwarelabs_map = function () {
    emit(this.user, this.likes);
}
;

// Variable for reduce
var __3tsoftwarelabs_reduce = function (keys, values) {
    let sum = 0;
    for (const value of values) {
        sum += value;
    }

    return sum;
}
;

db.runCommand({ 
    mapReduce: "comments",
    map: __3tsoftwarelabs_map,
    reduce: __3tsoftwarelabs_reduce,
    out: {"inline": 1},
    query: { "sent_at" : { "$gt" : ISODate("2022-01-01T00:00:00.000+0000") }},
    inputDB: "ecbd",
 });

// numarul de like-uri per canal, pentru acele like-uri trimise dupa 01.01.2022