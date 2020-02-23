from django import forms
import csv

path = r'C:\Users\alexd\Desktop\Kabum\kabum_backend\kabum_backend\user.csv'

usersList = []

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        usersList.append(row[1])
        line_count += 1

class usersClass(forms.Form):
    users = forms.CharField(widget=forms.RadioSelect(choices=usersList))
    test2 = usersList
