# Port Calls
There is growing research on the use of Automatic Identification System (AIS) data as alternative source 
for port and seaborne trade statistics. In recent years, the UK and US statistical agencies started publishing 
AIS-derived maritime statistics as part of their real-time faster economic 
indicators for UK [[1]](#1) and Covid-19 related transport statistics for US [[2]](#2). 
For pacific island economies where official data is not 
readily available, AIS data shows great potential to fill the gaps on  
seaborne trade activities [[3]](#3)

## Data and Methods
Our main data sources are the UN Global Platform (UNGP) for AIS and Ship Registry [[4]](#4),
and global port boundaries requested from the author of 
“Tracking trade from space: an application to pacific island countries“[[3]](#3). 
We used the helper functions from ais python package [[5]](#5) with some refinements
to generate a port calls dataset. 

![Port Calls Methodology](../images/ais/pc_method.svg)

The figure above presents a general overview of the methodology to capture port calls.
The term “port buffer” refers to a large area encompassing the port, 
with a square boundary of  22 km from the port. AIS data within the port buffer are 
extracted and then aggregated into routes. A route comprises consecutive AIS messages 
transmitted by a vessel during a port visit. It summarizes essential information such 
as the vessel’s port arrival and departure time at the port, as well as the changes in 
its draught. From here, the vessels are verified  in the Ship Registry data to identify
routes undertaken by individual ships. The Ship Registry data provides additional
information about the ship’s characteristics that are not available in AIS 
but are necessary for trade estimation purposes. Following this, the next port
calls for each route are generated to update the departure draught information
and determine if the vessel is embarking on an international voyage. The port 
calls data consists of routes from vessels that meet two criteria: cargo-carrying
(excluding for passenger ships) according to the Ship Register and engaged in
international voyages according to their next port calls. 

## Port Calls
````{tab-set}
``` {tab-item} Federated States of Micronesia
<div id= "content">
<iframe src="../interactive/ais/port calls/Micronesia port calls.html" name="Micronesia" id="Micronesia" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
``` 
``` {tab-item} Fiji 
<div id= "content">
<iframe src="../interactive/ais/port calls/Fiji port calls.html" name="Fiji" id="Fiji" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
``` 
```{tab-item} Kiribati
<div id= "content">
    <iframe src="../interactive/ais/port calls/Kiribati port calls.html" name="Kiribati" id="Kiribati" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Marshall Islands
<div id= "content">
    <iframe src="../interactive/ais/port calls/Marshall Islands port calls.html" name="Marshall" id="Marshall" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Nauru
<div id= "content">
    <iframe src="../interactive/ais/port calls/Nauru port calls.html" name="Nauru" id="Nauru" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Palau
<div id= "content">
    <iframe src="../interactive/ais/port calls/Palau port calls.html" name="Palau" id="Palau" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Papua New Guinea
<div id= "content">
    <iframe src="../interactive/ais/port calls/Papua New Guinea port calls.html" name="Palau" id="Papua New Guinea" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Samoa
<div id= "content">
    <iframe src="../interactive/ais/port calls/Samoa port calls.html" name="Samoa" id="Samoa" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Solomon Islands
<div id= "content">
    <iframe src="../interactive/ais/port calls/Solomon Islands port calls.html" name="Solomon" id="Solomon" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Tonga
<div id= "content">
    <iframe src="../interactive/ais/port calls/Tonga port calls.html "name="Tonga" id="Tonga" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Tuvalu
<div id= "content">
    <iframe src="../interactive/ais/port calls/Tuvalu port calls.html" name="Tuvalu" id="Tuvalu" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
```{tab-item} Vanuatu
<div id= "content">
    <iframe src="../interactive/ais/port calls/Vanuatu port calls.html" name="Vanuatu" id="Vanuatu" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```
````
References:

<a id="1">[1]</a> Office for National Statistics (ONS). (2023, February). 
Economic activity and social change in the UK, real-time indicators. 
ONS website statistical bulletin.

<a id="2">[2]</a> Bureau of Transportation Statistics (BTS). (2023), 
Latest Supply Chain Indicators. BTS website. 

<a id="3">[3]</a> Arslanalp S., Koepke R., and Verschuur J.. Tracking trade from space: an application to pacific island countries. IMF Working Papers, 2021(225):A001, 2021. 
URL: https://www.elibrary.imf.org/view/journals/001/2021/225/article-A001-en.xml, 
doi:10.5089/9781513593531.001.A001.

<a id="4">[4]</a> UN Global Platform. https://www.officialstatistics.org/

<a id="5">[5]</a> AIS Task Team. (2022). AIS python package (Version 2.8.1) 
[Source Code]. https://code.officialstatistics.org/trade-task-team-phase-1/ais