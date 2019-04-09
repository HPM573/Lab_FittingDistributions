from SimPy import InOutFunctions as InOutSupport
from SimPy import FigureSupport as Fig
from SimPy import StatisticalClasses as Stat
from SimPy import FittingProbDist_ML as FitML

# read weekly number of drinks
cols = InOutSupport.read_csv_cols(file_name='dataNumOfDrinks.csv',
                                  n_cols=1,
                                  if_ignore_first_row=True,
                                  if_convert_float=True)

# make a histogram
Fig.graph_histogram(data=cols[0],
                    title='Weekly Number of Drinks',
                    bin_width=1
                    )

# mean and standard deviation
stat = Stat.SummaryStat(name='Weekly number of drinks',
                        data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())


