# Alberta_well_locator

## Project Description
The Alberta Well Locator Program is a data visualisation tool that allows the user to interact with BitCan’s directory of well sites. Given any input Unique Well Identifier (UWI), the web app maps the point of interest, calculates the distance between the input UWI and all existing well sites, and displays rock lithology, in-situ, and mechanical properties associated with each well.\

**Tools Used:** Flask, Folium, Python (Pandas, NumPy), SQLite

## The Map
The input UWI is displayed as a blue marker and a circle with a radius representing 50 km on the map. Each green marker represents a well location from the database, the name is displayed when the user hovers over it.

<img width="1435" alt="Screen Shot 2022-10-08 at 1 00 39 PM" src="https://user-images.githubusercontent.com/105069660/194726200-ab1a18fe-36db-47f8-ae84-11f874604b73.png">

## Map Features
![Screen Shot 2022-10-08 at 1 12 34 PM](https://user-images.githubusercontent.com/105069660/194726245-01260241-30ec-4fc1-bf81-6f839bb6b15c.png)

Upon clicking on a well marker, a scrollable popup table will be displayed:
<img width="1433" alt="Screen Shot 2022-10-08 at 1 01 49 PM" src="https://user-images.githubusercontent.com/105069660/194726265-6906146b-afab-4adc-84bf-6a80dc9e4a5b.png">

| First Header  | Second Header |
| ------------- | ------------- |
| Distance | Distance between searched UWI and the well, measured in kilometers.|
| Depth  | Content Cell  |
| Rock Lithology  | Content Cell  |
| In-Situ  | Content Cell  |
| Mechanical Properties  | Content Cell  |
