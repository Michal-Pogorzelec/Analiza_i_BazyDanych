import math
import numpy
import pandas as pd



table_mockup = {"Data": [], "TMAX": [[] for _ in range(10)], "TMIN": [[] for _ in range(10)], "idx": []}

early_process = pd.read_fwf("../../Original Data/weather.txt")
print(early_process)

# ***** Data Processing *****

for i, (column, row) in enumerate(early_process.items()):
    if row.values[0] == 'MX000017004195504TMIN':
        for j, elem in enumerate(row.values):
            if elem[11:15] == "2010":
                if not elem[-3:] == "RCP":
                    # correct_idx.append(j)
                    table_mockup["Data"].append(elem[11:])
                    table_mockup["idx"].append(j)
                    # print(elem)
            if len(table_mockup["idx"]) >= 10:
                break
    break


for i, (column, row) in enumerate(early_process.items()):
    if (i%2 == 0) and (i not in [56, 58]):
        continue # parzyste kolumny są 'przerywnikami', "I" lub "S" w tekscie
        # oprócz 56 i 58, gdzie przez przypadek zrobiło I razem z pomiarami

    for j, measurement in enumerate(row.values):
        if j in table_mockup["idx"]:
            curr_idx = table_mockup["idx"].index(j)
            if table_mockup["Data"][curr_idx][-3:] == "MAX":
                table_mockup["TMAX"][curr_idx].append(measurement)
            else:
                table_mockup["TMIN"][curr_idx].append(measurement)


for i, elem in enumerate(table_mockup["TMIN"]):
    if elem == []:
        table_mockup["TMIN"].pop(i)

for i, elem in enumerate(table_mockup["TMAX"]):
    if elem == []:
        table_mockup["TMAX"].pop(i)

# print(table_mockup["TMIN"])
# print(type(table_mockup["TMAX"][0][0]))
# print(len(table_mockup["TMIN"]), len(table_mockup["TMAX"]))
#
# print(table_mockup)

# ***** Generating the results *****

processed_data = {"ID": [], "Date": [], "TMax": [], "TMin": []}
counter_tmax = 0
counter_tmin = 0

for month in range(5):
    for day in range(31):
        day_str = str(day+1)
        if len(day_str) < 2:
            day_str = "0" + day_str
        month_str = "0" + str(month+1)

        date = table_mockup["Data"][month][:4] + "-" + month_str + "-" + day_str

        processed_data["ID"].append("MX000017004")
        processed_data["Date"].append(date)

        tmax = table_mockup["TMAX"][month][day]
        tmin = table_mockup["TMIN"][month][day]

        if isinstance(tmax, numpy.int64):
            if tmax >= 900 or tmax <= -9999 or tmax == math.nan:
                processed_data["TMax"].append(math.nan)
                counter_tmax += 1
            else:
                processed_data["TMax"].append(tmax)
                counter_tmax += 1
        elif isinstance(tmax, str):
            try:
                tmax = int(tmax)
                if tmax >= 900 or tmax <= -9999 or tmax == math.nan:
                    processed_data["TMax"].append(math.nan)
                    counter_tmax += 1
                else:
                    processed_data["TMax"].append(tmax)
                    counter_tmax += 1
            except:
                processed_data["TMax"].append(math.nan)
                counter_tmax += 1

        if isinstance(tmin, numpy.int64):
            if tmin >= 900 or tmin <= -9999 or tmin == math.nan:
                processed_data["TMin"].append(math.nan)
                counter_tmin += 1
            else:
                processed_data["TMin"].append(tmin)
                counter_tmin += 1
        elif isinstance(tmin, str):
            try:
                tmin = int(tmin)
                if tmin >= 900 or tmin <= -9999 or tmin == math.nan:
                    processed_data["TMin"].append(math.nan)
                    counter_tmin += 1
                else:
                    processed_data["TMin"].append(tmin)
                    counter_tmin += 1
            except:
                processed_data["TMin"].append(math.nan)
                counter_tmin += 1


clear_data = pd.DataFrame(processed_data)
print(clear_data)

clear_data.to_csv("../../Analysis Data/weather_final.csv")


