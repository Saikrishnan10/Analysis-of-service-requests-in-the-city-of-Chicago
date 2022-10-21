#!/usr/bin/env python
# coding: utf-8

# In[400]:


#Getting structure files after performing data cleaning and transformation process (Saikrishnan)
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns

Structured_file_1 = pd.read_csv("C:/Users/mural/Downloads/TreeTrim.csv")
Structured_file_2 = pd.read_csv("C:/Users/mural/Downloads/Rodent.csv")
Structured_file_3 = pd.read_csv("C:/Users/mural/Downloads/Garbage.csv")
Structured_file_4 = pd.read_csv("C:/Users/mural/Downloads/Potholes.csv")


# In[401]:


#Analysing the similarity in all the 4 datasets
print(Structured_file_1.columns)
print(Structured_file_2.columns)
print(Structured_file_3.columns)
print(Structured_file_4.columns)


# In[ ]:


#We have merged the files using concat


# In[402]:


#Merging the files
concat_values = pd.concat([Structured_file_1,Structured_file_2,Structured_file_3,Structured_file_4],axis=1)
concat_values


# In[403]:


#Removing NA values
middle_value = concat_values.drop(["Unnamed: 0"],axis=1)
full_value = middle_value.dropna(axis=0)
full_value


# In[ ]:


#Grouping the files based on the status columns


# In[404]:


Status_Open = full_value[full_value['T_Status'].isin(['Open', 'Open - Dup'])& full_value['P_Status'].isin(['Open', 'Open - Dup'])
& full_value['R_Status'].isin(['Open', 'Open - Dup']) & full_value['G_Status'].isin(['Open', 'Open - Dup'])]


# In[405]:


Status_completed = full_value[full_value['T_Status'].isin(['Completed', 'Completed - Dup'])& full_value['P_Status'].isin(['Completed', 'Completed - Dup'])
& full_value['R_Status'].isin(['Completed', 'Completed - Dup']) & full_value['G_Status'].isin(['Completed', 'Completed - Dup'])]


# In[406]:


#Status as Open
Status_Open_Tree = full_value[full_value['T_Status'].isin(['Open', 'Open - Dup'])]
Status_Open_Garbage = full_value[full_value['G_Status'].isin(['Open', 'Open - Dup'])]
Status_Open_Roden = full_value[full_value['R_Status'].isin(['Open', 'Open - Dup'])]
Status_Open_Potholes = full_value[full_value['P_Status'].isin(['Open', 'Open - Dup'])]
Status_Open

#Status as Completed
Status_completed_Tree = full_value[full_value['T_Status'].isin(['Completed', 'Completed - Dup'])]
Status_completed_Garbage = full_value[full_value['G_Status'].isin(['Completed', 'Completed - Dup'])]
Status_completed_Roden = full_value[full_value['R_Status'].isin(['Completed', 'Completed - Dup'])]
Status_completed_Potholes = full_value[full_value['P_Status'].isin(['Completed', 'Completed - Dup'])]
Status_completed


#Tree Location Split
Status_Open_Tree['T_Tree Location'].value_counts()
Status_completed_Tree['T_Tree Location'].value_counts()

#Garbage split
Status_Open_Garbage['G_number_of_black_carts_delivered'].value_counts()
Status_completed_Garbage['G_number_of_black_carts_delivered'].value_counts()

#Rodent split
Status_Open_Roden['R_No_of_premises_baited'].value_counts()
Status_Open_Roden['R_No_of_premises_withgarbage'].value_counts()
Status_Open_Roden['R_No_of_premises_withrats'].value_counts()

Status_completed_Roden['R_No_of_premises_baited'].value_counts()
Status_completed_Roden['R_No_of_premises_withgarbage'].value_counts()
Status_completed_Roden['R_No_of_premises_withrats'].value_counts()

#Potholes split
Status_Open_Potholes['P_No_of_potholes_filled_on_block'].value_counts()
Status_completed_Potholes['P_No_of_potholes_filled_on_block'].value_counts()


# In[407]:


#Finding the open and completed case count for each department

Departments = ['Tree Trim - Open','Tree Trim - Completed','Garbage Cart Black Maintenance/Replacement - Open',
           'Garbage Cart Black Maintenance/Replacement - Completed','Rodent Baiting/Rat Complaint - open',
           'Rodent Baiting/Rat Complaint - closed','Pothole in Street - Open','Pothole in Street - Closed']
Status = [len(Status_Open_Tree),len(Status_completed_Tree),len(Status_Open_Garbage),len(Status_completed_Garbage),
            len(Status_Open_Roden),len(Status_completed_Roden),len(Status_Open_Potholes),len(Status_completed_Potholes)]

