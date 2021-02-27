from sklearn import svm


# Create a function to determine the most acturate 
def SVM_kernal_Optim(train1, test1, train2, test2, C=1):
    values=[]
    for kernal in 'linear', 'rbf', 'poly':
        clf = svm.SVC()  # initiate SVM
        clf = svm.SVC(kernel=kernal, C=C).fit(train1.tolist(), train2.tolist())  
        success = 0
        for i in range(0, len(test1)):
            predictionT = (clf.predict([test1.iloc[i]]))
            actualT = test2.iloc[i]
            if predictionT == actualT:
                success += 1
                answer = 'True'
            else:
                answer = 'False'
        successr = 100*success/len(test1)
        #print('With a {} kernal, a success rate of {:#.4g}% was found.'.format(kernal, successr))
        values.append(successr)
    return values

# Create a function to determine most acruate Kernal based on multiple random sets

    
