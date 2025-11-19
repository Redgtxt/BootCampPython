#creating a class
class User:
    
    #Inicializing the attributes using the init function aka Constructor
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        #Passing a default value
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1
        
#Creating a instance of my class
user1 = User("001","Jackie chan")
user2 = User("002","Bruce Lee")

#You can add variables to an instance  if you put a dot(.)
#user1.age = 23

user1.follow(user2)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)