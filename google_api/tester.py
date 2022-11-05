import pandas as pd

dataset = pd.read_excel('./TimeEdit_2022-10-11_12_53.xls')
begDate = dataset['Begin date']
begTime = dataset['Begin time']
endDate = dataset['End date']
endTime = dataset['End time']
activityType = dataset['Activity']
location = dataset['Room, Location Comment']
teacher = dataset['Teacher, External teacher']
description = dataset['Title, Public comment, URL']
course = dataset['Course']


begDate.fillna("", inplace=True)
begTime.fillna("", inplace=True)
endDate.fillna("", inplace=True)
endTime.fillna("", inplace=True)
activityType.fillna("", inplace=True)
location.fillna("", inplace=True)
teacher.fillna("", inplace=True)
description.fillna("", inplace=True)
course.fillna("", inplace=True)


begin_info = begDate + "T" + begTime + ":00"
end_info = endDate + "T" + endTime + ":00"
#print(begin_info[44])

# i = 0
# while begDate[i] != pd.isna:
#     print(begin_info[i])
#     i+=1

# def changetype(test):
#     if test != "NaN":
#         changetype = str(test)
#     else:
#         changetype = " "
