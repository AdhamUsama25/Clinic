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


class Doctor:
    def __init__(self, patients):
        self.treating_rate = patients
        self.current_patient = None
        self.time_remaining = 0

    def tick(self):
        if self.current_patient is not None:
            self.time_remaining -= 1
            if self.time_remaining == 0:
                self.current_patient = None

    def busy(self):
        return self.current_patient is not None

    def enter_next(self, new_patient):
        self.current_patient = new_patient
        self.time_remaining = new_patient.get_age()/self.treating_rate


class Patient:
    def __init__(self, time):
        self.timestamp = time
        self.age = random.randrange(20, 61)

    def get_age(self):
        return self.age

    def waiting_time(self, current_time):
        return current_time - self.timestamp

# Project:


def simulation(treating_rate):
    doctor_x = Doctor(treating_rate)
    patients_queue = Queue()
    waiting_times = []

    for current_second in range(4 * 3600):
        if random.randrange(1, 361) == 360:
            patient = Patient(current_second)
            patients_queue.enqueue(patient)

        if (not doctor_x.busy()) and (not patients_queue.is_empty()):
            next_patient = patients_queue.dequeue()
            waiting_times.append(next_patient.waiting_time(current_second))
            doctor_x.enter_next(next_patient)

        doctor_x.tick()

    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average Wait", str("{:.2f}".format(average_wait)), "secs", patients_queue.size(), "patients remaining")


for i in range(10):
    simulation(10)
