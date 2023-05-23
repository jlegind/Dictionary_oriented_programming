#Dictionary Oriented Programming
### It is a slightly different way of thinking about apps

It seems to me that many apps are really building a record one step at the time, say like a business order. In Python a record can well be represented by a dictionary.  

`{'id'; 13579 , 'fname': 'Kristoffer' , 'lname': 'Legind', 'address': "you'd like to know huh"}`

So far nothing special, but think about what you can add to this record dictionary like *checks*! Perhaps the project has some rules, like a record can expand along the way but never contract.  
This can be implemented as an element is the dict - 'previouslength' = len(dict.values()) at the previous step. 'currentlength': len(dict.values())  
The rule can be written as if dict['previouslength'] > dict['currentlength']: raise Error ...


