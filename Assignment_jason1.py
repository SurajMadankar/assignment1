# import json
# f=open('empl2.json')
# data=json.load(f)
# for i in data["Employees"]:
#     print(i)
# f.close()
#"C:\Users\ravi\OneDrive\Desktop\DATASCIENCE\PYTHON\empl2.json"

#_____________________________________________________________________________________________________________________________----

import json
state= {
    "Haryana":"(Chandigarh)",
    "Himachal Pradesh":"(Shimla)",
    "Jharkhand":"(Ranchi):",
    "Karnataka":"(Bangalore)",
    "Kerala":"(Thiruvananthapuram)",
    "Madhya Pradesh":"(Bhopal)",
    "Maharashtra":"(Mumbai)"
}
data=json.dumps(state,indent=4)
print(data)





