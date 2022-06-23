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


![image](https://user-images.githubusercontent.com/76405713/175430455-7629f4f9-6781-4202-a20c-353e645bdfd8.png)
