import csv

# diffrent Attributes
Attributes = [['Sunny','Rainy'],['Warm','Cold'],['Normal','High'],['Strong','Weak'],["Warm",'Cool'],['Same','Change']]

#Number of Diffrent attributes
Num_Attributes = len(Attributes)

a = []

#Reading The file XYX 
with open('XYX.csv') as f:
    reader = csv.reader(f)
    
    
    for line in reader:
        #read the contents and append it to empty list 
        a.append(line)
        print(line)
#initial value of hypothesis is initialized
print('initial value of hypothesis: -')
#Maximal genaralised hypothesis
hypothesis = ['0'] * Num_Attributes
print(hypothesis)

for j in range(0, Num_Attributes):
    hypothesis[j] = a[0][j]
    
#finding The most specific Hypothesis

for i in range(0, len(a)):

    if a[i][Num_Attributes] == 'YES':

        for j in range(0, Num_Attributes):

            if a[i][j] != hypothesis[j]:
                #replacing the unmatched attributes to a general "?
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]



print("For training example No  : {0} the hypothesis is ".format(i), hypothesis)
print("Maximal specific hypothesis : ")
print(hypothesis)               