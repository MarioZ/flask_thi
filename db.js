exams
/* 0 */
{
    "_id" : ObjectId("52a6f2280312daa75dc156be"),
    "link" : "exam1",
    "name" : "K� thi s? 1",
    "content" : "Chua c�",
    "question" : 2,
    "duration" : 30,
    "deadline" : ISODate("2013-12-24T00:00:00.000Z"),
    "status" : true
}

/* 1 */
{
    "_id" : ObjectId("52a743acc0757ccee4628aa3"),
    "link" : "exam2",
    "name" : "K� thi s? 2",
    "content" : "Chua c�",
    "question" : 2,
    "duration" : 60,
    "deadline" : ISODate("2013-12-10T00:00:00.000Z"),
    "status" : true
}

makes
/* 0 */
{
    "_id" : ObjectId("52a7538bc0757ccee4628aa4"),
    "name" : "admin",
    "exam" : "exam1",
    "point" : 80,
    "deadline" : ISODate("2013-12-09T00:00:00.000Z")
}

/* 1 */
{
    "_id" : ObjectId("52a75e0cc0757ccee4628aa5"),
    "name" : "admin",
    "exam" : "exam2",
    "point" : 50,
    "deadline" : ISODate("2013-12-08T00:00:00.000Z")
}

/* 2 */
{
    "_id" : ObjectId("52a895607b01cd1200940ee1"),
    "point" : 0,
    "deadline" : ISODate("2013-12-12T00:10:00.424Z"),
    "name" : "hieu",
    "exam" : "exam1"
}

questions
/* 0 */
{
    "_id" : ObjectId("52a6dd290312daa75dc156bc"),
    "question" : "M?t ng�y c� m?y gi??",
    "answers" : {
        "24" : true,
        "32" : false,
        "12" : false
    },
    "exams" : [ 
        "K� thi s? 1", 
        "K� thi s? 2"
    ]
}

/* 1 */
{
    "_id" : ObjectId("52a701b70312daa75dc156bf"),
    "question" : "? M?, Thanksgiving Day v�o ng�y bao nhi�u?",
    "answer" : {
        "Ng�y th? 5 h�ng th�ng" : false,
        "Ng�y th? 5 cu?i c�ng c?a th�ng 10" : false,
        "Ng�y th? 5 c?a tu?n th? 4 c?a th�ng 11" : true
    },
    "exams" : [ 
        "K� thi s? 1", 
        "K� thi s? 2"
    ]
}

/* 2 */
{
    "_id" : ObjectId("52a6dc130312daa75dc156bb"),
    "question" : "Trang Web n�y du?c vi?t b?ng Ng�n ng? l?p tr�nh n�o?",
    "answer" : {
        "Python" : true,
        "PHP" : false,
        "C++" : false
    },
    "exams" : [ 
        "K� thi s? 1", 
        "K� thi s? 2"
    ]
}

users
/* 0 */
{
    "_id" : ObjectId("52a608467b01cd0fb45e950f"),
    "username" : "admin",
    "password" : "admin",
    "fullname" : "Nguy?n ?t Min",
    "banned" : false
}

/* 1 */
{
    "_id" : ObjectId("52a6b9296927d9145f7f15e4"),
    "username" : "hieu",
    "password" : "hieu",
    "fullname" : "Ki?u Trung Hi?u",
    "banned" : false
}