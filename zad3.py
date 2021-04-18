import random
import csv
import os

# w przykładzie były inty, więc założyłam, że wartości od 0-1000 mają być intami


def partA():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:

        try:
            os.makedirs(f"{os.getcwd()}/{day}/morning")
            os.makedirs(f"{os.getcwd()}/{day}/evening")
        except OSError:
            print(f"Creating morning/evening folders for {day} failed :(")

        with open(f"{day}/morning/Solutions.csv", mode='w') as m:
            m_writer = csv.writer(m, delimiter = ';', quotechar = '"',  quoting = csv.QUOTE_MINIMAL)
            m_writer.writerow(['Model',
                               'Output value',
                               'Time of computation'])
            m_writer.writerow([random.choice(['A', 'B', 'C']),
                               random.randint(0, 1000),
                               f"{random.randint(0,1000)}s"])

        with open(f"{day}/evening/Solutions.csv", mode='w') as m:
            m_writer = csv.writer(m, delimiter = ";", quotechar = '"',  quoting = csv.QUOTE_MINIMAL)
            m_writer.writerow(['Model',
                               'Output value',
                               'Time of computation'])
            m_writer.writerow([random.choice(['A', 'B', 'C']),
                               random.randint(0, 1000),
                               f"{random.randint(0,1000)}s"])


def partB():
    sumtoc = 0
    def check_dirs(path, sumtoc=sumtoc):
        if 'Solutions.csv' in os.listdir(path):
            with open(f"{path}/Solutions.csv") as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=";")
                for row in csv_reader:
                    if row['Model'] == 'A':
                        sumtoc += int(row['Time of computation'][:-1])
        for dir in os.listdir(path):
            if os.path.isdir(path + '/' + dir):
                sumtoc += check_dirs(path + '/' + dir)
        return sumtoc
    sumtoc += check_dirs(os.getcwd())
    print(f"Sum of time of computation for model A is: {sumtoc}")




partA()
partB()