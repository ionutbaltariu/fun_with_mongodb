// *** 3T Software Labs, Studio 3T: MapReduce Job ****

// Variable for db
var __3tsoftwarelabs_db = "ecbd";

// Variable for map
var __3tsoftwarelabs_map = function () {
    this.channels.forEach( channel => emit(this.first_name + " " + this.last_name, channel));
}
;

// Variable for reduce
var __3tsoftwarelabs_reduce = function (key, values) {
    let count = 0;
    
    for ( const value of values ) {
        count += 1;
    }
    
    return count;
}
;

db.runCommand({ 
    mapReduce: "users",
    map: __3tsoftwarelabs_map,
    reduce: __3tsoftwarelabs_reduce,
    out: {"inline": 1},
    query: {  "current_job.years_of_experience" : { "$gte" : 2 }},
    inputDB: "ecbd",
 });

// numarul de canale la care sunt abonati utilizatorii cu cel putin 2 ani de experienta la jobul curent