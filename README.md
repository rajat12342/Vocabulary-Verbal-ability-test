# Vocabulary-Verbal-ability-test


Background and hypothesis: I have created a short vocabulary test consisting of 10 questions that I'm conjecturing has a significant g loading and can be used as a 10 minute test of general cognitive ability. The test questions were chosen from a test bank containing vocabulary items used by the American General Social Survey(1972-2008) and from the old Binet vocabulary cards.

The test can be found here: 
https://forms.gle/H1Qm6HMFBjbMK8E38

Data collection: In order to collect data, the test was posted on the cognitiveTesting subreddit. This subreddit consists primarily of individuals who are in the top 10% of general intelligence. The main problem with the data is that it is not representative of the general population. But when better data is not available and can't be easily gathered, this will have to suffice. The csv file contains the responses of n=21 people who answered all of the 10 questions on the test.


The analysis was done in Python and R.

Initial observations: 


Data was loaded into python: 

vocabData = pd.read_csv('VocabTest.csv')

print(VocabData.head())

![image](https://user-images.githubusercontent.com/76405713/175430845-c3f59c7b-ff60-4016-aa3f-1e0a562b6b36.png)


Check for missing values:

print(vocabData.isnull().sum())

![image](https://user-images.githubusercontent.com/76405713/175430894-37a29093-61e0-4535-b399-234f27030eba.png)

No missing values found.

Checking the distribution of total scores variable and summary statistics:

print(vocabData['Score'].describe())

![image](https://user-images.githubusercontent.com/76405713/175431095-e8cb6614-b9dd-4626-a8d8-194ebf42aa0f.png)

The scores are slightly right skewed as evident by the mean being higher than the median. This is expected since the data is not from a representative sample.

sns.histplot(data = vocabData, x='Score')
plt.show()

![image](https://user-images.githubusercontent.com/76405713/175431606-d4e27fde-a59e-46f9-9f43-bb2559c81199.png)

Using kde plot:

sns.kdeplot(data = vocabData, x='Score', shade=True)
plt.show()

![image](https://user-images.githubusercontent.com/76405713/175431829-4074758b-f3ee-4b60-b4ea-271e51b11c27.png)
















