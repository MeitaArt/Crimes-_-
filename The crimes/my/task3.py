from json import dumps
indexes_to_int = [0, 2, 3, 4]
to_bool = [7]
index_of_name = 5
crimes = {}


with open("../Crimes.csv") as file:
    header = file.readline().rstrip().split(",")
    header.pop(index_of_name)
    for line in file:
        crime_list = line.rstrip().split(",")
        for i in range(len(crime_list)):
            if i in indexes_to_int:
                if crime_list[i] != "-":
                    crime_list[i] = int(crime_list[i])
            elif i in to_bool:
                if crime_list[i] == "True":
                    crime_list[i] = True
                elif crime_list[i] == "False":
                    crime_list[i] = False

        name = crime_list.pop(index_of_name)
        dct = {}
        for i in range(len(header)):
            dct[header[i]] = crime_list[i]

        if name in crimes:
            crimes[name].append(dct)

        else:
            crimes[name] = [dct]


