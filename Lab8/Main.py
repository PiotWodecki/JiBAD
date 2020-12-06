from CsvFileHandler import CsvFileStorage
from Perceptron import Perceptron


def main():
    # data_sample_1 = CsvFileStorage()
    # data_sample_1.read_csv_file('sample1.csv')
    # perceptron_sample_1 = Perceptron(data_sample_1.description_row.shape[1])
    # perceptron_sample_1.train_perceptron(data_sample_1)
    # perceptron_sample_1.test_perceptron(data_sample_1)
    #
    # data_sample_2 = CsvFileStorage()
    # data_sample_2.read_csv_file('sample2.csv')
    # perceptron_sample_2 = Perceptron(data_sample_2.description_row.shape[1])
    # perceptron_sample_2.train_perceptron(data_sample_2)
    # perceptron_sample_2.test_perceptron(data_sample_2)

    data_sample_3 = CsvFileStorage()
    data_sample_3.read_csv_file('sample3.csv')
    train_sample, test_sample= data_sample_3.split_data_to_train_and_test()
    perceptron_sample_3 = Perceptron(data_sample_3.description_row.shape[1])
    perceptron_sample_3.train_perceptron(train_sample)
    perceptron_sample_3.test_perceptron(test_sample)
    perceptron_sample_3.train_perceptron(data_sample_3)


if __name__ == "__main__":
    main()