plt.barh(Departments,Status)
plt.title('Open and Completed status')
plt.ylabel('Sanitation Departments')
plt.xlabel('Status')
plt.show()

(Departments,Status)


# In[408]:


#Tree Trim Department

#Tree Location - open
Tree_location_open = Status_Open_Tree[['T_Tree Location','T_Latitude','T_Longitude']]
Tree_location_open_Parkway = Tree_location_open[Tree_location_open['T_Tree Location']=='Parkway']
Tree_location_open_unknown = Tree_location_open[Tree_location_open['T_Tree Location']=='Location Not Recorded']
Tree_location_open_Alley = Tree_location_open[Tree_location_open['T_Tree Location']=='Alley']
Tree_location_open_vacant = Tree_location_open[Tree_location_open['T_Tree Location']=='Vacant Lot']
Tree_location_open.columns

#Tree Location - Close
Tree_location_completed = Status_completed_Tree[['T_Tree Location','T_Latitude','T_Longitude']]
Tree_location_completed_Parkway = Tree_location_completed[Tree_location_completed['T_Tree Location']=='Parkway']
Tree_location_completed_unknown = Tree_location_completed[Tree_location_completed['T_Tree Location']=='Location Not Recorded']
Tree_location_completed_Alley = Tree_location_completed[Tree_location_completed['T_Tree Location']=='Alley']
Tree_location_completed_vacant = Tree_location_completed[Tree_location_completed['T_Tree Location']=='Vacant Lot']
Tree_location_completed.columns


# In[425]:


#Using folium library for visualization (Plots done via folium library are mentioned in report in the form of screenshots)
#Reference for the plots  - https://alysivji.github.io/getting-started-with-folium.html

import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

#Tree location for open
chicago_tree_open = folium.Map([41.8781, -87.6298], zoom_start=10)
for index, row in Tree_location_open_Parkway.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                        radius=5,popup=row['T_Tree Location'],
                        fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_tree_open)
for index, row in Tree_location_open_unknown.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                    radius=5,color = 'white',popup=row['T_Tree Location'],
                    fill_color="black",fill_opacity=10,opacity=10).add_to(chicago_tree_open)
    
for index, row in Tree_location_open_Alley.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                    radius=5,popup=row['T_Tree Location'],
                        fill_color ="pink",color = 'grey',fill_opacity=10,opacity=10).add_to(chicago_tree_open)
for index, row in Tree_location_open_vacant.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                    radius=5,popup=row['T_Tree Location'],
                    fill_color="green",color = 'yellow',
                        fill_opacity=10,opacity=10).add_to(chicago_tree_open)
print('For Open Tree Trims')
print('parkway - red and blue'', Location unknown - black and white'', Alley - pink and grey'' , Vacant - green and yellow')
chicago_tree_open


# In[426]:


#Tree location for close
chicago_tree_completed = folium.Map([41.8781, -87.6298], zoom_start=10)
for index, row in Tree_location_completed_Parkway.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                        radius=5,popup=row['T_Tree Location'],
                        fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_tree_completed)
for index, row in Tree_location_completed_unknown.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                    radius=5,color = 'white',popup=row['T_Tree Location'],
                    fill_color="black",fill_opacity=10,opacity=10).add_to(chicago_tree_completed)
    
for index, row in Tree_location_completed_Alley.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                    radius=5,popup=row['T_Tree Location'],
                        fill_color ="pink",color = 'grey',fill_opacity=10,opacity=10).add_to(chicago_tree_completed)
for index, row in Tree_location_completed_vacant.iterrows():
    folium.CircleMarker([row['T_Latitude'], row['T_Longitude']],
                    radius=5,popup=row['T_Tree Location'],
                    fill_color="green",color = 'yellow',
                        fill_opacity=10,opacity=10).add_to(chicago_tree_completed)

print('For Closed Tree Trims')
print('parkway - red and blue'', Location unknown - black and white'', Alley - pink and grey'' , Vacant - green and yellow')

chicago_tree_completed


# In[411]:


#GARBAGE Department

#Garbage - open
Open_Garbage = Status_Open_Garbage[['G_number_of_black_carts_delivered','G_Latitude','G_Longitude']]
Open_Garbage_zero = Open_Garbage[Open_Garbage['G_number_of_black_carts_delivered']== 0]
Open_Garbage_nonzero = Open_Garbage[Open_Garbage['G_number_of_black_carts_delivered'] !=0]

