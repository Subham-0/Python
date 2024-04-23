import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")

state_image = "blank_states_img.gif"
screen.addshape(state_image)

turtle.shape(state_image)



data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_state  = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name ?").title()
    
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state] #list comprehension
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
         # t.write(state_data.state.item)


#get perticular cooridinates
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()