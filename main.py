class user:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email

    def __repr__(self):
        return "user(username='{}',name='{}',email='{}')".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()

class UserDatabase:
    def __init__(self):
        self.user=[]
    def insert(self,user):
        i=0
        while i<len(self.user):
            if self.user[i].username>user.username:
                break
            else: i+=1
        self.user.insert(i,user)
    def find(self,find):
        for user in self.user:
            #print(self.user)
            #print(user.username)
            #print(find)
            #print(user)
            #print(find.username)
            #print(user.username)
            if user==find:
                return user

    def list_all(self):
        return self.user

ekjyot=user('ej','ekjyot','eshinh@abc.com')
jimmy=user('jim','jimmy','jimmy@abc.com')
qwerty=user('qrt','qwerty','qwerty@abc.com')
romin=user('ronin','romin','romin@abc.com')
gaurvi=user('gaurvi','guv','gaurvi@abc.com')


database=UserDatabase()
database.insert(qwerty)
database.insert(ekjyot)
database.insert(jimmy)
database.insert(romin)
database.insert(gaurvi)

#database.list_all()
print(database.list_all())
print(database.find(gaurvi))