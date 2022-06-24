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



Load the dataset into R:

vocabData <- read.csv(file.choose(),sep=',')

![image](https://user-images.githubusercontent.com/76405713/175438562-76622250-59a6-414c-99f8-611cc31fecf9.png)


The score column needs to be dropped to do factor analyze the matrix.

library(dplyr)

select(vocabData, -c(Score))

Before factor analysis, the reliability of the test needs to be known. The most common way to do this is by computing the Cronbach's alpha coefficient. High values for cronbach's alpha indicate the test items are reliable and measuring something valid.

vocabData <- select(vocabData,-c(Score))

cronbach.alpha(vocabData)

![image](https://user-images.githubusercontent.com/76405713/175440609-488e2cdc-1fcf-4ae9-9c5a-a012e9fd19c0.png)

The coefficient of 0.837 indicates very good reliability.


Next, a principal component analysis needs to be done to analyze the number of different factors that explain the performance on the test items.

We can do this using the in-built function princomp

vocabData.pca <- princomp(vocabData)

summary(vocabData.pca)


![image](https://user-images.githubusercontent.com/76405713/175440830-a2032051-9b6d-4026-ad55-2a8e113db9a2.png)

As it can be seen, the first component explains around 47% of the variance with subsequent factors explaining much less.
This can be seen easily through a plot.

plot(vocabData.pca)


![image](https://user-images.githubusercontent.com/76405713/175440973-34526ad0-5daf-430c-8116-9b1cdbb156b8.png)


This means that there is one factor which explains most of the variance in performance. As mentioned earlier, this is the result we would expect and this factor is most likely the g factor.
This needs to be confirmed through confirmatory factor analysis.

We can do this through the in built R function factanal.


vocabData.fa1 <- factanal(vocabData, factors=1)
vocabData.fa1

![image](https://user-images.githubusercontent.com/76405713/175441397-9ef92fc7-f44b-4915-89cb-e9e67530a0ab.png)


This gives the factor loadings of each question and conducts a hypothesis test with the null hypothesis being that one factor is sufficient. In this case, the p-value barely indicates evidence against the null hypothesis with a significance level of 5%. We would reject the null hypothesis that there is only one factor.

If we try CFA with 2 factors:


vocabData.fa2 <- factanal(vocabData, factors=2)

vocabData.fa2

![image](https://user-images.githubusercontent.com/76405713/175442402-049036ca-e9d7-4b66-b09b-ada8202ed0a7.png)


The p-value in this case is not statistically significant. In this case, we would not reject the null hypothesis that 2 factors are sufficient. 

As it can be seen, even though the PCA indicated there is one factor explaining most of the variance in test performance between individuals, the CFA failed to confirm that. 

I do believe the test to be significantly g loaded. The reason the analyses failed to confirm this is likely due to the small sample size and skewed sample data.

This analysis will be updated once the data is sufficient.






















