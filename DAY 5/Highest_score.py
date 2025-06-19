stud_score=[150,242,521,523,211,421,124,244,214,552,123,512]
# a=0
# for score in stud_score:
#     a+=score

# print(f"the total marks obtained are {a}")

#To find maximumscore 
max=0
for score in stud_score:
    if score>max:
        max=score

print("MAX Score is",max)
