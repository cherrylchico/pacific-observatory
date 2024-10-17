# Maritime Trade

## Methods
To estimate the trade volume, we refer to the ship’s dimension and reported changes in draught
during port calls. From Arslanalp, et. al (2021), vessels that contribute to trade in the 
PICs are from container ships, cargo carriers, and bulk carriers. 

$$   Load_{reported} = Disp_{reported} - Disp_{design} + DWT  $$
$$ Disp = L \times W \times D \times \rho \times c_D  $$

where:
- $D_{reported}$ = draught of the ship at report time
- $D_{design}$ = design draught or maximum possible draught, constant per ship 
- $DWT$ = deadweight tonnage or total load capacity, constant per ship 
- $L$ = length of the ship 
- $$W$ = width of the ship 
- $\rho$ = density of salt water 
- $c_D$ = block coefficient at draught D

The $c_{design}$ is taken from a technical report that publishes the block
coefficient of ships per design classification, but the classification does not easily
map with the categories in Ship Registry. However, from the $Disp$ equation, by using the design
displacement, design draught, length and width which are avialable in the Ship Registry, 
we can derive the $c_{design}$ as follows:

$$
c_{Ddesign} = \frac {Disp_{design}}{L \times W \times D_{design} \times \rho}
$$

Fuel tankers are excluded as they are mostly involved in re-exportation or transshipment. 
In addition, vessels in transit, which are defined as those spending less than 5 hours 
in the port and without any changes in draft between the current and next port, are also 
excluded. 

To determine the trade flow, the difference in the cargo volume on arrival and on 
departure was calculated. If there was no difference in volume, it was assumed that 
the draught value was not accurately reported. In such cases, the trade flow was replaced 
by the historical average net cargo volume of the vessel for that specific port. 
Finally, imports were identified as those where trade flow is less than 0, indicating 
that the departure cargo volume is lower than the arrival cargo volume, and exports were 
those where trade flow is higher than 0.

$$ 
Net Cargo = Load_{departure} - Load_{arrival}
$$