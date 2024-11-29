# import numpy as np
# import pandas as pd
# # #numpy arrays #1D
# # my_list=[1,4,5,3,2]
# # D1=np.array(my_list)
# # #print(D1)
# # #numpy arrays #2D
# # my_list=[[1,4,5,3,2],[11,3,3,3,2]]
# # D2=np.array(my_list)
# # # print(D2)
# # print(D2-2)
# # for i in range(len(D2)):
# #     D2[i]-=2
# # print(D2)

# ages = np.array([13,25,19])
# series1 = pd.Series(ages)
# #print(series1)

# ages = np.array([13,25,19])
# series1 = pd.Series(ages,index=['Emma', 'Swetha', 'Serajh'])
# #print(series1)

# dataf = pd.DataFrame([
#     ['John Smith','123 Main St',34],
#     ['Jane Doe', '456 Maple Ave',28],
#     ['Joe Schmo', '789 Broadway',51]
#     ],
#     columns=['name','address','age'])
# print(dataf)
# print(dataf.set_index('name'))

# import pandas as pd

# # Create a DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
# df = pd.DataFrame(data)

# # Calculate the mean of the 'Age' column
# print(df)

import numpy as np
import pandas as pd

a=np.array(range(1,10))
print(sum(a))

a=np.array