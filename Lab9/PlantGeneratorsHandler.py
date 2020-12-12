import pandas as pd
import matplotlib.pyplot as plt


def merge_data_frames(*dataframes):
    dfs = list(dataframes)
    df = pd.concat(dfs)
    return df


def draw_plot_for_generator(df, generator_key, start_date, end_date):
    plot_df = df.copy()
    plot_df = plot_df.loc[df['SOURCE_KEY'] == generator_key]
    plot_df = plot_df.set_index(['DATE_TIME'])

    plot_df = plot_df.loc[start_date:end_date]
    plot_df = plot_df.reset_index()
    plt.plot(plot_df['DATE_TIME'], plot_df['AC_POWER'], color='blue', label="Generator: {}".format(generator_key))
    plt.xlabel('Date Time')
    plt.ylabel('AC POWER')

    def draw_average_power_for_generator_on_existing_plot(dataframe):
        plot2_df = dataframe.copy()
        plot2_df = plot2_df.set_index(['DATE_TIME'])
        plot2_df = plot2_df.loc[start_date:end_date]
        means = plot2_df.groupby('DATE_TIME').mean()

        return means

    means_for_each_generator = draw_average_power_for_generator_on_existing_plot(df)
    plt.plot(means_for_each_generator['AC_POWER'], color='red', label="Mean for all generator")
    plt.legend()
    plt.show()


def calculate_mean_for_generator_power_for_each_date(dataframe):
    df = dataframe.copy()
    df['Means'] = df.groupby('DATE_TIME')['AC_POWER'].transform('mean')
    return df


def check_if_power_was_under_the_mean(dataframe, difference=0.8):
    df = dataframe.copy()
    df['Is under mean'] = df['AC_POWER'].lt(df['Means'] * difference)
    return df


def check_generator_with_the_most_occurence_under_the_average_power(dataframe, col_name='Is under mean'):
    df_with_true_occurences = dataframe[dataframe[col_name] == True]
    gen = df_with_true_occurences.groupby('SOURCE_KEY')['AC_POWER'].count().idxmax()
    return gen


pd.set_option('display.max_columns', None)
df_plant1 = pd.read_csv("Plant_1_Generation_Data.csv", parse_dates=['DATE_TIME'])
df_plant2 = pd.read_csv("Plant_2_Generation_Data.csv", parse_dates=['DATE_TIME'])

data = merge_data_frames(df_plant1, df_plant2)
data = data.dropna()

generator1_key = '1BY6WEcLGh8j5v7'

draw_plot_for_generator(data, generator1_key, '15.05.2020  00:00:00', '22.05.2020  00:00:00')
data = calculate_mean_for_generator_power_for_each_date(data)
data = check_if_power_was_under_the_mean(data)
print(data.to_string())

generator = check_generator_with_the_most_occurence_under_the_average_power(data)
print(generator)






