// *** 3T Software Labs, Studio 3T: MapReduce Job ****

// Variable for db
var __3tsoftwarelabs_db = "ecbd";

// Variable for map
var __3tsoftwarelabs_map = function () {
    this.channels.forEach(channel => emit(channel, 1));
}
;

// Variable for reduce
var __3tsoftwarelabs_reduce = function (key, values) {
    let count = 0;
    
    for ( const value of values ) {
        count += 1;
    }
    
    return count;
};

// Variable for finalize
var __3tsoftwarelabs_finalize = function (key, reducedValue) {
    return reducedValue * 10 / 500;
}
;

db.runCommand({ 
    mapReduce: "users",
    map: __3tsoftwarelabs_map,
    reduce: __3tsoftwarelabs_reduce,
    finalize: __3tsoftwarelabs_finalize,
    out: {"inline": 1},
    query: { },
    inputDB: "ecbd",
 });

// un scor care reprezinta cati utilizatori sunt abonati la un canal anume
// 10 -> 500 useri (hardcodat)
// 0 -> 0 useri
// fara finalize era o numarare a utilizatorilor abonati la fiecare canal