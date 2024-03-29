# Dictionary Oriented Programming
### It is a slightly different way of thinking about apps that is non object oriented.

It seems to me that many apps are really building a record one step at the time, say like a business order. In Python a record can well be represented by a dictionary, like this customer:  

`{'id'; 13579 , 'fname': 'Kristoffer' , 'lname': 'Legind', 'address': "you'd like to know huh"}`

So far nothing special (you might say we could do this with a class), but think about what you can add to this record dictionary like *checks*! Perhaps the project has some rules, like a record can expand along the way but never contract.  
This can be implemented as an element is the dict - 'previouslength' = len(dict.values()) at the previous step. 'currentlength': len(dict.values())  
The rule can be written as if dict['previouslength'] > dict['currentlength']: raise Error ...

You could also add a log for each step of the record creation process. The log is INSIDE the record:  
`{'id'; 13579, 'fname': 'Kristoffer', ..., 'log':`  
                                              {'getcustomerid_step': ...,                                                
                                              'getshoppingbasketcontent_step': ...',  
                                              ...
                                              }                                               
                                              }
                                              
So instead of being stuck in a soup of OO object instance references, an alternative could be using a tool like "Shared" ( https://pypi.org/project/shared/ ) - this allows us to reference an object, let's say a JSON doc, from anywhere in the code base. Like so:  

`sharedDocument = JsonDoc("some_name-data.json", directory=os.getcwd())`

This enables us to add items to the record from different classes or modules without having to pass class instance references around. Imagine your app has a GUI and every box in the gui talks to a function somewhere else - after that function has processed a particular step, that step's data product is added to the sharedDocument record using the doc handle. I think that in many cases this is more convenient than having a record class and passing this around for each step.


