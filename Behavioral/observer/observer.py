class User:
    def __init__(self,name):
        self.name = name
    
    def update(self,blog):
        print(f"dear {self.name } please check new article written by {blog.name}")

class BlogWriter:
    def __init__(self,name):
        self.name = name
        self.__subscriber = []
        self.__article = []
    
    def add_article(self,article):
        self.__article.append(article)
        self.notify()
    
    def subscribe(self,sub):
        self.__subscriber.append(sub)
    
    def unSubscribe(self,sub):
        self.__subscriber.remove(sub)

    def notify(self):
        for i in self.__subscriber:
            i.update(self);


blog  = BlogWriter("rahul")
user1 = User("vidhi")
user2 = User("Amit")
blog.subscribe(user1)
# blog.subscribe(user2)

blog.add_article("I am rahul")

