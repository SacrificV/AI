<h1 align="left">This README is made by AI( im too lazy to do this stuff )</h1>

###

<br clear="both">

<div align="center">
  <img src="https://skillicons.dev/icons?i=latex" height="45" alt="latex logo"  />
  <img width="110" />
  <img src="https://skillicons.dev/icons?i=pycharm" height="45" alt="pycharm logo"  />
  <img width="110" />
  <img src="https://skillicons.dev/icons?i=py" height="45" alt="python logo"  />
  <img width="110" />
  <img src="https://skillicons.dev/icons?i=visualstudio" height="45" alt="visualstudio logo"  />
</div>

###

<h5 align="left">🧩 1. Labyrinth (BFS Shortest Path)<br>🔹 Problem Summary<br><br>Given a grid with:<br><br>A → start<br>B → destination<br>. → free cell<br># → wall<br><br>Find a path from A to B and print:<br><br>"YES" + path if it exists<br>"NO" otherwise<br><br>🔹 Approach: Breadth-First Search (BFS)<br><br>We use BFS because:<br><br>It explores level by level<br>Guarantees the shortest path in an unweighted grid<br>🔹 Key Components<br>1. Directions<br>directions = [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]<br>2. BFS Traversal<br>Start from A<br>Visit all reachable cells<br>Avoid revisiting using visited<br>3. Parent Tracking<br>parent[nx][ny] = (x, y, move)<br><br>Stores:<br><br>Previous cell (x, y)<br>Move taken (U/D/L/R)<br>4. Path Reconstruction<br><br>Start from B and go backward:<br><br>while cur != start:<br>    px, py, move = parent[cur[0]][cur[1]]<br>    path.append(move)<br><br>Then reverse the path.<br><br>🔹 Complexity<br>Time: O(n × m)<br>Space: O(n × m)<br>🔹 Key Insight<br><br>BFS ensures the first time we reach B, we have the shortest path.<br><br>⚡ 2. Range XOR Queries (Prefix XOR)<br>🔹 Problem Summary<br><br>Given an array, answer queries:<br><br>What is XOR of elements in range [a, b]?<br>🔹 Approach: Prefix XOR<br><br>Define:<br><br>px[i] = x1 ^ x2 ^ ... ^ xi<br>🔹 Query Formula<br>xor(a, b) = px[b] ^ px[a-1]<br>🔹 Why it Works<br><br>XOR cancels itself:<br><br>px[b] = x1 ^ x2 ^ ... ^ xa-1 ^ xa ^ ... ^ xb<br>px[a-1] = x1 ^ x2 ^ ... ^ xa-1<br><br>px[b] ^ px[a-1] = xa ^ ... ^ xb<br>🔹 Steps<br>Build prefix array<br>Answer each query in O(1)<br>🔹 Complexity<br>Preprocessing: O(n)<br>Each query: O(1)<br>Total: O(n + q)<br>🔹 Key Insight<br><br>XOR behaves like addition but with self-canceling property:<br><br>a ^ a = 0<br>🔤 3. Distinct Substrings (Suffix Automaton)<br>🔹 Problem Summary<br><br>Count the number of distinct substrings in a string.<br><br>🔹 Why Not Brute Force?<br><br>Total substrings:<br><br>O(n²)<br><br>Too slow for n = 100000.<br><br>🔹 Approach: Suffix Automaton (SAM)<br><br>A Suffix Automaton is a compressed structure that represents all substrings.<br><br>🔹 Key Idea<br><br>Each state contributes:<br><br>len[v] - len[link[v]]<br><br>Total distinct substrings:<br><br>sum(len[v] - len[link[v]])<br>🔹 Components<br>next → transitions<br>link → suffix links<br>length → longest string in state<br>🔹 Construction<br><br>For each character:<br><br>Create new state<br>Update transitions<br>Handle cloning if needed<br>🔹 Counting Substrings<br>for i in range(1, len(length)):<br>    result += length[i] - length[link[i]]<br>🔹 Complexity<br>Build: O(n)<br>Count: O(n)<br>🔹 Intuition<br><br>Each state represents multiple substrings.<br>The difference:<br><br>len[v] - len[link[v]]<br><br>= number of new substrings introduced<br><br>🔹 Example<br>Input: abaa<br>Output: 8<br><br>Distinct substrings:<br><br>a, b, aa, ab, ba, aba, baa, abaa<br>🧠 Final Comparison<br>Problem	Technique	Complexity	Key Idea<br>Labyrinth	BFS	O(n·m)	Shortest path in grid<br>Range XOR	Prefix XOR	O(n + q)	XOR cancellation<br>Distinct Substrings	Suffix Automaton	O(n)	State contributions</h5>

###

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sacrificv/sacrificv/output/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sacrificv/sacrificv/output/pacman-contribution-graph.svg">
  <img alt="pacman contribution graph" src="https://raw.githubusercontent.com/sacrificv/sacrificv/output/pacman-contribution-graph.svg">
</picture>

###

<img src="https://raw.githubusercontent.com/sacrificv/sacrificv/output/snake.svg" alt="Snake animation" />

###

<br clear="both">

<div align="center">
  <img src="https://skillicons.dev/icons?i=latex" height="45" alt="latex logo"  />
  <img width="110" />
  <img src="https://skillicons.dev/icons?i=pycharm" height="45" alt="pycharm logo"  />
  <img width="110" />
  <img src="https://skillicons.dev/icons?i=py" height="45" alt="python logo"  />
  <img width="110" />
  <img src="https://skillicons.dev/icons?i=visualstudio" height="45" alt="visualstudio logo"  />
</div>

###
