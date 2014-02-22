exams
/* 0 */
{
    "_id" : ObjectId("52a6f2280312daa75dc156be"),
    "link" : "exam1",
    "name" : "Kì thi s? 1",
    "content" : "Chua có",
    "question" : 2,
    "duration" : 30,
    "deadline" : ISODate("2013-12-24T00:00:00.000Z"),
    "status" : true
}

/* 1 */
{
    "_id" : ObjectId("52a743acc0757ccee4628aa3"),
    "link" : "exam2",
    "name" : "Kì thi s? 2",
    "content" : "Chua có",
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
    "question" : "M?t ngày có m?y gi??",
    "answers" : {
        "24" : true,
        "32" : false,
        "12" : false
    },
    "exams" : [ 
        "Kì thi s? 1", 
        "Kì thi s? 2"
    ]
}

/* 1 */
{
    "_id" : ObjectId("52a701b70312daa75dc156bf"),
    "question" : "? M?, Thanksgiving Day vào ngày bao nhiêu?",
    "answer" : {
        "Ngày th? 5 hàng tháng" : false,
        "Ngày th? 5 cu?i cùng c?a tháng 10" : false,
        "Ngày th? 5 c?a tu?n th? 4 c?a tháng 11" : true
    },
    "exams" : [ 
        "Kì thi s? 1", 
        "Kì thi s? 2"
    ]
}

/* 2 */
{
    "_id" : ObjectId("52a6dc130312daa75dc156bb"),
    "question" : "Trang Web này du?c vi?t b?ng Ngôn ng? l?p trình nào?",
    "answer" : {
        "Python" : true,
        "PHP" : false,
        "C++" : false
    },
    "exams" : [ 
        "Kì thi s? 1", 
        "Kì thi s? 2"
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