## **Analysis-of-service-requests-in-the-city-of-Chicago**
Many cities maintain open data platforms for 311 calls, as part of a broader effort to increase transparency and good governance in local government. The objective of this project is to extract unstructured data from the government repository of Chicago and load the data into a non-relational database. The unstructured data from the government repository are the service requests procedures with respect to complaints recorded in each neighborhood. The complaint type is classified based on the areas and different profiles such as garbage, potholes rodent baiting, and tree trims. This data is cleaned and converted into structured data and fed into a relational database. The data is retrieved from the database, interpreted, and visualized to obtain insights that can help with the analysis.

### **This research has been conducted with the intent to find the solution for the following questions.**
1. What are the status of service requests in terms of Opened and completed? 
2. Which locations hold the highest amount of Opened and Completed service requests for the Garbage cart department?
3. Which locations hold the highest amount of Opened and Completed service requests for the potholes department?
4. Which locations hold the highest amount of Opened and Completed service requests for the Rodent Baiting department?
5. Which locations hold the highest amount of Opened and Completed service requests for the Tree Trim department?


### ***Dataset Description:***

The data for this study was taken from the city of Chicago's official government repository for 311 Service Requests (https://data.cityofchicago.org), which is open to the public. The data in the dataset was gathered and separated from multiple surveys conducted in various places:

### **Data Extraction:**

Four datasets from the data.cityofchicago.org repository for this analysis. Socrata Open Data API, also known as SODA API, is initially used to extract the data in JSON format. By installing soda-py package in Python unstructured data were extracted from government repositories using API keys. Four JSON files are created from the extracted data.


**Source for Tree Trim data API:**               
[https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Tree-Trims-Historical/uxic-zsuj](https://data.cityofchicago.org/resource/uxic-zsuj.json)

**Source for Rodent Baiting data API:**          
[https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Rodent-Baiting-Historical/97t6-zrhs](https://data.cityofchicago.org/resource/97t6-zrhs.json)

**Source for Garbage data API:**          
[https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Garbage-Carts-Historical/9ksk-na4q](https://data.cityofchicago.org/resource/9ksk-na4q.json)

**Source for Pot-Holes data API:**            
[https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Pot-Holes-Reported-Historical/7as2-ds3y](https://data.cityofchicago.org/resource/_311-potholes.json)

### **Storage of Unstructured data:**

 The Four JSON file containing the unstructured data is then parsed into the Mongo DB. The process of creating a new database and creating a new collection for loading the data was undertaken independently for every dataset. From this database, further data is obtained and converted to the individual CSV file
 
 ### **Storage of Structured data:**
 
Using the pandas package present in python, the four CSV datas were transformed into a data frame and was subjected to data cleaning process. After cleaning and transforming data, structured data were stored and saved individually in CSV format into a Relational database, a PostgreSQL DB. With the help of the psycopg2 package, a connection is made with the localhost. Then pandas data frames are created using the pandas.io.sql package in Python to extract the data from this table. The four structured data are available under the file names (Tree Trims Data, Rodent Infestation Data, Garbage Data and Potholes Data)

### **Data Visualization:**

All the four datasets were extracted from PostgreSQL in the form of Pandas data frame and then combined into one. The combined data frame was used for the visualization using python libraries such as Matplotlib Folium and several other libraries. The opened and closed service requests were analysed for each of the four datasets based on the location around Chicago. The results identified as the outcome of the project were the solutions of the above five questions.


