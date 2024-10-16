def is_valid(coloring, region, color):
    """
    Check if it's valid to assign the given color to the given region.
    """
    for neighbor in region.neighbors:
        if coloring[neighbor] == color:
            return False
    return True

def backtrack(coloring, regions, colors):
    """
    Recursively try different color assignments for each region.
    """
    if all(coloring[region] is not None for region in regions):
        return coloring

    for region in regions:
        if coloring[region] is None:
            for color in colors:
                if is_valid(coloring, region, color):
                    coloring[region] = color
                    result = backtrack(coloring, regions, colors)
                    if result:
                        return result
                    coloring[region] = None
    return None

class Region:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

class MapColoring:
    def __init__(self, regions, colors):
        self.regions = regions
        self.colors = colors

    def solve(self):
        coloring = {region: None for region in self.regions}
        return backtrack(coloring, self.regions, self.colors)

# Example usage
regions = [
    Region("A"),
    Region("B"),
    Region("C"),
    Region("D"),
]

regions[0].neighbors = [regions[1], regions[2]]
regions[1].neighbors = [regions[0], regions[3]]
regions[2].neighbors = [regions[0], regions[3]]
regions[3].neighbors = [regions[1], regions[2]]

colors = ["Red", "Green", "Blue"]

map_coloring = MapColoring(regions, colors)
solution = map_coloring.solve()

if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"{region.name}: {color}")
else:
    print("No solution found")