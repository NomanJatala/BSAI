"""
 Extension Challenge (Sample Solution) - Implementation Task 1
 (a) Records and visualizes the ORDER in which nodes are expanded
     by BFS, DFS and UCS (Matplotlib).
 (b) Adds A* Search with the Manhattan-distance heuristic.

 Requires: maze_search.py in the same folder, and matplotlib.
 Run:      python maze_extension.py
"""
import heapq
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from maze_search import MAZE, build_graph, bfs, dfs, ucs, path_cost, reconstruct

FILL = {".": "#FFFFFF", "S": "#FFFFFF", "G": "#FFFFFF", "M": "#D9B38C", "W": "#9CC9F0", "#": "#404040"}


# ------------------------------------------------------------------
# (b) A* SEARCH  f(n) = g(n) + h(n)
# ------------------------------------------------------------------
def manhattan(name_to_pos, goal):
    """h(n) = |row - goal_row| + |col - goal_col|.
    Admissible because every move costs at least 1 and at least
    this many moves are needed to reach the goal."""
    gr, gc = name_to_pos[goal]
    return lambda n: abs(name_to_pos[n][0] - gr) + abs(name_to_pos[n][1] - gc)


def astar(graph, start, goal, h):
    counter = 0
    frontier = [(h(start), counter, 0, start)]     # (f, order, g, node)
    best_g = {start: 0}
    parent = {start: None}
    explored = []
    while frontier:
        f, _, g, node = heapq.heappop(frontier)
        if node in explored or g > best_g[node]:
            continue
        explored.append(node)
        if node == goal:
            return reconstruct(parent, node), g, explored
        for child, step, _ in graph[node]:
            ng = g + step
            if child not in explored and ng < best_g.get(child, float("inf")):
                best_g[child] = ng
                parent[child] = node
                counter += 1
                heapq.heappush(frontier, (ng + h(child), counter, ng, child))
    return None, float("inf"), explored


# ------------------------------------------------------------------
# (a) EXPANSION-ORDER VISUALIZATION
# ------------------------------------------------------------------
def draw_panel(ax, name_to_pos, order, path, title):
    rows, cols = len(MAZE), len(MAZE[0])
    names = {p: n for n, p in name_to_pos.items()}
    rank = {n: i + 1 for i, n in enumerate(order)}
    for r in range(rows):
        for c in range(cols):
            ch = MAZE[r][c]
            ax.add_patch(Rectangle((c, rows - 1 - r), 1, 1, facecolor=FILL[ch], edgecolor="#999999"))
            n = names.get((r, c))
            if n is None:
                continue
            ax.text(c + 0.12, rows - 1 - r + 0.78, n, fontsize=9, color="#555555")
            if n in rank:                       # expansion number
                ax.text(c + 0.5, rows - 1 - r + 0.42, str(rank[n]), fontsize=15,
                        ha="center", va="center", weight="bold", color="#1F3864")
            else:
                ax.text(c + 0.5, rows - 1 - r + 0.42, "–", fontsize=13, ha="center", color="#BBBBBB")
    xs = [name_to_pos[n][1] + 0.5 for n in path]
    ys = [rows - 1 - name_to_pos[n][0] + 0.5 for n in path]
    ax.plot(xs, ys, color="#C0392B", lw=3, alpha=0.75, marker="o", ms=4)
    ax.set_xlim(0, cols); ax.set_ylim(0, rows); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title, fontsize=10)


def main():
    graph, name_to_pos = build_graph(MAZE)
    s, g = "S", "G"
    bp, bn, bt = bfs(graph, s, g)
    dp, dn, dt = dfs(graph, s, g)
    up, uc, un, ut = ucs(graph, s, g)
    h = manhattan(name_to_pos, g)
    ap, ac, aorder = astar(graph, s, g, h)

    runs = [("BFS", [t[0] for t in bt], bp), ("DFS", [t[0] for t in dt], dp),
            ("UCS", [t[0] for t in ut], up), ("A*", aorder, ap)]
    print("Heuristic values h(n):", {n: h(n) for n in graph})
    for name, order, path in runs:
        print(f"{name:<4} expansion order: {' '.join(order):<24} path: {'-'.join(path)}"
              f"  cost={path_cost(graph, path)}  expanded={len(order)}")

    fig, axes = plt.subplots(1, 4, figsize=(14, 4))
    for ax, (name, order, path) in zip(axes, runs):
        draw_panel(ax, name_to_pos, order, path,
                   f"{name}: {len(order)} expanded, cost {path_cost(graph, path)}")
    fig.suptitle("Order of node expansion (numbers) and returned path (red line)", fontsize=12)
    fig.tight_layout()
    fig.savefig("expansion_order.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
