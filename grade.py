Grade = int(input("Marks scored: "))
#Subjective grading system
if Grade > 70:
    print("EXCELLENT!!  \n Grade: A ")
elif Grade > 60:
    print("GOOD!!  \n Grade: B  ")
elif Grade > 50: 
    print("SATISFACTORY!!  \n Grade: C ")
elif Grade> 40:
    print("BELOW AVERAGE!!  \n Grade: D ")
else:
    print("FAILED!!  \n  Grade: F ")
