# Alberta_well_locator

#Project Description
The Alberta Well Locator Program is a data visualisation tool that allows the user to interact with BitCan’s directory of well sites. Given any input Unique Well Identifier (UWI), the web app maps the point of interest, calculates the distance between the input UWI and all existing well sites, and displays rock lithology, in-situ, and mechanical properties associated with each well.![image](https://user-images.githubusercontent.com/105069660/194726172-c6abaf73-5bba-49d2-b6bd-d2d139cc2cf2.png)

Tools Used: Flask, Folium, Python (Pandas, NumPy), SQLite

#The Map
The input UWI is displayed as a blue marker and a circle with a radius representing 50 km on the map. Each green marker represents a well location from the database, the name is displayed when the user hovers over it.![image](https://user-images.githubusercontent.com/105069660/194726194-3857d8b3-6624-4a95-a26f-0a44c23739a8.png)

<img width="1435" alt="Screen Shot 2022-10-08 at 1 00 39 PM" src="https://user-images.githubusercontent.com/105069660/194726200-ab1a18fe-36db-47f8-ae84-11f874604b73.png">
