import csv
import numpy as np


class CsvFileStorage:

    def __init__(self, description_row=None, label=None):
        self.description_row = description_row
        self.label = label

    def read_csv_file(self, path, delimiter=';', label_col=-1):
        with open(path, 'r') as file:
            data = csv.reader(file, delimiter=delimiter)
            data = [d for d in data]

        data = np.asarray(data, float)
        if isinstance(label_col, (int, float)):
            self.label = np.asarray(data[:, label_col])
            self.description_row = np.delete(data, label_col, 1)
        else:
            self.description_row = data

    def mean_center_column(self, col):
        self.description_row[:, col] = self.description_row[:, col] - self.description_row[:, col].mean()

    def normalize_column(self, col):
        self.description_row[:, col] = (self.description_row[:, col] - self.description_row[:, col].min())/\
                                       (self.description_row[:, col].max() - self.description_row[:, col].min())

    def normalize_all_rows(self):
        for i in range(self.description_row.shape[0]):
            self.description_row[i, :] = (self.description_row[i, :] - self.description_row[i, :].min())/\
                                         (self.description_row[i, :].max() - self.description_row[i, :].min())

    def split_data_to_train_and_test(self, training_size=0.75):
        train_data = self.description_row[0: round(training_size * np.shape(self.description_row)[0]), :]
        train_label = self.label[0: round(training_size * np.shape(self.description_row)[0])]

        test_data = self.description_row[round(training_size * np.shape(self.description_row)[0]): np.shape(self.description_row)[0], :]
        test_label = self.label[round(training_size * np.shape(self.description_row)[0]): np.shape(self.description_row)[0]]

        return CsvFileStorage(train_data, train_label), CsvFileStorage(test_data, test_label)