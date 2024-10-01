# Hopcroft-Karp Algorithm

This repository contains a Python implementation of the **Hopcroft-Karp algorithm** for finding the **maximum cardinality matching** in bipartite graphs.

## Overview

The Hopcroft-Karp algorithm is an efficient method to find a maximum matching in a bipartite graph. It operates in **O(√V * E)** time, where **V** is the number of vertices and **E** is the number of edges. This algorithm is widely used in problems involving bipartite graphs, including job assignment and network flow.

## Features

- **Efficient Matching**: Implements the Hopcroft-Karp algorithm to find the maximum cardinality matching.
- **Visualization**: Generates a GIF to visualize the matching process step by step.
- **Input Flexibility**: Accepts input from JSON files representing bipartite graphs.
- **Graph Representation**: Utilizes `networkx` for graph construction and manipulation.
- **Visualization Support**: Uses `matplotlib` for plotting and `imageio` for generating animated GIFs.

## Dependencies

To run this project, you will need to install the following Python libraries:

```bash
pip install matplotlib networkx imageio
```
## How to Run an Example

How to Run an Example
```bash
python3 main.py examples/example_1.json
```

In this example, example_1.json should represent a bipartite graph in JSON format, specifying vertices in sets U and V, along with the edges between them.

## Example JSON format

```json
{
    "U": ["A", "B", "C"],
    "V": ["X", "Y", "Z"],
    "edges": [["A", "X"], ["B", "Y"], ["C", "Z"], ["A", "Y"]]
}

```
This will execute the algorithm and generate the results.

## Output

- The algorithm finds the maximum cardinality matching for the given bipartite graph.
- After execution, a GIF is generated to visualize the step-by-step process of the algorithm.

### Example Gif

![Texto Alternativo](https://i.ibb.co/txGmQ6S/animation.gif)

## Contributions
Contributions are welcome! If you'd like to add new features, optimize the algorithm, or improve the visualizations, feel free to submit a pull request.


## License

This project is licensed under the MIT License.

