(lambda g: [None for g["d"],g["depth"] in [(lambda elem,level: max([level] + [d(child,level+1) for child in elem]),lambda elem,level: [None for g["maxdepth"] in [d(elem,0)]])]])(globals()) # Removed stub code