#Garbage - completed
completed_Garbage = Status_completed_Garbage[["G_number_of_black_carts_delivered","G_Latitude","G_Longitude"]]
completed_Garbage_zero = completed_Garbage[completed_Garbage['G_number_of_black_carts_delivered']==0]
completed_Garbage_nonzero = completed_Garbage[completed_Garbage['G_number_of_black_carts_delivered']!=0]


# In[428]:


#Garbage - Open - all are zero which means
chicago_garbage_open = folium.Map([41.8781, -87.6298], zoom_start=10)
for index, row in Open_Garbage_zero.iterrows():
    folium.CircleMarker([row['G_Latitude'], row['G_Longitude']],popup=row['G_number_of_black_carts_delivered'],
                        radius=5,fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_garbage_open)
for index, row in Open_Garbage_nonzero.iterrows():
    folium.CircleMarker([row['G_Latitude'], row['G_Longitude']],popup=row['G_number_of_black_carts_delivered'],
                        radius=5,fill_color="black",color = 'white', fill_opacity=10,opacity=10).add_to(chicago_garbage_open)


print('Open Garbage with zero cart - red and blue, Open Garbage with more than zero carts - black and white (None)')
chicago_garbage_open


# In[433]:


#Garbage - Closed

chicago_garbage_closed = folium.Map([41.8781, -87.6298], zoom_start=10)
for index, row in completed_Garbage_zero.iterrows():
    folium.CircleMarker([row['G_Latitude'], row['G_Longitude']],popup=row['G_number_of_black_carts_delivered'],
                        radius=5,fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_garbage_closed)
for index, row in completed_Garbage_nonzero.iterrows():
    folium.CircleMarker([row['G_Latitude'], row['G_Longitude']],popup=row['G_number_of_black_carts_delivered'],
                        radius=5,fill_color="black",color = 'white', fill_opacity=10,opacity=10).add_to(chicago_garbage_closed)

print('Completed Garbage with zero cart - red and blue , Completed Garbage with more than zero carts - black and white')
chicago_garbage_closed


# In[415]:


#Rodent Control Department

#Rodent Control - open
Rodent_open_bait = Status_Open_Roden[["R_No_of_premises_baited","R_Latitude","R_Longitude"]]
Rodent_open_garbage = Status_Open_Roden[["R_No_of_premises_withgarbage","R_Latitude","R_Longitude"]]
Rodent_open_rats = Status_Open_Roden[["R_No_of_premises_withrats","R_Latitude","R_Longitude"]]


#Rodent Control - completed
Rodent_completed_bait = Status_completed_Roden[["R_No_of_premises_baited","R_Latitude","R_Longitude"]]
Rodent_completed_garbage = Status_completed_Roden[["R_No_of_premises_withgarbage","R_Latitude","R_Longitude"]]
Rodent_completed_rats = Status_completed_Roden[["R_No_of_premises_withrats","R_Latitude","R_Longitude"]]


#Zero and Non Zero - Both

#BAIT ZERO & NON ZERO
Rodent_open_bait_zero = Rodent_open_bait[Rodent_open_bait['R_No_of_premises_baited']==0]
Rodent_open_bait_nonzero = Rodent_open_bait[Rodent_open_bait['R_No_of_premises_baited'] !=0]

#Rodent GARBAGE ZERO & NON ZERO
Rodent_open_GARBAGE_zero = Rodent_open_garbage[Rodent_open_garbage['R_No_of_premises_withgarbage']==0]
Rodent_open_GARBAGE_nonzero = Rodent_open_garbage[Rodent_open_garbage['R_No_of_premises_withgarbage']!=0]

#Rodent GARBAGE ZERO & NON ZERO
Rodent_open_rats_zero = Rodent_open_rats[Rodent_open_rats['R_No_of_premises_withrats']==0]
Rodent_open_rats_nonzero = Rodent_open_rats[Rodent_open_rats['R_No_of_premises_withrats']!=0]



#Rodent Control - open
#BAIT ZERO & NON ZERO
Rodent_open_bait_zero = Rodent_completed_bait[Rodent_completed_bait['R_No_of_premises_baited']==0]
Rodent_open_bait_nonzero = Rodent_completed_bait[Rodent_completed_bait['R_No_of_premises_baited']!=0]

#Rodent GARBAGE ZERO & NON ZERO
Rodent_open_GARBAGE_zero = Rodent_open_garbage[Rodent_open_garbage['R_No_of_premises_withgarbage']==0]
Rodent_completed_GARBAGE_nonzero = Rodent_open_garbage[Rodent_open_garbage['R_No_of_premises_withgarbage']!=0]

