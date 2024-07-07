import turtle
import pandas




screen = turtle.Screen()
screen.title("egypt game")
image ="data\eg-02 .gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse(x,y):
#     print(x,",",y)
#
# turtle.onscreenclick(get_mouse)
# turtle.mainloop()

data = pandas.read_csv("data\governorates_coordinates_negative.csv")
all_Governorate= data.Governorate.to_list()

guss_state=[]

while len(guss_state) <27:
    answer= screen.textinput(title=f"{len(guss_state)} /27 correct", prompt="do u know any more ?").title()
    # print(answer)

    if answer =="Exit":
        break
    if answer in all_Governorate :
         guss_state.append(answer)
         t= turtle.Turtle()
         t.hideturtle()
         t.pu()
         gov_data=data[data.Governorate == answer]
         t.goto(int(gov_data.X),int(gov_data.Y))
         t.write(answer)

Governorate_to_learn = data[~data.Governorate.isin(guss_state)].Governorate.to_list()

gt = pandas.DataFrame(Governorate_to_learn)
gt.to_csv("Governorate_to_learn.csv")

screen.exitonclick()