import csv
import os


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(os.path.abspath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_class(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects