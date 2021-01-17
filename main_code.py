import tkinter
import cv2
import PIL.Image 
import PIL.ImageTk
import threading
import imutils
import time
from functools import partial

stream = cv2.VideoCapture("video.mp4")

def play(speed):
    print(f"Your speed is {speed}")

    # Now will run the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH , height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

def pending(decision):
    # 1)Display the decision pending screen
    frame = cv2.cvtColor(cv2.imread("decision.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2)Wait for 1 sec
    time.sleep(1)
    # 3)Display the sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 4)Wait for 1.5 sec
    time.sleep(1.5)
    # 5)Display the final decision
    if decision == 'goal':
        decisionImg = "goal.png"
    elif decision == 'no_goal':
        decisionImg = "no_goal.png"
    elif decision == 'penalty':
        decisionImg = "penalty.png"
    elif decision == 'no_penalty':
        decisionImg = "no_penalty.png"
    elif decision == 'offside':
        decisionImg = "offside.png"
    else:
        decisionImg = "not_offside"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
def goal():
    thread = threading.Thread(target=pending, args=("goal",))    
    thread.daemon = 1
    thread.start()
    print("This is a goal")
def no_goal():
    thread = threading.Thread(target=pending, args=("no goal",))    
    thread.daemon = 1
    thread.start()
    print("no goal")
def penalty():
    thread = threading.Thread(target=pending, args=("penalty",))    
    thread.daemon = 1
    thread.start()
    print("This is a penalty")
def no_penalty():
    thread = threading.Thread(target=pending, args=("no penalty",))    
    thread.daemon = 1
    thread.start()
    print("This is not a penalty")
def offside():
    thread = threading.Thread(target=pending, args=("offside",))    
    thread.daemon = 1
    thread.start()
    print("This is offside")
def not_offside():
    thread = threading.Thread(target=pending, args=("not offside",))    
    thread.daemon = 1
    thread.start()
    print("Not offside")

SET_WIDTH = 607
SET_HEIGHT = 402

window = tkinter.Tk()
window.title("Video Assistance Referee")
cv_img = cv2.cvtColor(cv2.imread("var.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor=tkinter.NW, image=photo)
canvas.pack()
btn = tkinter.Button(window, text="<< Previous(FAST)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous(SLOW)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next(SLOW) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next(FAST) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="GIVE (GOAL)", width=50, command=goal)
btn.pack()

btn = tkinter.Button(window, text="GIVE (NO GOAL)", width=50, command=no_goal)
btn.pack()

btn = tkinter.Button(window, text="GIVE (PENALTY)", width=50, command=penalty)
btn.pack()

btn = tkinter.Button(window, text="GIVE (NO PENALTY)", width=50, command=no_penalty)
btn.pack()

btn = tkinter.Button(window, text="GIVE (OFFSIDE)", width=50, command=offside)
btn.pack()

btn = tkinter.Button(window, text="GIVE (NOT OFFSIDE)", width=50, command=not_offside)
btn.pack()
window.mainloop()