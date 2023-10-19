# paris_metro_graph

## Data description

Graph representation of the Parisian metro and RER network.

Two data formats are considered for the moment:

`paris.dimacs` is a list of edges. It contains only metro, no RER. Station names have been simplified, there are no accents and no spaces. There is no extra data (i.e. line number).

`stationsNoAccent.data` defines a directed graph as an union of paths, where each path is a valid direction of the metro. Each line of the file contains metro line number or identifier and a code for the path within the metro line (that might consist of multiple paths). Paths are identified with a header starting with `####` and the direction of the path in the form `source -- destination`

## TODO

- [ ] RER lines are not finished. Lines A, B and C are done, but only in one direction. The paths must be added in the inverse order. Line D is not done.
- [ ] Some stations have different names in different lines, particularly between RER and metro. Something must be done to correctly model transfers between lines.
- [ ] Add custom transfer times, and maybe custom times for lines or between stations to better model the cost of transport.