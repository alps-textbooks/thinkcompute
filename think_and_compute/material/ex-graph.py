# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC

from networkx import Graph

g = Graph()

g.add_node("Tim Berners-Lee")
g.add_node("Tom Heath")
g.add_node("Christian Bizer")
g.add_node("Sören Auer")
g.add_node("Lalana Kagal")
g.add_node("Daniel J. Weitzner")

g.add_edge("Tim Berners-Lee", "Tom Heath", weight=18)
g.add_edge("Tim Berners-Lee", "Christian Bizer", weight=18)
g.add_edge("Tim Berners-Lee", "Sören Auer", weight=10)
g.add_edge("Tim Berners-Lee", "Lalana Kagal", weight=9)
g.add_edge("Tim Berners-Lee", "Daniel J. Weitzner", weight=8)
