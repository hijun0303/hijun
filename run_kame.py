import dice
a = dice.Dice(6)
b = dice.Dice(6)
import kame
k1 = kame.Kame("red","blue")
k2 = kame.Kame("purple","pink")
k1.penup()
k2.penup()
k1.goto(-300,200)
k2.goto(-300,-200)
c = a.shoot()
d = b.shoot()
k1.fd(c*50)
k2.fd(d*50)
if c > d:
     k1.home()
     k1.pendown
     k1.write("WIN",move=True,font=("Verdana",50,"normal"))
else:
     k2.home()
     k2.pendown
     k2.write("WIN",move=True,font=("Verdana",50,"normal"))
kame.turtle.done()
