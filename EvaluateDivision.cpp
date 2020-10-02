#include <map>
#include <string>

using namespace std;

double depthFirstSearch(map<string, map<string, int>> graph, string firstQuerie, string secondQuerie, double weight)	{
	if (graph[firstQuerie].count(secondQuerie) != 0)
		return graph[firstQuerie][secondQuerie];

	double ans = -1;



	return ans;
}

std::vector<double> calcEquation(vector<vector<string>> &equations, vector<double> &values, vector<vector<string>> &queries) {
	vector<double> ans;
	map<string, map<string, int>> graph;
	for (int index = 0; index < equations.size(); ++index)	{
		string vertex = equations[index][0], neighbor = equations[index][1];
		graph[vertex][neighbor] = values[index];
		graph[neighbor][vertex] = 1/values[index];
	}

	for (auto querie : queries)	{
		string firstQuerie = querie[0], secondQuerie = querie[1];
		ans.push_back(depthFirstSearch(graph, firstQuerie, secondQuerie, 1));
	}


}