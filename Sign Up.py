#---------------------------------------------------
#| Ver 1.1 - added test ticket data                |
#| Ver 1.2 - adding server functionality to pyhton |
#---------------------------------------------------


from bottle import run, route, view, get, post, request
from itertools import count



class Ticket:
    
    
    _ids = count(0)
    
    def __int__(self, name, email, date_of_birth,check_in):
        
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in




#test data
tickets = [
    Tickets("James Cameron", "jamescameron@my.rnls.school.nz", "21/09/01", False),
    Tickets("Dan", "dan123@outlook.com", "13/06/87", False),
    Tickets("Hannah Wilson", "hannah123@gmail.com", "n/a", False),
    Tickets("Cynthia", "randomperson@gmail.com", "n/a", False)
    ]





#Pages

#index
@route("/")
@view("index")
def index():
    
    pass




run(host='0.0.0.0',port = 8080, reloader=True, debug=True)
