import pandas as pd
import matplotlib.pyplot as plt


data = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Pavel', 'Lena', 'Katya', 'Kostya', 'Eugene'],
    'Математика' :      [3, 4, 4, 4, 2, 5, 5, 3, 4, 3],
    'Русский язык' :    [3, 4, 4, 4, 3, 5, 5, 3, 2, 3],
    'Английский язык' : [3, 4, 5, 4, 3, 5, 5, 5, 4, 3],
    'Физкультура' :     [2, 4, 5, 4, 3, 2, 5, 5, 2, 3],
    'Физика' :          [1, 4, 5, 4, 3, 4, 4, 4, 4, 3]
    }

df = pd.DataFrame(data)

print(df.head())
sr_math = df['Математика'].mean()
med_math = df['Математика'].median()
print("Математика", sr_math, med_math)

sr_rus = df['Русский язык'].mean()
med_rus = df['Русский язык'].median()
print('Русский язык',sr_rus, med_rus)

sr_eng = df['Английский язык'].mean()
med_eng = df['Английский язык'].median()
print('Английский язык', sr_eng, med_eng)

sr_sport = df['Физкультура'].mean()
med_sport = df['Физкультура'].median()
print('Физкультура',sr_sport, med_sport)

sr_phy = df['Физика'].mean()
med_phy = df['Физика'].median()
print('Физика',sr_phy, med_phy)

#print(df.describe())


Q1_Math = df['Математика'].quantile(0.25)
Q3_Math = df['Математика'].quantile(0.75)
IQR_Math = Q3_Math - Q1_Math
STD_Math = df['Математика'].std()

print(Q1_Math, Q3_Math, IQR_Math, STD_Math)

#df.boxplot('Математика')
#plt.show()