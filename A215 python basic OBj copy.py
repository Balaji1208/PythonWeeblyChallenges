# Object oriented - basics "weebly challenges"
# graph class
'''
class Point:
  """The pointer class manupilate the x,y co-oridanates"""
  def __init__(self,x=0,y=0):
    """Create a new point at the origin"""
    self.x = x
    self.y = y

  def distance_from_origin(self):
        """ Computes distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

  def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

  def midpoint(self, target):
    """ Return the midpoint of points p1 and p2 """
    mx = (self.x + target.x)/2
    my = (self.y + target.y)/2
    return Point(mx, my)

  def reflectx(self):
    """Reflects the point on the x axis"""
    x = (self.x)
    y = (self.y * -1)
    return Point(x,y)

  def slope_from_origin(self):
    """Returns the slope of the line joining the origin to the point"""
    return (self.y / self.x)

  def get_line_to(self,target):
    """Computes the equation of the straight line joining the two points"""
    gradient = (self.y - target.y )/(self.x - target.x)
    yintercept = self.y - (gradient*self.x)
    print (gradient,"x +",yintercept)
  

x = Point(7,13)
print('Distance from origin:')
print(x.distance_from_origin())
print('Point:')
print(str(x))
print('Slope:')
print(x.slope_from_origin())
print('Equation of line from 2 points:')
x.get_line_to(Point(5,4))

y = Point(2,4)
print('Distance from origin:')
print(y.distance_from_origin())
print('Point:')
print(str(y))
print('Slope:')
print(y.slope_from_origin())
print('Equation of line from 2 points:')
y.get_line_to(x)

r = x.midpoint(y)
print('Midpoint:')
print(r)

f = r.reflectx()
print('Reflected on x-axis:')
print(f) 
'''

# SMS class

'''
class SMS_store:
  """The SMS class to manupilate messages"""
  def __init__(self):
    """Create a new SMS"""
    self.has_been_viewed = input("message view time")
    self.from_number = input("who message is from")
    self.time_arrived = input("what time you recieved the message")
    self.text_of_SMS = input("what was written in the message")
    print(self.has_been_viewed,self.from_number,self.time_arrived,self.text_of_SMS)

  def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
      self.append((False, from_number, time_arrived, text_of_SMS))    

  def message_count(self):
      return len(self)

class my_inbox:
  """Manupilate your SMS inbox"""
  def work(self):
    """Create an empty inbox"""
    self = ['',]
  def add_new_arrival(self):
    """Add a new SMS"""
    self.work()
    self.append([SMS_store()])


inboc = my_inbox()
inboc.add_new_arrival()
print(my_inbox)

'''



class SMS_store(object):
  """The SMS class to manupilate messages"""
  def __init__(self):
    """Initiating the inbox list"""
    self.messages = []
  def add_new_arrival(self,status,from_number, time_arrived, text_of_SMS):
    self.messages.append((status,from_number,time_arrived,text_of_SMS))

  def message_count(self):
    return len(self.messages)

  def get_message(self,place):
    return self.messages[place]

  def get_unread_indexes(self):
    for i in range (len(self.messages)):
      x = self.messages[i]
      if False in self.messages[i]:
        print(i)

my_inbox = SMS_store()
my_inbox.add_new_arrival(False,'012-6152539','9:37 AM','How are you?')
my_inbox.add_new_arrival(True, '012-4359994','11:24 PM','Does this actually work?')
my_inbox.add_new_arrival(False, '012-4359994','13:19 PM','I believe this is actually working')
my_inbox.add_new_arrival(False, '012-4359994','16:25 PM','OMG it is working ')

print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(1))
print(my_inbox.get_message(2))







    
