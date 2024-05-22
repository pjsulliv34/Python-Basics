"""
This program reads in 4 different text files information about a current teams season, win, loss, and games left. As
well as each teams planned games for the rest of the season. Using this information, the program first calculates
whether the team will be trivially eliminated using the win loss and games left columns. Next the program utilizes
the current season info and the planned games to construct a graph that shows all possible games that can be played. For
simplicity the second elimination calculation, we are not constructing graphs for any of the teams that are trivially
eliminated. We then use the constructed graph to calculate the mass flow using the networkx package. Utilizing the max
flow value, we can compare the sum of the total edges of the planned games to see if any more of the teams will be
eliminated.
"""
# Import the packages
import networkx as nx
import math


# Create the eliminate class
class Eliminate:

    # Create Eliminate object with initial instances
    def __init__(self, file_name):
        self.file_name = file_name

    # Create the read_format method
    def read_format(self):

        # Opening up txt file in reader mode
        with open(self.file_name, 'r') as reader:

            # Grab number of teams from reader file
            number_of_teams = int(reader.readline())

            # Initialize empty lists and dictionarys
            team_data = []
            remaining_games = []
            team_id = {}

            # For loop to loop through range of number of teams
            for i in range(number_of_teams):

                # Read in current line from txt file
                line = reader.readline().strip().split()

                # Append list and dictionarys with information from current line
                team_data.append([line[0], [line[1], line[2], line[3]]])
                team_id[line[0]] = i

                # Initialize empty temp list
                temp_table = []

                # For loop to loop through range of teams again
                for item in range(number_of_teams):

                    # Append temp table
                    temp_table.append(line[4 + item])

                # Append list with current temp table
                remaining_games.append([line[0],temp_table])

                # Clear temp table for next loop in for loop
                temp_table.clear

            # Return the the lists and dictionarys created in method
            return team_data, remaining_games, team_id



    # Create graph method
    def graph(self, game_verts, team_verts, sink_verts):

        # Initialize directional graph
        graph = nx.DiGraph()

        # Create edges and nodes
        graph.add_edges_from(game_verts)
        graph.add_edges_from(team_verts)
        graph.add_edges_from(sink_verts)

        # return graph
        return graph

    # Create max flow method
    def max_flow(self, graph, source, sink, weight):

        # Grab max flow value and dictionary using networkx method
        val, dict_ = nx.maximum_flow(graph, source, sink, capacity= weight)

        # Return value and dictionary
        return val, dict_

    # Create Status method
    def status(self, summ: int, val: int):

        # If clause to check if sum of edges is <= to max flow value
        if summ <= val:
            # Return true if summ is larger then flow value
            return True
        else:
            # Return false if summ is less then val
            return False

# Create a main function to be called while running script
def main():

    # File list of text file names
    files = ['potter.txt','mlb.txt','ivy_league.txt','world_cup.txt']

    # For loop to loop through file name list
    for i in files:

        # Create an eliminate using eliminate class
        eliminate_object = Eliminate(i)

        # Read in txt file using read format method
        team_data, remaining_games, team_id = eliminate_object.read_format()

        # Initialize empty lists
        eliminated_trivially = []
        eliminated_teams = []

        # For loop to loop through team data
        for i in team_data:

            # Create max possible wins variable for each team
            max_possible_wins = int(i[1][0]) + int(i[1][2])

            # For loop to loop through team data again
            for team in team_data:

                # If clause current team in first loop is equal to current team
                if i != team:

                    # create trivial max variable using teams wins
                    trival_max = int(team[1][0])

                    # If clause to check if trivial max is greater then max possible wins
                    if trival_max > max_possible_wins:

                        # Append list with team data
                        eliminated_trivially.append([i[0],team[0]])
                        eliminated_teams.append(i[0])

        # initialize empty list
        not_eliminated_trivially = []

        # For loop to loop through team data
        for i in team_data:

            # If team not in team list append not eliminated list
            if i[0] not in eliminated_teams:
                not_eliminated_trivially.append(i[0])

        # Initialize emliminate status list
        eliminate_status = []

        # For loop to check not eliminated trivalally list
        for i in not_eliminated_trivially:

            # Initialize game vertice list
            game_vertices = []

            # For loop to loop through the range of the remaining games
            for team in range(len(remaining_games)):

                # If clause to check if name of team equals the team in eliminated trivally
                if remaining_games[team][0] != i:

                    # If so, for loop to go through the range of the remaining games
                    for games in range(len(remaining_games[team][1])):

                        # Final if clause to check if the index of the games equals the team id index, and the teams have seperate names
                        if games != team_id[i]:

                            # Append games vertices with info needed for nx.add_edges_from method
                            game_vertices.append(('source', f'{remaining_games[team][0]} - {team_data[games][0]}', {'games': int(remaining_games[team][1][games])}))

            # Initialize empty team vertices list
            team_vertices = []

            # Loop through game vertices
            for vert in game_vertices:

                # For loop to loop through the second element the games vertices
                for split in vert[1].split():

                    # If clause to check if current item does not equal '-'
                    if split != '-':

                        # Append team vertices list with vertice info
                        team_vertices.append((vert[1], split, {'games': math.inf}))

            # Initialize an empty list
            sink = []

            # For loop to loop through the range of the team data
            for data in range(len(team_data)):

                # If clause to check if current team name in for loop equals team name in the very first for loop
                if team_data[data][0] != i:

                    # If not append sink list with vertice info
                    sink.append((team_data[data][0], 'sink', {'games': int(team_data[team_id[i]][1][0]) +
                                                                       int(team_data[team_id[i]][1][2]) -
                                                                       int(team_data[team_id[team_data[data][0]]][1][0])}))


            # Initialize graph using vertice lists
            graph = eliminate_object.graph(game_vertices, team_vertices, sink)

            # Create flow value and dictionary using maximum flow method
            flow_value, flow_dict = eliminate_object.max_flow(graph,'source','sink','games')

            # Initialize empty variable summ
            summ = 0

            # For loop to loop through game vertices
            for vert in game_vertices:

                # Add edge value to summ
                summ += int(vert[2]['games'])

            # If loop to calculate status
            if eliminate_object.status(summ, flow_value):

                # If Status true, then append eliminate status list
                eliminate_status.append([i,'not eliminated'])

            else:

                # Append eliminate status list
                eliminate_status.append([i,'eliminated'])


        # Initialize empty list called final output
        final_output = []

        # For loop to loop through team data list
        for team in team_data:

            # If clause to check if team name in eliminated team name list
            if team[0] in eliminated_teams:

                # For loop to loop through eliminated trivalally list
                for elim in eliminated_trivially:

                    # If clause to check if eliminate name is equal to team name
                    if elim[0] == team[0]:

                        # Append final output list with elim data
                        final_output.append(elim)

            else:

                # For loop to loop through the eliminate status list
                for elm_status in eliminate_status:

                    # If clause to check if name is equal to elm status
                    if elm_status[0] == team[0]:

                        # If so append the final output list
                        final_output.append(elm_status)


        # For loop to loop through final output list
        for status in final_output:

            # If team name in eliminated teams list use first print statement otherwise use else clause print statement
            if status[0] in eliminated_teams:
                print(f'{status[0]} has been trivially eliminated by {status[1]}.')
            else:
                print(f'{status[0]} is {status[1]}.')

        # Additional spacing for formatting
        print('')

# Checks to see if dunder name changed to main
if __name__ == "__main__":
    main()


