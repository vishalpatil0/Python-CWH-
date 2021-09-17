import pandas as pd
scores=pd.read_csv("CSV File\scores.csv")
# print(scores['Total'].sort_values(ascending=False))
# print(type(scores)) # raw file
# print(scores)
# print(scores.shape) #tells you the diemesion
# print(scores.tail)
print(scores["Name"])












# with open('CSV File\scores.csv','r') as f:
#     scores=f.readlines()[1:]
#     max=0
#     for record in scores:
#         fields=record.split(',')
#         if(int(fields[8])>max):
#             max=int(fields[8])
#     print(max)