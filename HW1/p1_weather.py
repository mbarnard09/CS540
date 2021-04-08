import io
import datetime


def manhattan_distance(data_point1, data_point2):
    x = (data_point1["TMAX"] - data_point2["TMAX"]) + (data_point1["PRCP"] -
        data_point2["PRCP"]) + (data_point1["TMIN"] - data_point2["TMIN"])
    return x

def read_dataset(filename):
    f = open(filename, 'r')
    bigList = []
    for line in f:
        line = line.strip('\n')
        list = line.split(' ')
        dict = {
            "DATE": list[0],
            "TMAX": float(list[2]),
            "PRCP": float(list[1]),
            "TMIN": float(list[3]),
            "RAIN": list[4],
        }
        bigList.append(dict)
    f.close()
    return bigList

def majority_vote(nearest_neighbors):
    true = 0
    false = 0
    for item in nearest_neighbors:
        if(item['RAIN'] == 'TRUE'):
            true += 1
        elif(item['RAIN'] == 'FALSE'):
            false += 1
    if true > false or true == false:
        return 'TRUE'
    else:
        return 'FALSE'


def k_nearest_neighbors(filename, test_point, k, year_interval):
    f = open(filename, 'r')
    date = datetime.datetime.strptime(test_point["DATE"], "%Y-%m-%d")
    plusdate = date.replace(year = date.year + year_interval)
    minusdate = date.replace(year = date.year - year_interval)

    bigList = read_dataset(filename)

    finalList = []
    for d in bigList:

        da = datetime.datetime.strptime(d["DATE"], "%Y-%m-%d")
        if(da > minusdate and da < plusdate):
            finalList.append(d)
    actuallyFinalList = []
    # this is where im not sure 
    return 'TRUE'




#print(manhattan_distance({'DATE': '1951-05-19', 'TMAX': 66.0, 'PRCP': 0.0, 'TMIN': 43.0, 'RAIN': 'FALSE'},{'DATE': '1951-01-27', 'TMAX': 33.0, 'PRCP': 0.0, 'TMIN': 19.0, 'RAIN': 'FALSE'}))
#print(manhattan_distance({'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'}, {'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'}))

#dataset = read_dataset(r'C:\Users\Owner\Documents\Atom\CS540\HW1\rain.txt')

#print(len(dataset))
#print(dataset[0])

#print(majority_vote([{'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'},
#{'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'},
#{'DATE': '2014-12-05', 'TMAX': 55.0, 'PRCP': 0.12, 'TMIN': 44.0, 'RAIN': 'TRUE'},
#{'DATE': '2014-08-27', 'TMAX': 84.0, 'PRCP': 0.0, 'TMIN': 61.0, 'RAIN': 'FALSE'}]))


#print(k_nearest_neighbors(r'C:\Users\Owner\Documents\Atom\CS540\HW1\rain.txt', {'DATE': '1958-01-01', 'TMAX': 51.0, 'PRCP': 0.47, 'TMIN': 42.0}, 2, 10))
