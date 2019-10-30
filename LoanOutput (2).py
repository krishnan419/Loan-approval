from tkinter import *
window=Tk()

depender=StringVar()
depender.set("0")
gender=StringVar()
gender.set("Male")
married=StringVar()
married.set("Yes")
graduate=StringVar()
graduate.set("Graduate")
employed=StringVar()
employed.set("Yes")
credit_history=StringVar()
credit_history.set("1")
area=StringVar()
area.set("Rural")

window.title("Loan approval prediction")

Label(window,text="Loan-id",bg="black",fg="white",font="none 12 bold",width=15).grid(row=1,column=0,sticky=W)
Loan_ID=Entry(window,width=20,bg="white")
Loan_ID.grid(row=1,column=1,sticky=W)

Label(window,text="Gender",bg="black",fg="white",font="none 12 bold",width=15).grid(row=2,column=0,sticky=W)
Male=Radiobutton(window,text="Male",variable=gender,value="Male")
Male.grid(row=2,column=1)
Female=Radiobutton(window,text="Female",variable=gender,value="Female")
Female.grid(row=2,column=2)


Label(window,text="Married",bg="black",fg="white",font="none 12 bold",width=15).grid(row=3,column=0,sticky=W)
Married=Radiobutton(window,text="Yes",variable=married,value="Yes")
Married.grid(row=3,column=1)
UnMarried=Radiobutton(window,text="No",variable=married,value="No")
UnMarried.grid(row=3,column=2)

Label(window,text="Depender",bg="black",fg="white",font="none 12 bold",width=15).grid(row=4,column=0,sticky=W)
r1=Radiobutton(window,text="0",variable=depender,value=0)
r1.grid(row=4,column=1)
r2=Radiobutton(window,text="1",variable=depender,value=1)
r2.grid(row=4,column=2)
r3=Radiobutton(window,text="2",variable=depender,value=2)
r3.grid(row=4,column=3)
r4=Radiobutton(window,text="3+",variable=depender,value=3)
r4.grid(row=4,column=4)

Label(window,text="Education",bg="black",fg="white",font="none 12 bold",width=15).grid(row=5,column=0,sticky=W)
Graduate=Radiobutton(window,text="Graduate",variable=graduate,value="Graduate")
Graduate.grid(row=5,column=1)
NotGraduate=Radiobutton(window,text="Not Graduate",variable=graduate,value="Not Graduate")
NotGraduate.grid(row=5,column=2)

Label(window,text="Self-employed",bg="black",fg="white",font="none 12 bold",width=15).grid(row=6,column=0,sticky=W)
Employed=Radiobutton(window,text="Yes",variable=employed,value="Yes")
Employed.grid(row=6,column=1)
NotEmployed=Radiobutton(window,text="No",variable=employed,value="No")
NotEmployed.grid(row=6,column=2)

Label(window,text="Applicant income",bg="black",fg="white",font="none 12 bold",width=15).grid(row=7,column=0,sticky=W)
ApplicantIncome=Entry(window,width=20,bg="white")
ApplicantIncome.grid(row=7,column=1,sticky=W)

Label(window,text="Co-Applicant income",bg="black",fg="white",font="none 12 bold",width=15).grid(row=8,column=0,sticky=W)
CoapplicantIncome=Entry(window,width=20,bg="white")
CoapplicantIncome.grid(row=8,column=1,sticky=W)

Label(window,text="Loan Amount",bg="black",fg="white",font="none 12 bold",width=15).grid(row=9,column=0,sticky=W)
LoanAmount=Entry(window,width=20,bg="white")
LoanAmount.grid(row=9,column=1,sticky=W)

Label(window,text="Loan Amount Term",bg="black",fg="white",font="none 12 bold",width=15).grid(row=10,column=0,sticky=W)
Loan_Amount_Term=Entry(window,width=20,bg="white")
Loan_Amount_Term.grid(row=10,column=1,sticky=W)

Label(window,text="Credit History",bg="black",fg="white",font="none 12 bold",width=15).grid(row=11,column=0,sticky=W)
CreditHistory=Radiobutton(window,text="0",variable=credit_history,value=0)
CreditHistory.grid(row=11,column=1)
NoCreditHistory=Radiobutton(window,text="1",variable=credit_history,value=1)
NoCreditHistory.grid(row=11,column=2)

