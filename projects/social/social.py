import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {1}")

        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle possible friends
        random.shuffle(possible_friendships)

        # add friendships
        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])

        # number of users must be greater than the average number of friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # create that empty queue you hear so much about

        q = Queue()
        # if len(self.friendships[user_id]) <= 0:
        #     pass
        # else:
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            last_user = path[-1]
            if last_user not in visited:
                visited[last_user] = path
                for neighbor in self.friendships[last_user]:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return visited

    """
    #go through every other element in the graph,
    for all_the_friends in self.users[user_id]:
    #  check if it's related to your starting element,
        if all_the_friends == user_id:
            return all_the_friends
    #  and if it is, add the path to the dictionary
                visited[user_id] = path
    """

    """
        # UNDERSTAND:
        # the first user: show the stops along the path to get to that friend
        # the next users are based on the next level of friends of the first user
        # if user 1 has friends 8, 10, 5
        # the next users that are explored are those that are within the first degree of seperation of the user 1.
        # -so whatever the path of going from 1 -> the second degree seperated. ie: if userid = 1 -> 8 -> read the friends of 8, got 2 -> 2:{1, 8, 2}
        # then all of that information once they've been recorded and the friend list exhausted, returns the whole dictionary of that.

        # first need to set up a bfs
        # need a queue
        # need a way to keep track of the paths
        # putthe paths into the dictonary

        # PLAN:
        # bfs to find the paths of all users/friends store them in the dic.
        #  if the user's id has no friends(neighbors) return the path as its id
        # if the user's id has friends:
        # store the friends' ID
        # put the friend into the array to be returned with its path to the original user
        #
        # Returns a dictionary containing every user in that user's
        # extended network with the shortest friendship path between them.
"""


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f"List of Friendships{sg.friendships}")
    connections = sg.get_all_social_paths(1)
    print(f"Connector paths: {connections}")
