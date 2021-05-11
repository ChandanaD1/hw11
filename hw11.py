# Data Analysis by Visualization

import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("hw11.csv")

group = df.groupby(["student_id", "level"], as_index = False)
mean = group["attempt"].mean()
#print(mean)

graph = px.scatter(mean, x = "student_id", y = "level", size = "attempt", color = "attempt")
graph.show()