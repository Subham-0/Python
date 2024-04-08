import turtle as t 
tut = t.Turtle()

colors = ["gray0","gray10","gray20","gray30","gray40","gray50","gray60","gray70","gray80","gray90"]

for i in range(3,11):
    tut.pencolor(colors[i-3])     
    for j in range(0,i):   
        tut.forward(60)
        tut.right(360/i)
    
sc = t.Screen()
sc.exitonclick()
