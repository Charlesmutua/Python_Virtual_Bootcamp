math = int(input("Enter marks for Maths"))
eng = int(input("Enter marks for English"))
kisw = int(input("Enter marks for KIswahili"))
sci = int(input("Enter marks for Science"))
sst = int(input("Enter marks for Social Studies"))



total_marks = math+eng+kisw+sci+sst
average_score = total_marks/5

if  average_score> 80 and average_score <100:
    print("Grade A")
elif 74<average_score<80:
    print("Grade A-")
elif 69<average_score<75:
    print("Grade B+")
elif 64<average_score<70:
    print("Grade B-")
elif 59<average_score <65:
    print("Grade C+")
    pass
    

print(average_score)
    