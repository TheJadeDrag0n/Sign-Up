#---------------------------------------------------
#| Ver 1.1 - added test ticket data                |
#| Ver 1.2 - adding server functionality to pyhton |
#|                                                 |
#| Ver 1.5 - add second page.                      |
#---------------------------------------------------


from bottle import run, route, view, get, post, request
from itertools import count



class Ticket:
    
    
    _ids = count(0)
    
    def __init__(self, name, email, date_of_birth,check_in):
        
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in




#test data
tickets = [
    Ticket("James Cameron", "jamescameron@my.rnls.school.nz", "21/09/01", False),
    Ticket("Dan", "dan123@outlook.com", "13/06/87", False),
    Ticket("Hannah Wilson", "hannah123@gmail.com", "n/a", False),
    Ticket("Cynthia", "randomperson@gmail.com", "n/a", False)
    ]





#Pages

#index
@route("/")
@view("index")
def index():
    
    pass

#check in
@route("/check-in")
@view("check-in")
def check_in():
    data = dict (ticket_list=tickets)
    return data





run(host='0.0.0.0',port = 8080, reloader=True, debug=True)
