

posts = [
  {
  "title": "About the importance of functional programming",
  "body": "Functional programming is ....." 
  },
  {
  "title": "OOP programming brings classes and objects into the code",
  "body": "OOP is  ....." 
  },
]

def addPost(posts,title,body):
    post = {"title":title["title"],"body":body["body"]}
    posts.insert(0,post)



d = {"title":"Harap-Alb"}
c = {"body":"reprezinta lupta binelui împotriva răului..."}


addPost(posts,d,c)

print (posts)
    



#    What is required:
#
# 1. create a function called "addPost()", which will take exactly 3 parameters: the list in which
#    the post is to be added, the post title and the post body
# 2. the function will form a new dictionary formed of the last 2 parameters and add it into the first
#    place inside the first parameter
# 3. the function will NOT return anything