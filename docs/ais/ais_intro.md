# Introduction

The Automatic Identification System was originally developed by the International Maritime 
Organization in 2004 to prevent collisions between large vessels. This system requires all 
commercial ships (gross tonnage greater than 300) and passenger ships to broadcast their 
position and other characteristics via ground stations and satellites. The resulting data 
is highly complex as it includes dynamic information on ship movements (position and speed), 
and static information on ship characteristics and voyage-related attributes.

Although AIS was originally developed to maintain safety at sea, recent work by 
[IMF researchers](https://blogs.worldbank.org/opendata/using-marine-spatial-data-inform-development-work-and-public-policies) 
has highlighted its potential to nowcast economic statistics, with a particular focus on trade. 
Most relevantly, [Arslanalp, Koepke and Verschuur (2019)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4026426) 
conducted a study to track daily merchandise trade at the port-level in the Pacific Islands.

This branch of work will build on these initiatives by adapting and improving on the methodologies 
to derive high-frequency maritime statistics for the Pacific Island Countries (PICs).

## AIS Density Map

The maps show the density of AIS messages collected within the Exclusive Economic Zone of each PIC (blue line).
The white circles point to port locations. To view the density maps, choose the layer 
(cargo, tankers, passengers, fishing, and others) from the upper-right button of the map. 

````{tab-set}
``` {tab-item} Federated States of Micronesia
<div id= "content">
<iframe src="../interactive/ais/heatmap/Micronesia2023.html" name="Micronesia" id="Micronesia" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
``` 
``` {tab-item} Fiji 
<div id= "content">
<iframe src="../interactive/ais/heatmap/Fiji2023.html" name="Fiji" id="Fiji" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
``` 
```{tab-item} Kiribati
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Kiribati2023.html" name="Kiribati" id="Kiribati" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Marshall Islands
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Marshall Islands2023.html" name="Marshall" id="Marshall" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Nauru
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Nauru2023.html" name="Nauru" id="Nauru" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Palau
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Palau2023.html" name="Palau" id="Palau" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Papua New Guinea
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Papua New Guinea2023.html" name="Palau" id="Papua New Guinea" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Samoa
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Samoa2023.html" name="Samoa" id="Samoa" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Solomon Islands
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Solomon Islands2023.html" name="Solomon" id="Solomon" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Tonga
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Tonga2023.html "name="Tonga" id="Tonga" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Tuvalu
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Tuvalu2023.html" name="Tuvalu" id="Tuvalu" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Vanuatu
<div id= "content">
    <iframe src="../interactive/ais/heatmap/Vanuatu2023.html" name="Vanuatu" id="Vanuatu" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
````
Sources: 
AIS data from [UN Global Platform](https://www.officialstatistics.org/); 
EEZ geojson file from [Pacific Data hub](https://pacificdata.org/data/dataset/pacific-island-countries-and-territories-exclusive-economic-zones);
port locations from IMF. 

## Additional Resources

- [AIS Handbook, Global Working Group on Big Data for Official Statistics](https://unstats.un.org/wiki/display/AIS/Introduction)
    > Data for this analysis is available through the UN Global Platform, which also
    hosts a dedicated working group to promote the use of AIS data to derive economic
    indicators.
