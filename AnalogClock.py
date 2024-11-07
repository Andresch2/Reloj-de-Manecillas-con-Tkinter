from tkinter import Canvas, Tk, Frame, LAST
from time import strftime, localtime
from math import sin, cos, radians, pi

class Clock:
    def __init__(self, time_unit):
        self.time_unit = time_unit
        self.next = None

class ClockList:
    def __init__(self):
        self.start_clock = None

    def add_at_end(self, time_unit):
        new_time = Clock(time_unit)
        if self.start_clock is None:
            self.start_clock = new_time
            new_time.next = self.start_clock
        else:
            current = self.start_clock
            while current.next != self.start_clock:
                current = current.next
            current.next = new_time
            new_time.next = self.start_clock

clock_list = ClockList()
clock_list.add_at_end("12:00:00")
clock_list.add_at_end("3:00:00")
clock_list.add_at_end("6:00:00")
clock_list.add_at_end("9:00:00")
clock_list.add_at_end("12:00:00")

window = Tk()
window.title('Analog Clock')
window.geometry('420x420')
window.config(bg='white')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame = Frame(window, height=400, width=400, bg='white', relief='sunken')
frame.grid(column=0, row=0)
canvas = Canvas(frame, bg='white', width=385, height=385, relief='raised', bd=10)
canvas.grid(padx=5, pady=5)

hour_angle = 0
minute_angle = 0
second_angle = 0

def draw_clock(hour_angle, minute_angle, second_angle):
    canvas.create_oval(50, 50, 350, 350, fill='white', outline='black', width=6)
    numbers = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]
    for i in range(len(numbers)):
        canvas.create_text(200 - 120 * sin(((i + 1) * 2 * pi) / 12), 200 - 120 * cos(((i + 1) * 2 * pi) / 12), text=numbers[i], font=('Arial', 12, 'bold'), fill='black')
    for y in range(60):
        canvas.create_text(200 - 140 * sin(((y + 1) * 2 * pi) / 60), 200 - 140 * cos(((y + 1) * 2 * pi) / 60), text='•', font=('Arial', 12, 'bold'), fill='red')
    for x in range(12):
        canvas.create_text(200 - 140 * sin(((x + 1) * 2 * pi) / 12), 200 - 140 * cos(((x + 1) * 2 * pi) / 12),text='•', font=('Arial', 25, 'bold'), fill='blue')

    canvas.create_line(200, 200, 200 + 60 * sin(radians(hour_angle)), 200 - 60 * cos(radians(hour_angle)), fill='black', width=9, arrow=LAST)
    canvas.create_line(200, 200, 200 + 80 * sin(radians(minute_angle)), 200 - 80 * cos(radians(minute_angle)), fill='black', width=6, arrow=LAST)
    canvas.create_line(200, 200, 200 + 120 * sin(radians(second_angle)), 200 - 120 * cos(radians(second_angle)), fill='red', width=3, arrow=LAST)
    canvas.create_oval(190, 190, 210, 210, fill='white', outline='black', width=2)

def update_time():
    global hour_angle, minute_angle, second_angle
    current_time_str = strftime('%H:%M:%S', localtime())
    hour_angle = (int(current_time_str.split(':')[0]) / 12) * 360
    minute_angle = (int(current_time_str.split(':')[1]) / 60) * 360
    second_angle = (int(current_time_str.split(':')[2]) / 60) * 360
    draw_clock(hour_angle, minute_angle, second_angle)
    canvas.after(1000, update_time)

update_time()
window.mainloop()
