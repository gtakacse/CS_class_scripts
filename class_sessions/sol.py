import sys

def get_data(path):
    with open(path, 'r') as f:
        return f.read().strip()

def get_mappings(data):
    chunks = data.split("\n\n")
    seeds = list(map(int, chunks[0].split(":")[1].split()))
    mappings = []
    for chunk in chunks[1:]:
        lines = chunk.split('\n')
        triplets = [list(map(int, line.split())) for line in lines[1:]]
        mappings.append(triplets)
        
    return seeds, mappings


def find_location(seed, mappings):
    loc = seed
    # print("=" * 10)
    # print(seed)
    # print("=" * 10)
    for mapping in mappings:
        for tgt, src, rng in mapping:
            if src <= loc <= src + rng -1:
                loc = loc - src + tgt
                break
        # print(loc)
    return loc

def part_1(seeds, mappings):
    locs = []
    for seed in seeds:
        locs.append(find_location(seed, mappings))
    return (min(locs))

def part_2(seeds, mappings):
    ans = sys.maxsize
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            ans = min(find_location(seed, mappings), ans)
    return ans

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "/Users/edittakacs/Documents/Coding/AoC/src/main/resources/2023/day05.txt"
    data = get_data(path)
    seeds, mappings = get_mappings(data)
    print(part_1(seeds, mappings))
    print(part_2(seeds, mappings))


    
