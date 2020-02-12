x_month = []
y_gap = []

with open("offerten.csv", "r") as file:

    for line in file:
        if "Month" in line:
            continue

        data = line.strip().split(";")
        sales = int(data[1]) + int(data[2])
        sales_netto = sales // 1.077
        sales_ohne_ex = sales_netto - int(data[3]) - int(data[4])
        gap = 8000 - sales_ohne_ex 
        y_gap.append(int(gap))
        x_month.append(data[0])

print(x_month)
print(y_gap)

import matplotlib.pyplot as plt



steuer_mon = []

with open("steuer.csv", "r") as file:
    for line in file:
        if "Month" in line:
            continue
        data = line.strip().split(";")
        steuer_betr = int(data[6])
        steuer_mon.append(steuer_betr)
        steuer_jahr = sum(steuer_mon)
print(steuer_mon)
print(steuer_jahr)

cf_month = []
month = []

with open("Cashflow.csv", "r") as file:
    for line in file:
        if "Month" in line:
            continue
        data = line.strip().split(";")
        cf = int(data[1])
        cf_month.append(cf)
        month.append(data[0])

import matplotlib.pyplot as plt

plt.plot(x_month, y_gap)
plt.plot(month, cf_month)
plt.show()
plt.show()


