import pandas as pd
import json
from pydantic import BaseModel, Field
from typing import List

file = "/home/onedata/Downloads/empy/detailed-03-07-2023-03-07-2023.csv"
data = pd.read_csv(file)

class Project(BaseModel):
    name: str
    user_name: str
    spent_time: int

class Projects(BaseModel):
    projects:List[Project]

data_json = data.to_json(index=False,orient="split")
data_json =json.loads(data_json)


all_data=list()
for data in data_json['data']:
    name,username,spentime=data

    new2={
        "name":name,
        "user_name":username,
        "spent_time":spentime
    }

    new=Project(**new2)
    all_data.append(new)

final=Projects(projects=all_data)


p_input = "o"

for project in final.projects:
    if p_input.lower() in project.name.lower():
        print(project)


# df=data

# new=df[df["Project Name"].str.lower().str.contains("one")]
# print(new)

