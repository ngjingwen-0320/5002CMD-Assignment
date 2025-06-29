# INTI Matriculation Number: P23015051
# Name: Ng Jing Wen

# Part 1: Construct Unweighted Directed Graph
class Graph:
    def __init__(self):
        self.adjacency = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def addEdge(self, fromVertex, toVertex):
        if fromVertex in self.adjacency and toVertex in self.adjacency:
            if toVertex not in self.adjacency[fromVertex]:
                self.adjacency[fromVertex].append(toVertex)

    def listOutgoingAdjacentVertex(self, vertex):
        return self.adjacency.get(vertex, [])

    def listIncomingAdjacentVertex(self, vertex):
        return [v for v in self.adjacency if vertex in self.adjacency[v]]


# Part 2: Create Person Class
class Person:
    def __init__(self, name, gender, bio, privacy):
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy  # 'public' or 'private'

    # Part 5(b): Private Settings
    def __str__(self):
        if self.privacy == 'private':
            return f"Name: {self.name} (Private Profile)"
        else:
            return f"Name: {self.name}\nGender: {self.gender}\nBiography: {self.bio}"


def show_menu():
    print("\n--- Social Media App ---")
    print("1. View names of all profiles")
    print("2. View details of any profile")
    print("3. View followers of any profile")
    print("4. View followed accounts of any profile")
    print("5. Add a new user")
    print("6. Follow someone")
    print("7. Unfollow someone")
    print("8. Exit")

def print_title(people, title):
    print("=" * 40)
    print(title)
    print("=" * 40)
    i = 1
    for name in people:
        print(f"{i}. {name}")
        i += 1


def main():
    # Part 3: Create Person Objects
    # Create people profiles
    people = {
        "Karen": Person("Karen", "Female", "Just an ordinary woman", "public"),
        "Susy": Person("Susy", "Female", "Just a normal person", "private"),
        "Brian": Person("Brian", "Male", "Just an ordinary teenager", "public"),
        "Calvin": Person("Calvin", "Male", "Just an ordinary man", "public"),
        "Eva": Person("Eva", "Female", "Just a hardworking woman", "private")
    }

    # Part 4: Create Graph Object
    # Create graph and add users as vertices
    g = Graph()
    for person in people:
        g.addVertex(person)

    # Add following relationships (edges)
    g.addEdge("Karen", "Susy")
    g.addEdge("Karen", "Brian")
    g.addEdge("Karen", "Eva")

    g.addEdge("Eva", "Karen")
    g.addEdge("Eva", "Calvin")

    g.addEdge("Brian", "Karen")
    g.addEdge("Brian", "Susy")

    running = True

    while running:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print_title(people, "View Names of All Profiles")

        elif choice == "2":
            print_title(people, "View Details of Any Profile")
            name = input("Enter user name: ").title()
            if name in people:
                print("\nProfile Info:")
                print(people[name])
            else:
                print("User not found.")

        elif choice == "3":
            print_title(people, "View Followers of Any Profile")
            name = input("Enter user name: ").title()
            if name in people:
                followers = g.listIncomingAdjacentVertex(name)
                print(f"\n{name} is followed by:")
                if followers:
                    for person in followers:
                        print(f"- {person}")
                else:
                    print("No followers.")
            else:
                print("User not found.")

        elif choice == "4":
            print_title(people, "View Followed Accounts of Any Profile")
            name = input("Enter user name: ").title()
            if name in people:
                followed = g.listOutgoingAdjacentVertex(name)
                print(f"\n{name} follows:")
                if followed:
                    for person in followed:
                        print(f"- {person}")
                else:
                    print("No followed accounts.")
            else:
                print("User not found.")

        # Part 5: Advanced Features
        # Part 5(a): Add New User Profile
        elif choice == "5":
            print("=" * 30)
            print("Add a New User")
            print("=" * 30)
            name = input("Enter name: ").title()
            gender = input("Enter gender (male/female): ").title()
            bio = input("Enter bio: ")
            privacy = input("Enter privacy (public/private): ").lower()
            person = Person(name, gender, bio, privacy)

            people[name] = person
            g.addVertex(name)
            print(f"{name} has been added.\n")

        # Part 5(c): Follow Someone
        elif choice == "6":
            print_title(people, "Follow Someone")
            follower = input("Enter follower's name: ").title()
            followee = input("Enter followee's name: ").title()

            if follower in people and followee in people:
                g.addEdge(follower, followee)
                print(f"{follower} now follows {followee}.\n")
            else:
                print("Invalid names. Please try again.\n")

        # Part 5(d): Unfollow Someone
        elif choice == "7":
            print_title(people, "Unfollow Someone")
            follower = input("Enter follower's name: ").title()
            followee = input("Enter followee's name: ").title()

            if follower in g.adjacency and followee in g.adjacency[follower]:
                g.adjacency[follower].remove(followee)
                print(f"{follower} has unfollowed {followee}.\n")
            else:
                print("They are not connected, or user doesn't exist.\n")

        elif choice == "8":
            print("Exiting program.")
            running = False

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()