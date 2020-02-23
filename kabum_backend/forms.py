import csv

usersPath = r'C:\Users\alexd\Desktop\Kabum\kabum_backend\kabum_backend\user.csv'
productsPath = r'C:\Users\alexd\Desktop\Kabum\kabum_backend\kabum_backend\products.csv'

usersList = []
productList = []

with open(usersPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        usersList.append([row[0], row[1]])
        line_count += 1


with open(productsPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        productList.append([row[0],row[1],row[2],row[3]])
        line_count += 1

class usersClass():
    userNames = usersList

class productClass():
    productsCollection = productList
