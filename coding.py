import plotly.figure_factory as pff
import random
import statistics
import csv
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
math_list = df["math score"].to_list()

math_mean = statistics.mean(math_list)
print(math_mean)

math_median = statistics.median(math_list)
print(math_median)

math_mode = statistics.mode(math_list)
print(math_mode)

math_stan_dev = statistics.stdev(math_list)
print(math_stan_dev)

fir_stan_dev_star = math_mean-math_stan_dev
fir_stan_dev_en = math_mean+math_stan_dev

list_of_data_within_1_std_deviation = [
    result for result in math_list if result > fir_stan_dev_star and result < fir_stan_dev_en
]

sec_stan_dev_star = math_mean-(2*math_stan_dev)
sec_stan_dev_en = math_mean+(2*math_stan_dev)

list_of_data_within_2_std_deviation = [
    result for result in math_list if result > sec_stan_dev_star and result < sec_stan_dev_en
]

thi_stan_dev_star = math_mean-(3*math_stan_dev)
thi_stan_dev_en = math_mean+(3*math_stan_dev)

list_of_data_within_3_std_deviation = [
    result for result in math_list if result > thi_stan_dev_star and result < thi_stan_dev_en
]

print("{}% of data lies within the 1st standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data lies within the 2nd standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data lies within the 3rd standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(math_list)))

figure = pff.create_distplot([math_list],["Result"],show_hist=False)
figure.show()