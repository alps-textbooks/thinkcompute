# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC

from networkx import DiGraph

g = DiGraph()

g.add_node("Brad Pitt")
g.add_node("Eva Green")
g.add_node("George Clooney")
g.add_node("Catherine Zeta-Jones")
g.add_node("Johnny Depp")
g.add_node("Helena Bonham Carter")
g.add_node("Ocean's Twelve")
g.add_node("Fight Club")
g.add_node("Dark Shadows")

g.add_edge("Brad Pitt", "Ocean's Twelve")
g.add_edge("George Clooney", "Ocean's Twelve")
g.add_edge("Catherine Zeta-Jones", "Ocean's Twelve")

g.add_edge("Brad Pitt", "Fight Club")
g.add_edge("Helena Bonham Carter", "Fight Club")

g.add_edge("Helena Bonham Carter", "Dark Shadows")
g.add_edge("Johnny Depp", "Dark Shadows")
g.add_edge("Eva Green", "Dark Shadows")
