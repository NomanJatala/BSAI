"""
=====================================================================
 Artificial Intelligence - Implementation Task 1 (Sample Solution)
 Maze / Grid Search Problem solved with BFS, DFS and UCS
---------------------------------------------------------------------
 University of Okara - Department of Computer Science
 Instructor: Dr. Ghulam Ali, Associate Professor of Computer Science
=====================================================================

PROBLEM
    An agent stands at START (S) in a 4 x 4 maze and must reach GOAL (G).
    It can move one cell Up, Left, Right or Down. It cannot enter walls (#).
    Entering a cell costs according to its terrain:
        '.' normal floor = 1,  'M' mud = 3,  'W' water = 10
    The shortest route (fewest moves) goes through the water cell,
    so the path with fewer edges is NOT the least-cost path.

Run:   python maze_search.py
Only the Python standard library is used (collections.deque, heapq).
"""

from collections import deque
import heapq

# ------------------------------------------------------------------
# 1. MAZE DEFINITION
# ------------------------------------------------------------------
MAZE = [
    "S...",
    "W##.",
    ".#M.",
    "G...",
]

TERRAIN_COST = {".": 1, "S": 1, "G": 1, "M": 3, "W": 10}

# Actions in the order they are generated (this order matters for DFS).
ACTIONS = [
    ("Up",    (-1, 0)),
    ("Left",  (0, -1)),
    ("Right", (0, 1)),
    ("Down",  (1, 0)),
]

# Letters used to name open cells (G is reserved for the Goal).
CELL_LETTERS = "ABCDEFHIJKLNOPQRTUVWXYZ"


# ------------------------------------------------------------------
# 2. PROBLEM FORMULATION -> STATE-SPACE GRAPH
# ------------------------------------------------------------------
def label_cells(maze):
    """Give every open cell a readable name: S, G, or a letter A, B, C ...
    Returns two dicts: (row, col) -> name  and  name -> (row, col)."""
    letters = iter(CELL_LETTERS)
    pos_to_name, name_to_pos = {}, {}
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == "#":
                continue                       # walls are not states
            name = ch if ch in "SG" else next(letters)
            pos_to_name[(r, c)] = name
            name_to_pos[name] = (r, c)
    return pos_to_name, name_to_pos


def build_graph(maze):
    """Transition model: from each open cell, apply every action that stays
    inside the maze and does not hit a wall. The step cost is the terrain
    cost of the cell being ENTERED.
    Result:  graph[name] = [(neighbour_name, step_cost, action), ...]"""
    pos_to_name, name_to_pos = label_cells(maze)
    rows, cols = len(maze), len(maze[0])
    graph = {}
    for (r, c), name in pos_to_name.items():
        graph[name] = []
        for action, (dr, dc) in ACTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#":
                cost = TERRAIN_COST[maze[nr][nc]]
                graph[name].append((pos_to_name[(nr, nc)], cost, action))
    return graph, name_to_pos


def path_cost(graph, path):
    """Sum of step costs along a path."""
    total = 0
    for a, b in zip(path, path[1:]):
        total += next(cost for (n, cost, _) in graph[a] if n == b)
    return total


def reconstruct(parent, goal):
    """Follow parent pointers back from the goal to the start."""
    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return path[::-1]


# ------------------------------------------------------------------
# 3. BREADTH-FIRST SEARCH  (FIFO queue)
# ------------------------------------------------------------------
def bfs(graph, start, goal):
    frontier = deque([start])          # FIFO queue
    parent = {start: None}             # also acts as the "reached" set
    explored = []                      # expansion order
    trace = []

    while frontier:
        node = frontier.popleft()      # oldest node first
        explored.append(node)
        current_path = reconstruct(parent, node)

        if node == goal:               # goal test when the node is expanded
            trace.append((node, list(frontier), list(explored),
                          current_path, path_cost(graph, current_path)))
            return current_path, len(explored), trace

        for child, _, _ in graph[node]:
            if child not in parent:    # not explored and not in frontier
                parent[child] = node
                frontier.append(child)

        trace.append((node, list(frontier), list(explored),
                      current_path, path_cost(graph, current_path)))
    return None, len(explored), trace


# ------------------------------------------------------------------
# 4. DEPTH-FIRST SEARCH  (LIFO stack, graph search)
# ------------------------------------------------------------------
def dfs(graph, start, goal):
    frontier = [(start, [start])]      # stack of (node, path to node)
    explored = []
    explored_set = set()               # cycle detection
    trace = []

    while frontier:
        node, path = frontier.pop()    # newest node first
        if node in explored_set:       # already expanded via another path
            continue
        explored.append(node)
        explored_set.add(node)

        if node == goal:
            trace.append((node, [n for n, _ in frontier], list(explored),
                          path, path_cost(graph, path)))
            return path, len(explored), trace

        # Push children in REVERSE action order so the first action
        # (Up, then Left, Right, Down) ends up on top of the stack.
        for child, _, _ in reversed(graph[node]):
            if child not in explored_set:
                frontier.append((child, path + [child]))

        trace.append((node, [n for n, _ in frontier], list(explored),
                      path, path_cost(graph, path)))
    return None, len(explored), trace


