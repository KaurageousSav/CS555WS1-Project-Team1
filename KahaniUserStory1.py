#!/usr/bin/env python
# coding: utf-8

# In[5]:


string1 = 'BIRT'
string2 = 'PMARR'
with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
    lines = f.readlines()




def birtbefparmarr():
    i = 0
    for line in lines:

        if string1 in line and string2 in lines[i + 2]:

            BirthDate = lines[i + 1]
            BirthDateSplit = str.split(BirthDate)
            BirthDateSplit[2] = ' '.join(BirthDateSplit[2:])
            FinalBirthDate = BirthDateSplit[2]
            FinalBirthDateList = []
            FinalBirthDateList.append(FinalBirthDate)
            print(lines[i - 2])
            # print(FinalBirthDateList)
            print('Birth date:' + FinalBirthDate)
            BirthDateArray = str.split(FinalBirthDate)
            FinalBirthYear = BirthDateArray[2]
            FinalBirthYearList = []
            FinalBirthYearList.append(FinalBirthYear)
            # print(FinalBirthYearList)

            parMarriageDate = lines[i + 3]
            parMarriageDateSplit = str.split(parMarriageDate)
            parMarriageDateSplit[2] = ' '.join(parMarriageDateSplit[2:])
            FinalparMarriageDate = parMarriageDateSplit[2]
            FinalparMarriageDateList = []
            FinalparMarriageDateList.append(FinalparMarriageDate)
            # print(FinalparMarriageDateList)
            print('parent Marriage date:' + FinalparMarriageDate)
            parMarriageDateArray = str.split(FinalparMarriageDate)
            FinalparMarriageYear = parMarriageDateArray[2]
            FinalparMarriageYearList = []
            FinalparMarriageYearList.append(FinalparMarriageYear)
            # print(FinalparMarriageYearList)
            if FinalBirthYear < FinalparMarriageYear and FinalBirthDate != FinalparMarriageDate:
                print('Birth year < parent Marriage year')

            else:
                print('The child is considered as an anomaly')

        i += 1

# In[ ]:




