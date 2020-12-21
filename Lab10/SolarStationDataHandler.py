import pandas as pd
import matplotlib.pyplot as plt


def merge_data_frames(*dataframes):
    df = pd.concat(dataframes)
    return df


def compare_daily_yield_to_average(dataframe, generator_id):
    df = dataframe.copy()
    df['DATE'] = df['DATE_TIME'].dt.date
    df['MAX_DAILY_YIELD'] = df.groupby(['DATE', 'SOURCE_KEY'])['DAILY_YIELD'].transform('max')
    df['AVERAGE_FOR_EACH_DATE'] = df.groupby('DATE')['MAX_DAILY_YIELD'].transform('mean')
    current_generator_df = df[df['SOURCE_KEY'] == generator_id]
    df2 = current_generator_df.copy() #get rid of setting copy warning

    df2['Gen-avg ratio'] = df2.apply(lambda row: row['MAX_DAILY_YIELD'] / row['AVERAGE_FOR_EACH_DATE'], axis=1)
    df2.loc[:, 'Gen-avg ratio percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df2['Gen-avg ratio']], index=df2.index)
    df2 = df2.drop(['DATE_TIME', 'AC_POWER', 'DC_POWER', 'DAILY_YIELD', 'TOTAL_YIELD'], axis=1)
    df2 = df2.drop_duplicates()
    return df2


def get_cmap(n, name='hsv'): #rozwiązanie pochodzi ze stackoverflow (do losowania kolorów)
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


def draw_plots_ac_or_dc_power(df, main_generators_id, main_generators_id2, generators_to_compare_ids, start_date, end_date, ac_or_dc='AC_POWER'):
    #ta metoda nie jest najlepiej napisana, ale miałem problemy ze znalezieniem błędu :(
    plot_df = df.copy()
    plot_df = plot_df.loc[df['SOURCE_KEY'] == main_generators_id]
    plot_df = plot_df.set_index(['DATE_TIME'])

    plot_df = plot_df.loc[start_date:end_date]
    plot_df = plot_df.reset_index()
    plt.plot(plot_df['DATE_TIME'], plot_df[ac_or_dc], color='blue', linewidth=2, label="Generator: {}".format(main_generators_id))
    plt.xlabel('Date Time')
    plt.ylabel('AC POWER')
    new_plot_df = df.copy()
    new_plot_df = new_plot_df.loc[df['SOURCE_KEY'] == main_generators_id2]
    new_plot_df = new_plot_df.set_index(['DATE_TIME'])
    new_plot_df = new_plot_df.loc[start_date:end_date]
    new_plot_df = new_plot_df.reset_index()

    plt.plot(new_plot_df['DATE_TIME'],new_plot_df[ac_or_dc], color='red', linewidth=2, label="Generator: {}".format(main_generators_id2))

    if len(generators_to_compare_ids) != 4:
        pass
    else:
        for i in range(4):
            new_plot_df = df.copy()
            new_plot_df = new_plot_df.loc[df['SOURCE_KEY'] == generators_to_compare_ids[i]]
            new_plot_df = new_plot_df.set_index(['DATE_TIME'])
            new_plot_df = new_plot_df.loc[start_date:end_date]
            new_plot_df = new_plot_df.reset_index()

            cmap = get_cmap(25)

            plt.plot(new_plot_df['DATE_TIME'], new_plot_df[ac_or_dc], color=cmap(i*6),
                     linestyle='dashed', linewidth=1,
                     label="Generator: {}".format(generators_to_compare_ids[i]))

    plt.title('Comparison of AC/DC POWER')


def draw_yield_figure(dataframe, generator_id):
    df = compare_daily_yield_to_average(dataframe, generator_id)
    ratio_under_75 = (df['Gen-avg ratio'] < 0.75).sum()
    ratio_75_85 = ((df['Gen-avg ratio'] >= 0.75) & (df['Gen-avg ratio'] < 0.85)).sum()
    ratio_85_95 = ((df['Gen-avg ratio'] >= 0.85) & (df['Gen-avg ratio'] < 0.95)).sum()
    ratio_95_105 = ((df['Gen-avg ratio'] >= 0.95) & (df['Gen-avg ratio'] < 1.05)).sum()
    ratio_105_115 = ((df['Gen-avg ratio'] >= 1.05) & (df['Gen-avg ratio'] < 1.15)).sum()
    ratio_115_125 = ((df['Gen-avg ratio'] >= 1.15) & (df['Gen-avg ratio'] < 1.25)).sum()
    ratio_above_125 = (df['Gen-avg ratio'] >= 1.25).sum()

    ratios = ['<75%', '75%-85%', '85%-95%', '95%-105%', '105%-115%', '115%-125%', '125%>']
    counts = [ratio_under_75, ratio_75_85, ratio_85_95, ratio_95_105, ratio_105_115, ratio_115_125, ratio_above_125]
    plt.bar(ratios, counts)
    plt.title(' Daily yield ratio for generator {}'.format(generator_id))
    plt.xlabel('Ratio')
    plt.ylabel('Counts')


def create_subplots(df, main_generators_id, main_generators_id2, generators_to_compare_ids, start_date, end_date):

    plt.subplot(2, 2, 1)
    draw_plots_ac_or_dc_power(df, main_generators_id, main_generators_id2, generators_to_compare_ids, start_date, end_date)
    plt.legend(loc='upper left')

    plt.subplot(2, 2, 2)
    draw_plots_ac_or_dc_power(df, main_generators_id, main_generators_id2, generators_to_compare_ids, start_date, end_date, 'DC_POWER')
    plt.legend(loc='upper left')

    plt.subplot(2, 2, 3)
    draw_yield_figure(df, main_generators_id)

    plt.subplot(2, 2, 4)
    draw_yield_figure(df, main_generators_id2)

    plt.show()


pd.set_option('display.max_columns', None)
df_plant1 = pd.read_csv("Plant_1_Generation_Data.csv", parse_dates=['DATE_TIME'])
df_plant2 = pd.read_csv("Plant_2_Generation_Data.csv", parse_dates=['DATE_TIME'])

data = merge_data_frames(df_plant1, df_plant2)
data = data.dropna()

generator1_key = '1BY6WEcLGh8j5v7'
main_generators = ['1BY6WEcLGh8j5v7', 'VHMLBKoKgIrUVDU']
generators_to_compare = ['1IF53ai7Xc0U56Y', '3PZuoBAID5Wc2HD', '7JYdWkrLSPkdwr4', 'McdE0feGgRqW7Ca']
start_date = '15.05.2020  00:00:00'
end_date = '22.05.2020  00:00:00'

compare_daily_yield_to_average(data, generator1_key)
create_subplots(data, '1BY6WEcLGh8j5v7', 'pkci93gMrogZuBj', generators_to_compare, start_date, end_date)
