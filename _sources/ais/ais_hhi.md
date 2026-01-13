# Market concentration of vessel operators
Market concentration among vessel operators in Pacific Island countries can be analyzed using the Herfindahl-Hirschman Index (HHI):
$$
HHI =  \sum s_i^2 
$$

Where $s_i$ is the  market share of operator $i$. HHI value close to 0 indicates near perfect competition, while HHI value close to 1 indicates monopoly. 

Here, the market share is defined by the share of port calls from an operator. We use the [port calls data](ais_trade.md) derived from AIS, and the operator information from ship register data. Note that this excludes all vessels not registered with the IMO which is ~12% of port calls from cargo, tanker, and passenger vessels. 

## HHI per Country and Vessel Category

The following graph displays the latest and 2009 HHI values for each country and vessel category The countries are ranked from highest (most concentrated) to lowest (most competitive) latest HHI.

<div style="width: 100%; max-width: 800px; margin: 0 auto;">
  <iframe src="../interactive/ais/hhi-compare.html"
          frameborder="0"
          scrolling="no"
          style="width: 100%; height: 660px;">
  </iframe>
</div>


