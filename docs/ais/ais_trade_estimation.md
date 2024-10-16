# Maritime Trade
There is growing research on the use of Automatic Identification System (AIS) data as alternative source 
for port and seaborne trade statistics. In recent years, the UK and US statistical agencies started publishing 
AIS-derived maritime statistics as part of their [real-time faster economic 
indicators for UK](https://datasciencecampus.ons.gov.uk/projects/faster-indicators-of-uk-economic-activity-improving-the-shipping-indicators/), 
and [Covid-19 related transport statistics for US](https://www.bts.gov/freight-indicators#anchored-offshore). 
For pacific island economies where official data is not 
readily available, AIS data shows great potential to fill the gaps on  seaborne trade activities.

The steps for capturing seaborne trade activities involves identifying port calls from AIS data. The next section 
summarizes related literature for these steps.

| study | Output                                | Coverage                         |Methods|
|-------|---------------------------------------|----------------------------------|---|
| 1, 2  | port boundary, port calls, cargo load | Global, vessels related to trade | asd|

In here, we validate the use of AIS data to produce official port statistics 
for pacific island economies, with Samoa as use case for its admin data availability (5).
Our main data sources are the UN Global Platform (UNGP) for AIS and Ship Registry (6),
and global port boundaries requested from the author of 
“Tracking trade from space: an application to pacific island countries“ (4). 
We used the helper functions from ais python package (7) with some refinements
to generate a port calls dataset. We follow two existing methodologies on cargo
volume estimation (4, 8, 9) to estimate the cargo carried by the vessel upon
arrival and departure. We find that our derived port calls data accurately capture
international trade-related ships, but cargo volume estimates are still far-off from 
official data.

## Data and Methods
Figure 1 presents the port calls methodology from the Samoa study. 
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
