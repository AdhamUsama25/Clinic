# Imports:
import random

# Classes:


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Patient:
    def __init__(self, time):
        self.timestamp = time
        self.age = random.randrange(20, 61)

    def get_age(self):
        return self.age

    def waiting_time(self, current_time):
        return current_time - self.timestamp


class Doctor:
    def __init__(self, patients):
        self.treating_rate = patients
        self.current_patient = None
        self.time_remaining = 0

    def tick(self):
        if self.current_patient is not None:
            self.time_remaining -= 1
            if round(self.time_remaining) == 0:
                self.current_patient = None

    def busy(self):
        return self.current_patient is not None

    def enter_next(self, new_patient):
        self.current_patient = new_patient
        self.time_remaining = round(new_patient.get_age()/self.treating_rate) * 60


def time_format(a_time):
    h = a_time // 3600
    m = (a_time - h * 3600) // 60
    s = a_time - h * 3600 - m * 60
    if a_time >= 3600:
        return f'{int(h)} hrs, {int(m)} mins, {str("{:.2f}".format(s))} secs'
    elif a_time >= 60:
        return f'{int(m)} mins, {str("{:.2f}".format(s))} secs'
    else:
        return f'{str("{:.2f}".format(s))} secs'

# Project:


def simulation(num_of_hours, treating_factor):
    doctor_x = Doctor(treating_factor)
    patients_queue = Queue()
    waiting_times = []

    for current_second in range(num_of_hours * 3600):
        if random.randrange(1, 361) == 360:     # The rate of the clinic is 10 patients per hour. 10/3600 = 360
            patient = Patient(current_second)
            patients_queue.enqueue(patient)

        if (not doctor_x.busy()) and (not patients_queue.is_empty()):
            next_patient = patients_queue.dequeue()
            waiting_times.append(next_patient.waiting_time(current_second))
            doctor_x.enter_next(next_patient)

        doctor_x.tick()

    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average Wait", time_format(average_wait), "and", patients_queue.size(), "patients remaining")


for i in range(10):
    simulation(4, 10)
