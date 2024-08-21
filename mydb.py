from country import Country
from user import User
from job import Job
from song import Song


class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.User=User()
    self.Song=Song()
    self.Job=Job()
