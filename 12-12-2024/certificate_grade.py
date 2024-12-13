project,internal,external=map(int,input("Enter Project,Internal,External score:").split())
# if project < 50:
#     if internal < 50:
#         if external < 50:
#             print("Failed in project",project,"score and internal",internal,"score and external",external,"score")
#         else:
#             print("Failed in project", project, "score and internal", internal, "score")
#     else:
#         if external < 50:
#             print("Failed in project",project,"score and external",external,"score")
#         else:
#             print("Failed in project", project, "score")
# else:
#     if internal < 50:
#         if external < 50:
#             print("Failed in internal",internal,"score and external",external,"score")
#         else:
#             print("Failed in internal", internal, "score")
#     else:
#         if external < 50:
#             print("Failed in external", external, "score")
#         else:
#             total_marks = project * 0.70 + internal * 0.10 + external * 0.20
#             if total_marks >= 90:
#                 print('A grade')
#             elif total_marks > 80:
#                 print('B grade')
#             else:
#                 print('C grade')

if project>=50 and internal>=50 and external>=50:
    total_marks = project * 0.70 + internal * 0.10 + external * 0.20
    if total_marks >= 90:
        print('A grade')
    elif total_marks > 80:
        print('B grade')
    else:
        print('C grade')
else:
    if project<50:
        print('Failed in project and score is :',project)
    if external<50:
        print('Failed in external and score is :',external)
    if internal<50:
        print('Failed in internal and score is :',internal)
