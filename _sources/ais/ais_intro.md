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

This branch of work will build on these initiatives by adapting and improving methodologies to derive maritime statistics 
for the Pacific Island Countries (PICs).

## AIS Density Map

The map shows the  Exclusive Economic Zone of each PIC and their corresponding port locations.
Hover on the location to know the country or port name. 
The AIS density per vessel type (cargo, tankers, passengers, fishing, and others)
can be shown by choosing the corresponding layer from the upper-right button of the map. 

```
<div id= "content">
<iframe src="interactive/ais/Pacific Islands AIS Heatmap.html" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
</div>
```


## Additional Resources

- [AIS Handbook, Global Working Group on Big Data for Official Statistics](https://unstats.un.org/wiki/display/AIS/Introduction)
    > Data for this analysis is available through the UN Global Platform, which also
    hosts a dedicated working group to promote the use of AIS data to derive economic
    indicators.