#Rodent GARBAGE ZERO & NON ZERO
Rodent_completed_rats_zero = Rodent_completed_rats[Rodent_completed_rats['R_No_of_premises_withrats']==0]
Rodent_completed_rats_nonzero = Rodent_completed_rats[Rodent_completed_rats['R_No_of_premises_withrats']!=0]



#Rodent Control - completed
#BAIT ZERO & NON ZERO
Rodent_completed_bait_zero = Rodent_completed_bait[Rodent_completed_bait['R_No_of_premises_baited']==0]
Rodent_completed_bait_nonzero = Rodent_completed_bait[Rodent_completed_bait['R_No_of_premises_baited']!=0]

#Rodent GARBAGE ZERO & NON ZERO
Rodent_completed_GARBAGE_zero = Rodent_completed_garbage[Rodent_completed_garbage['R_No_of_premises_withgarbage']==0]
Rodent_completed_GARBAGE_nonzero = Rodent_completed_garbage[Rodent_completed_garbage['R_No_of_premises_withgarbage']!=0]

#Rodent GARBAGE ZERO & NON ZERO
Rodent_completed_rats_zero = Rodent_completed_rats[Rodent_completed_rats['R_No_of_premises_withrats']==0]
Rodent_completed_rats_nonzero = Rodent_completed_rats[Rodent_completed_rats['R_No_of_premises_withrats']!=0]
Rodent_completed_rats_nonzero


# In[427]:


#chicago_rodent - Completed
chicago_rodent_Completed = folium.Map([41.8781, -87.6298], zoom_start=10)

for index, row in Rodent_completed_rats_zero.iterrows():
    folium.CircleMarker([row['R_Latitude'], row['R_Longitude']],popup=row['R_No_of_premises_withrats'],
                        radius=5,fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_rodent_Completed)

for index, row in Rodent_completed_rats_nonzero.iterrows():
    folium.CircleMarker([row['R_Latitude'], row['R_Longitude']],popup=row['R_No_of_premises_withrats'],
                        radius=5,fill_color="black",color = 'white', fill_opacity=10,opacity=10).add_to(chicago_rodent_Completed)

print('Completed Rodent baiting with zero rats - red and blue , Completed Rodent baiting  with more than zero Rats - black and white')
chicago_rodent_Completed


# In[429]:


#chicago_rodent - Open

chicago_rodent_open = folium.Map([41.8781, -87.6298], zoom_start=10)

for index, row in Rodent_open_rats_zero.iterrows():
    folium.CircleMarker([row['R_Latitude'], row['R_Longitude']],popup=row['R_No_of_premises_withrats'],
                        radius=5,fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_rodent_open)
    
for index, row in Rodent_open_rats_nonzero.iterrows():
    folium.CircleMarker([row['R_Latitude'], row['R_Longitude']],popup=row['R_No_of_premises_withrats'],
                        radius=5,fill_color="black",color = 'white', fill_opacity=10,opacity=10).add_to(chicago_rodent_open)

print('Open Rodent baiting with no action - red and blue , Open Rodent baiting  with action initiated - black and white (None)')

chicago_rodent_open


# In[430]:


#POTHOLES Department

#Potholes split
Status_Open_Potholes['P_No_of_potholes_filled_on_block'].value_counts()
Status_completed_Potholes['P_No_of_potholes_filled_on_block'].value_counts()


#Potholes - open
potholes_open = Status_Open_Potholes[['P_No_of_potholes_filled_on_block','P_Latitude','P_Longitude']]

#Potholes - closed

potholes_completed = Status_completed_Potholes[['P_No_of_potholes_filled_on_block','P_Latitude','P_Longitude']]


#Potholes Department

#Pothole - open
potholes_open_zero = potholes_open[potholes_open['P_No_of_potholes_filled_on_block']== 0]
potholes_open_nonzero = potholes_open[potholes_open['P_No_of_potholes_filled_on_block'] !=0]

#Potholes - completed
potholes_completed_zero = potholes_completed[potholes_completed['P_No_of_potholes_filled_on_block']==0]
potholes_completed_nonzero = potholes_completed[potholes_completed['P_No_of_potholes_filled_on_block']!=0]


# In[431]:


#Pothole - Open - all are zero which means
chicago_pothole_open = folium.Map([41.8781, -87.6298], zoom_start=10)
for index, row in potholes_open_zero.iterrows():
    folium.CircleMarker([row['P_Latitude'], row['P_Longitude']],popup=row['P_No_of_potholes_filled_on_block'],
                        radius=5,fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_pothole_open)
