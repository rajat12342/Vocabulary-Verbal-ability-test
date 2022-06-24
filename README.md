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

Pearson's coefficient of skewness was 0.123, confirming a slight right skew.
print(scipy.stats.skew(vocabData['Score']))


If the score column is dropped, the a heatmap with the correlations between scores on different questions can be devised.

vocabData = vocabData.drop('Score', axis=1)

sns.heatmap(vocabData.corr(), annot= True)

![image](https://user-images.githubusercontent.com/76405713/175436398-72ef7426-9a61-4065-b3c4-dcf112fd1d23.png)

Performance on most test items is positively correlated with performance on most other items. This is an indication that there is a higher order factor that can explain most of the variance in performance that exists between individuals. 

In psychometrics, this higher order factor is called the "g-factor". g is short for general intelligence and it is this factor which explains most of the differences in performance between individuals on various cognitive tasks. This factor is extracted using methods such as principal component analysis and confirmatory factor analysis. Vocabulary tests tend to load strongly on g and are a good measure of the g factor. Past research has shown that g loadings of items administered to high ability individuals tends to be lower than if those same items were given to a representative sample. However, I will still try to calculate the g loadings of the various test items in R.























