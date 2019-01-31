# saman_rasool_test
There are 2 directories in the project,
src: Contains source code for all three questions
  QuestionA.py
  QuestionB.py
  QuestionC.py
  
test: Contains unit test cases for QuestionA and QuestionB. You can run the test file. 




Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
Answer: To test this method call the method:
 
 Example:  print(isOverlap([2,3],[3,5]))


Question B
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
Answer: To test this method, call the method:
 
 Example:  print(compareVersion('1.2.3','1.2.7'))

Question C
At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

    1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema
    7 - Cache can expire 
    
  Solution: I was only able to implement a basic LRU Cache mechanism with get and set functions. 
  I was not able to implement point 2,5
