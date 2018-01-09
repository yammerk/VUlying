# VUlying
project Heuristics 2018
***PROJECT DESCRIPTION***


The newly created Dutch airline Mokum Airways (MAW) is planning their flight schedule. They are based in Amsterdam and have landing rights for 28 destinations around Europe. The distances between these destinations is given by a distance matrix.

Mokum Airways has done market research for the airports where she has landing rights and checked how many people can potentially be transported by Mokum Airways.

The airline has a fleet of 6 Airbus A321 aircrafts and your goal is to create a flight schedule that results in as much profit as possible. Passengers pay per passenger-kilometers. For example, when an aircraft has transported 10 passengers over 10 kilometers, the number of passenger-kilometers is 100. Passengers may be transported via a detour, however only the kilometers of the direct route count toward the passenger-kilometers. In other words if a passenger flies from city A to city C via city B, only the distance city A – city C counts, not the detour.

Once per day each aircraft needs to land in the home base (Amsterdam) for crew changes. The start and endpoint of a route needs to be the same but can be any of the destinations. The take off and landing time for an aircraft needs to be between 06:00 and 02:00.

aircraft speed: 800 km/h
aircraft seats: 199
aircraft maximum range: 3199 km (refuel to extent range)
un-boarding and boarding time: 1 hour for both
refueling time: 1 hour (on top of the boarding time)

**Assignment**

a) Create a one-day flight schedule for a single aircraft that results in as much passenger-kilometers as possible.

b) Create a one-day flight schedule for all 6 aircrafts that results in as much passenger-kilometers as possible.

Advanced

c) Mokum Airways is not sure that Amsterdam is the best place for the home base. Find out if Amsterdam is the best place to base the airline or whether a different city would be better.