# ------------------------------------------------------------------
# 5. UNIFORM-COST SEARCH  (priority queue ordered by g(n))
# ------------------------------------------------------------------
def ucs(graph, start, goal):
    counter = 0                        # tie-breaker: FIFO among equal costs
    frontier = [(0, counter, start)]   # (g, order, node)
    best_cost = {start: 0}             # cheapest known cost to each node
    parent = {start: None}
    explored = []
    explored_set = set()
    trace = []

    def frontier_view():
        """Live frontier entries (stale duplicates hidden), cheapest first."""
        live = [(g, k, n) for (g, k, n) in frontier
                if n not in explored_set and g == best_cost[n]]
        return [f"{n}({g})" for g, k, n in sorted(live)]

    while frontier:
        g, _, node = heapq.heappop(frontier)   # lowest path cost first
        if node in explored_set or g > best_cost[node]:
            continue                            # stale entry - skip
        explored.append(node)
        explored_set.add(node)
        current_path = reconstruct(parent, node)

        if node == goal:
            trace.append((node, frontier_view(), list(explored), current_path, g))
            return current_path, g, len(explored), trace

        for child, step, _ in graph[node]:
            new_cost = g + step
            if child not in explored_set and new_cost < best_cost.get(child, float("inf")):
                best_cost[child] = new_cost     # found a cheaper way
                parent[child] = node
                counter += 1
                heapq.heappush(frontier, (new_cost, counter, child))

        trace.append((node, frontier_view(), list(explored), current_path, g))
    return None, float("inf"), len(explored), trace


# ------------------------------------------------------------------
# 6. OUTPUT HELPERS
# ------------------------------------------------------------------
def show_maze(maze, name_to_pos):
    print("Maze (terrain)            Maze (state names)")
    names = {pos: n for n, pos in name_to_pos.items()}
    for r, row in enumerate(maze):
        left = " ".join(row)
        right = " ".join(names.get((r, c), "#") for c in range(len(row)))
        print(f"   {left:<22}   {right}")
    print("Costs: '.'=1  M(mud)=3  W(water)=10  #=wall\n")


def show_graph(graph):
    print("Adjacency list  (neighbour: step cost, action)")
    for node, edges in graph.items():
        text = ", ".join(f"{n}:{c} {a}" for n, c, a in edges)
        print(f"   {node} -> {text}")
    print()


def show_trace(title, trace, frontier_is_text=False):
    print(f"--- {title} trace ---")
    print(f"{'Step':<5}{'Node':<6}{'Frontier':<26}{'Explored':<26}{'Current path':<22}{'Cost':>4}")
    for i, (node, front, expl, path, cost) in enumerate(trace, 1):
        f = ", ".join(front) if front else "-"
        print(f"{i:<5}{node:<6}{f:<26}{','.join(expl):<26}{'-'.join(path):<22}{cost:>4}")
    print()


# ------------------------------------------------------------------
# 7. MAIN PROGRAM
# ------------------------------------------------------------------
def main():
    graph, name_to_pos = build_graph(MAZE)
    start, goal = "S", "G"

    show_maze(MAZE, name_to_pos)
    show_graph(graph)

    bfs_path, bfs_n, bfs_trace = bfs(graph, start, goal)
    dfs_path, dfs_n, dfs_trace = dfs(graph, start, goal)
    ucs_path, ucs_cost, ucs_n, ucs_trace = ucs(graph, start, goal)

    show_trace("BFS", bfs_trace)
    show_trace("DFS", dfs_trace)
    show_trace("UCS", ucs_trace)

    results = [
        ("BFS", bfs_path, bfs_n),
        ("DFS", dfs_path, dfs_n),
        ("UCS", ucs_path, ucs_n),
    ]
    optimal = path_cost(graph, ucs_path)       # UCS is optimal (costs > 0)

    print("=== Comparison ===")
    print(f"{'Algorithm':<10}{'Returned path':<42}{'Length':>7}{'Cost':>6}{'Expanded':>10}{'Optimal?':>10}")
    for name, path, n in results:
        cost = path_cost(graph, path)
        print(f"{name:<10}{' -> '.join(path):<42}{len(path) - 1:>7}{cost:>6}{n:>10}"
              f"{'Yes' if cost == optimal else 'No':>10}")


if __name__ == "__main__":
    main()