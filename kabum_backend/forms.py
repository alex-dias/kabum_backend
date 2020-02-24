# This methods are used to read csv files, this files are storing information
# from users and products. This approach was taken for being more versatile,
# it can work with any csv files following the same pattern
import csv
# Files paths
usersPath = r'kabum_backend\user.csv'
productsPath = r'kabum_backend\products.csv'
# Lists to get every row from the csv files
usersList = []
productList = []
# Reading the user csv file
with open(usersPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # Adding to the list every id and username
        usersList.append([row[0], row[1]])
        line_count += 1

# Reading the products csv file
with open(productsPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # Adding to the list every id, product name, price and multiplier
        productList.append([row[0],row[1],row[2],row[3]])
        line_count += 1

# Creation of simple classes for user and product
class usersClass():
    userNames = usersList

class productClass():
    productsCollection = productList
