import pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy

#gss = pandas.read_csv('GSS_data.csv')


#gss.drop('Timestamp', axis=1, inplace=True)
#gss.drop('Email Address', axis=1, inplace=True)
#gss.drop(gss.columns[11], axis=1, inplace=True)
#gss.drop(gss.columns[21], axis=1, inplace=True)
#gss.drop(gss.columns[21], axis=1, inplace=True)
#gss.drop(gss.columns[21], axis=1, inplace=True)


#gssAnalysis = gss[['Space', 'concern', 'accustom', 'chirrup', 'solicitor', 'caprice', 'emanate', 'madrigal', 'encomium', 'tactility']]

#print(gssAnalysis.head())


#correlation = gssAnalysis.corr()

#sns.heatmap(correlation, annot=True)

#print(gss['Space'].unique())

#plt.show()


#print(gss.head())



vocabData = pd.read_csv('VocabTest.csv')


#print(vocabData['Score'].describe())

print(vocabData['Score'].mode())

vocabData = vocabData.drop('Score', axis=1)
sns.heatmap(vocabData.corr(), annot= True)


plt.show()