month = []
gap = []

with open("offerten.csv", "r") as file:

    for line in file:
        if "Month" in line:
            continue

        data = line.strip().split(";")
        sales = int(data[1]) + int(data[2])
        sales_netto = sales // 1.077
        sales_ohne_ex = sales_netto - int(data[3]) - int(data[4])
        gap_mon = 8000 - sales_ohne_ex
        gap.append(int(gap_mon))
        month.append(data[0])

print(gap)


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

cf_month = []

with open("Cashflow.csv", "r") as file:
    for line in file:
        if "Month" in line:
            continue
        data = line.strip().split(";")
        cf = int(data[1])
        cf_month.append(cf)
print(cf_month)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(month, gap, label="Revenue Gap")
ax.plot(month, cf_month, label="Cashflow")
ax.plot(month, steuer_mon, label="Acc for taxes")
ax.legend()

plt.show()






