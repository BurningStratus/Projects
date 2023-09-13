
# DONE store times of  the year in a tuple
# DONE index times of the year as nums of the months
# DONE prog asks user num of the month and prints corresponding time of the year(Dec = 1st)

year = ("DEC", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV")

(fir, sec, thi, fou, fif, six, sev, eig, nin, ten, elev, twlv) = year
fir, sec, thi, fou, fif, six = 1, 2, 3, 4, 5, 6
sev, eig, nin, ten, elev, twlv = 7, 8, 9, 10, 11, 12

num = int(input("Number of the month of the year> "))
print(f"It is {year[num-1]}.")