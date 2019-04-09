from SimPy import InOutFunctions as InOutSupport
from SimPy import FigureSupport as Fig
from SimPy import StatisticalClasses as Stat
from SimPy import FittingProbDist_ML as FitML

# read interarrival times
cols = InOutSupport.read_csv_cols(file_name='dataInterarrivalTimes.csv',
                                  n_cols=1,
                                  if_ignore_first_row=True,
                                  if_convert_float=True)

# make a histogram
Fig.graph_histogram(data=cols[0],
                    title='Interarrival Times (Minutes)',
                    bin_width=0.5
                    )

# mean and standard deviation
stat = Stat.SummaryStat(name='Interarrival times',
                        data=cols[0])
print('Mean = ', stat.get_mean())
print('StDev = ', stat.get_stdev())

