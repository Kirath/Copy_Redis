# Copy_Redis
Mini Project given Unacadmey
# Redis-Clone
This is a prototype for Redis with some basic functionalities. Itan be used like any REST API. 
### Table of Contents
---
 <details>

   ##### Redis-Clone
   1. Usage
   2. Abstract
   3. Functions Implemented
      * GET()
      * SET()
      * EXPIRE()
      * ZADD()
      * ZRANGE()
      * ZRANK()
   4. Questions
 </details>
 
### Usage
---
 To run this app the dependencies mentioned in the dependencies.txt must be satisfed. 
Once the dependency has been satisfied app.py can directly be executed python interpreter. 

    python3 app.py
The server will then be live on [http://localhost:5000/](http://localhost:5000/)

### **Abstract**
---This is a  project a clone of Redis commands. Redis ( Remote Dictionary Server)  is an in-memory data structure project implementing a distributed, in- memory key-value database  with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indexes. The project is mainly developed by Salvatore Sanfilippo and as of 2019, is sponsored by Redis Lab. It is open-source software released under a BSD 3-clause license.



### **Function Implemented**
---
### 1. GET()

##### How to use?

`/api/v1/books?id=x`

##### Time Complexity: O(1)

This function simply checks if the string value exist for the given key. If the key is not present "nil".

---
### 2. SET()

##### How to use?

`/api/v1/books/set`

##### Time Complexity: O(1)

This function is used to insert value with given key. If key is already holding a value it is overriden. It can operate in all different modes like a redis SET. 

---
### 3. EXPIRE()

##### How to use?

`/api/v1/books/time`

##### Time Complexity: O(1)

This can be used to add timeout on any key irrespective of the value it is holding. This particular key and score are deleted from the main database once the GET is called for this key.

### 4. ZADD()

##### How to use?

`/api/v1/books/update?id_1=x&val_1='hi'&id_2=3&val_2='three'&mode=[NX|XX] [CH] [INCR] score member [score member ...]`

##### Time Complexity: O(log(N)) (N represents number of items present in our Sorted Set)

Adds all the specified members with the specified scores to the sorted set stored at key. It is possible to specify multiple score / member pairs. If a specified member is already a member of the sorted set, the score is updated and the element reinserted at the right position to ensure the correct ordering.

If key does not exist, a new sorted set with the specified members as sole members is created. If the key exists but does not hold a sorted set, an error is returned. 

---
### 5. ZRANGE()

##### How to use?

`/api/v1/books/add/find?praram1=x&param2=y`

##### Time Complexity: O(log(N)+C)
		 N being the number of elements in the sorted set and C the number of elements returned.

Returns the specified range of elements in the sorted set stored at key. The elements are considered to be ordered from the lowest to the highest score. Lexicographical order is used for elements with equal score.

---
### 6. ZRANK()

##### How to use?

`/api/v1/books/search?val=q`

##### Time Complexity: O(log(N))

Returns the rank of member in the sorted set stored at key, with the scores ordered from low to high. The rank (or index) is 0-based, which means that the member with the lowest score has rank 0.


## Questions

#### 1. Why python language has been used?
Ans: This project was implemented using python and its libraries. The reason behind  using python language was the vast library support and also my comfortability to work with python. The libraries used are flask, datetime, sorted container, deque.

#### 2. What are the further improvements that can be made?
Ans: Various improvements can be done in this prototype. Some improvements that was planned by me but was not implemented due to lack of time are as follow:-
- Log: Creating the logs of the file so that if program ends we can get the edits made post the end of session.
- Threading: Writing in file can be done parallely with main thread 

#### 3. What Data Structures have been used and Why?
Ans: Various data structures have been used in this prototype. They are as follows:-
- Red Black Tree: For implementing Sorted Set Data Strucutre. It is used as a Balanced BST
- Tuples: For storing (score, value) pair whoch acts as node for RB Tree
- Arrays: Temporary intermediate Calculation and Input
- Deque = For storing the sequence of items according to their TTL.

#### 4. Does your implementation support multi threaded operations?
Ans: Currently it does not support Multi threading due to lack of time. But the prototype can be multi threaded ny creating log files where more than one thread can write. Since this operation is an I/O operation and is also independent of other parts of the program it can be multi threaded.