for index, row in potholes_open_nonzero.iterrows():
    folium.CircleMarker([row['P_Latitude'], row['P_Longitude']],popup=row['P_No_of_potholes_filled_on_block'],
                        radius=5,fill_color="black",color = 'white', fill_opacity=10,opacity=10).add_to(chicago_pothole_open)
    
print('Open Potholes with no action taken - red and blue , Open Potholes with action initiated - black and white')
chicago_pothole_open


# In[432]:


#Pothole - Closed

chicago_pothole_closed = folium.Map([41.8781, -87.6298], zoom_start=10)
for index, row in potholes_completed_zero.iterrows():
    folium.CircleMarker([row['P_Latitude'], row['P_Longitude']],popup=row['P_No_of_potholes_filled_on_block'],
                        radius=5,fill_color="red",color = 'blue', fill_opacity=10,opacity=10).add_to(chicago_pothole_closed)
for index, row in potholes_completed_nonzero.iterrows():
    folium.CircleMarker([row['P_Latitude'], row['P_Longitude']],popup=row['P_No_of_potholes_filled_on_block'],
                        radius=5,fill_color="black",color = 'white', fill_opacity=10,opacity=10).add_to(chicago_pothole_closed)

print('Completed Potholes with no need for filling potholes - red and blue , Completed Potholes with need for filling potholes - black and white')
chicago_pothole_closed


# In[422]:


# Future works based on police district , community area and ward

tree_codes_open = Status_completed_Tree[["T_Status","T_Ward","T_Police_District","T_Community_Area"]]
tree_codes_completed = Status_completed_Tree[["T_Ward","T_Police_District","T_Community_Area"]]
garbage_wards_open = Status_Open_Garbage[["G_Ward","G_Police_District","G_Community_Area"]]
garbage_wards_completed = Status_completed_Garbage[["G_Ward","G_Police_District","G_Community_Area"]]
rodent_wards_open = Status_Open_Roden[["R_ Ward","R_Police_District","R_Community_Area"]]
rodent_wards_completed = Status_completed_Roden[["R_ Ward","R_Police_District","R_Community_Area"]]
pothole_wards_open = Status_Open_Potholes[["P_ Ward","P_Police_District","P_Community_Area"]]
pothole_wards_completed = Status_completed_Potholes[["P_ Ward","P_Police_District","P_Community_Area"]]


# In[369]:


#Plotting of Graphs based on the above mentioned data which has the details of all the zones and their respective case counts

fig, axes = plt.subplots(1,1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of open Rodent complaints across Wards,Police districts and Community area')
sns.histplot([rodent_wards_open['R_ Ward'],rodent_wards_open['R_Police_District'],rodent_wards_open['R_Community_Area']],bins = range(0,80))
fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of Completed Rodent complaints across Wards,Police districts and Community area')
sns.histplot([rodent_wards_completed['R_ Ward'],rodent_wards_completed['R_Police_District'],rodent_wards_completed['R_Community_Area']],bins = range(0,80))
fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of Open Pothole complaints across Wards,Police districts and Community area')
a3 = sns.histplot([pothole_wards_open['P_ Ward'],pothole_wards_open['P_Police_District'],pothole_wards_open['P_Community_Area']],bins = range(0,80))
fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of Completed Pothole complaints across Wards,Police districts and Community area')
a4 = sns.histplot([pothole_wards_completed['P_ Ward'],pothole_wards_completed['P_Police_District'],pothole_wards_completed['P_Community_Area']],bins = range(0,80))
fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of Open Tree trim complaints across Wards,Police districts and Community area')
a5 = sns.histplot([tree_codes_open['T_Ward'],tree_codes_open['T_Police_District'],tree_codes_open['T_Community_Area']],bins = range(0,80))
fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of Completed Tree trim complaints across Wards,Police districts and Community area')
a6 = sns.histplot([tree_codes_completed['T_Ward'],tree_codes_completed['T_Police_District'],tree_codes_completed['T_Community_Area']],bins = range(0,80))
fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of Open Garbage Maintenance/Replacement complaints across Wards,Police districts and Community area')
a7 = sns.histplot([garbage_wards_open['G_Ward'],garbage_wards_open['G_Police_District'],garbage_wards_open['G_Community_Area']],bins = range(0,80))
fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)
fig.suptitle('Number of Completed Garbage Maintenance/Replacement complaints across Wards,Police districts and Community area')
a8 = sns.histplot([garbage_wards_completed['G_Ward'],garbage_wards_completed['G_Police_District'],garbage_wards_completed['G_Community_Area']],bins = range(0,80))

