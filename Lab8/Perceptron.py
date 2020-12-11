import numpy as np


class Perceptron:

    def __init__(self, number_of_cols):
        self.weights = np.random.rand(number_of_cols, 1)
        self.threshold = 0

    def predict_value(self, row):
        predicted_value = np.matmul(self.weights.T, row) + self.threshold   # jeśli + to raczej bias

        if predicted_value > 0:
            return 1
        else:
            return 0

    def train_perceptron(self, data,  max_iter=100, learning_rate=0.1):
        for i in range(max_iter):
            error_counter = 0

            for description_data, label in zip(data.description_row, data.label):
                predicted_label = self.predict_value(description_data)
                real_label = label

                if predicted_label != real_label:
                    add_to_weights = (description_data * (label - predicted_label) * learning_rate)
                    add_to_weights = add_to_weights.reshape(add_to_weights.shape[0], 1)
                    self.weights = np.add(self.weights, add_to_weights)
                    self.threshold = (label - predicted_label) * learning_rate
                    error_counter = error_counter + 1

            error_rate = error_counter/data.description_row.shape[0]
            print("Iteration: {} Error rate: {} Precision: {}".format(i, error_rate, 1 - error_rate))
            print()

    def test_perceptron(self, data):
        n = data.description_row.shape[0]
        error_counter = 0
        for description_data, label in zip(data.description_row, data.label):
            predicted_label = self.predict_value(description_data)
            error_counter += abs(label - predicted_label)

        error_rate = error_counter / n
        print("Error rate: {} Precision: {}".format(error_rate, 1-error_rate))
