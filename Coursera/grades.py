score = input("Enter Score: ")
sc=float(score)
if sc>= 0.9 and sc<=1.0:
    grade='A'
elif sc>=0.8 and sc<9.0:
    grade='B'
elif sc>=0.7 and sc<8.0:
    grade='C'   
elif sc>=0.6 and sc<7.0:
    grade='D'
elif sc<0.6:
    grade = 'F'
elif sc>1.0 and sc<0.0:
    print (" Error Found ")
print(grade)