Label(window,text="Property Area",bg="black",fg="white",font="none 12 bold",width=15).grid(row=12,column=0,sticky=W)
Rural=Radiobutton(window,text="Urban",variable=area,value="Rural")
Rural.grid(row=12,column=1)
SemiUrban=Radiobutton(window,text="Semi-urban",variable=area,value="SemiUrban")
SemiUrban.grid(row=12,column=2)
Urban=Radiobutton(window,text="Rural",variable=area,value="Urban")
Urban.grid(row=12,column=3)

def click() :
    d1 = Loan_ID.get()
    d2 = gender.get()
    d3 = married.get()
    d4 = depender.get()
    d5 = graduate.get()
    d6 = employed.get()
    d7 = ApplicantIncome.get()
    d8 = CoapplicantIncome.get()
    d9 = LoanAmount.get()
    d10 = Loan_Amount_Term.get()
    d11 = credit_history.get()
    d12 = area.get()
    import csv
    with open('loan.csv','w',newline='') as f :
        dataentry=csv.writer(f,delimiter=",")
        dataentry.writerow(('Loan_ID','Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'))
        dataentry.writerow((d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12))

    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier

    trainData = pd.read_csv('LoanData.csv')

    trainData.loc[trainData['Gender'] == 'Male', 'Gender'] = 1
    trainData.loc[trainData['Gender'] == 'Female', 'Gender'] = 0

    trainData.loc[trainData['Education'] == 'Graduate', 'Education'] = 1
    trainData.loc[trainData['Education'] == 'Not Graduate', 'Education'] = 0

    trainData.loc[trainData['Married'] == 'Yes', 'Married'] = 1
    trainData.loc[trainData['Married'] == 'No', 'Married'] = 0

    trainData.loc[trainData['Self_Employed'] == 'Yes', 'Self_Employed'] = 1
    trainData.loc[trainData['Self_Employed'] == 'No', 'Self_Employed'] = 0

    trainData.loc[trainData['Property_Area'] == 'Rural', 'Property_Area'] = 0
    trainData.loc[trainData['Property_Area'] == 'Semiurban', 'Property_Area'] = 1
    trainData.loc[trainData['Property_Area'] == 'Urban', 'Property_Area'] = 2

    trainData.loc[trainData['Loan_Status'] == 'Y', 'Loan_Status'] = 1
    trainData.loc[trainData['Loan_Status'] == 'N', 'Loan_Status'] = 0

    X = trainData.iloc[:,1:12]
    y = trainData.iloc[:,-1]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

    predict = pd.read_csv('loan.csv')

    if predict['Gender'] is 'Male':
        predict['Gender'] = 1
    else:
        predict['Gender'] = 0

    if predict['Education'] is 'Graduate':
        predict['Education'] = 1
    else:
        predict['Education'] = 0

    if predict['Married'] is 'Yes':
        predict['Married'] = 1
    else:
        predict['Married'] = 0

    if predict['Self_Employed'] is 'Yes':
        predict['Self_Employed'] = 1
    else:
        predict['Self_Employed'] = 0

    if predict['Property_Area'] is 'Rural':
        predict['Property_Area'] = 0
    elif predict['Property_Area'] is 'Semiurban':
        predict['Property_Area'] = 1
    else:
        predict['Property_Area'] = 2

    X_predict = predict.iloc[:,1:12]

    randForest = RandomForestClassifier(n_estimators=25, min_samples_split=25, max_depth=7, max_features=1)
    randForest.fit(X_train, y_train)
    y_result = randForest.predict(X_predict)

    Label(window,text="Loan Status", bg="black",fg="white",width=15,font="none 12 bold").grid(row=13, column=0, sticky=W)
    output=Text(window, width=20, height=3, wrap=WORD, background="grey")
    output.grid(row=13, column=1, sticky=W)
    if y_result == 1:
        y_result = "Yes"
    else:
        y_result = "No"
    output.insert(END, y_result)


Button(window, text="Submit", width=6, command=click).grid(row=14,column=1,sticky=E)
window.mainloop()
