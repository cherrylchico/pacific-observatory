# Maritime Trade
- General Methodology
  - Define port boundary
  - Generate port calls from boundary
  - Estimate trade / generate indicators

## Review of Related Literature
- <a href="https://www.imf.org/en/Publications/WP/Issues/2019/12/13/Big-Data-on-Vessel-Traffic-Nowcasting-Trade-Flows-in-Real-Time-48837"><b>2019 IMF: Big Data on Vessel Traffic: Nowcasting Trade Flows in Real Time</b><a>
  - Port Calls created by Marine Traffic
  - Data waterfall
    - Exclude: speed > 1.0 knot
    - Exclude: Anchorage and bunkering tankers - remove bunkering tankers
        - Fuel supplied to foreign vessels should be recorded as exports of the country according to international standards, although it is recognized that data collection may be challenging.6 Since the inclusion of these tankers introduces considerable volatility to the indices, we omit bunkering tankers from our valid port calls
    - Exclude: Ship arrived but not departerd
    - Exclude: Stay in the harbor outside reasonable range for trade activity
        - stay in port < 5hrs: unlikely to have enough time to load or unload goods in the port
        - stay in port > 60 hrs: Longer stays may be associated with ships visiting the port for repairs or maintenance services.
  - Indicators:
    - cargo number
        - cargo load
            - $ CWI_t = \sum_{i}^{} DWT_{i, t} \frac{|d_{i,t}^{D} - d_{i,t}^{A}|}{max(d_{i})} $
            - DWT is adjusted with a capacity utilization ratio.

- <a href="https://www.sciencedirect.com/science/article/pii/S1361920920305800"><b> 2020 Science Direct: Port disruptions due to natural disasters: Insights into port and logistics resilience</b><a>
  - no mention of how port calls were derived
  - ![image.png](ais/port-disruptions.png)

- <a href="https://www.imf.org/en/Publications/WP/Issues/2020/05/14/World-Seaborne-Trade-in-Real-Time-A-Proof-of-Concept-for-Building-AIS-based-Nowcasts-from-49393"><b> 2020 IMF: World Seaborne Trade in Real Time</b><a>
  - Port boundary:
    - SOG < 0.5, \& nav status anchored or moored

- <a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0248818#pone.0248818.s001"><b> 2021 Global economic impacts of COVID-19 lockdown measures stand out in high-frequency shipping data</b><a>
  - Port Boundary: manually mapped, berthing + navigation channels
  - Port Calls: Vessel call algorithm
    - Filter:
      - include: cargo and tanker vessels.
      - exclude: stay in port less than 5h and more than the 95th percentile (of the port) are truncated, as they are most likely associated with refueling, repair or maintenance.
      - exclude: turnaround time of less than 10h and leave the port area at a direction that is within 45 degree of the direction of entering the port area. These port calls are most likely associated with vessels passing a port (e.g. ports alongside a river).

- <a href="https://www.imf.org/en/Publications/WP/Issues/2021/08/20/Tracking-Trade-from-Space-An-Application-to-Pacific-Island-Countries-464345"><b> 2021 IMF: Tracking Trade from Space: An Application to Pacific Island Countries</b><a>
  - Port Boundary: "manually determined using satellite imagery"
  - Port Call:
    - include: focus on container ships—the main engine of seaborne trade in the Pacific—vehicle carriers, and bulk carriers (relevant for Fiji, Nauru, and Solomon Islands as commodity-exporters).
    - exclude: Fuel tankers are not included, as Pacific countries import a significant portion of fuel for re-exports (for visiting foreign vessels and airlines
    - exclude vessels in transit: turnaround time of less than 5 hours and no draft change between the current and next port

