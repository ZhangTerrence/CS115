PREF_FILE = "musicrecplus.txt"

def init():
    """
    When the program starts, it loads the database from the file named musicrecplus.txt, if it exists. Otherwise, it
    creates the file. The file stores the database using the following format:
    Written by Terrence Zhang"""
    userData = {}
    try:
        with open(PREF_FILE, "r") as file:
            for line in file:
                [user, artists] = line.strip().split(":")
                if artists == "":
                    artistList = []
                else:
                    artistList = artists.split(",")
                artistList.sort()
                userData[user] = [artist.title() for artist in artistList]
        file.close()
    except FileNotFoundError:
        file = open(PREF_FILE, "w")
        file.close()
    user = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
    if user not in userData:
        done, count = False, 0
        while not done:
            pref = input("Enter an artist that you like (Enter to finish):")
            if pref == "":
                if count == 0:
                    userData[user] = []
                userData = dict(sorted(userData.items()))
                done = True
                menu(userData, user)
            else:
                if user not in userData:
                    artistList = [pref.title().strip()]
                    userData[user] = artistList
                    userData = dict(sorted(userData.items()))
                else:
                    L = [pref.title().strip()] + userData[user]
                    artistList = []
                    [artistList.append(artist) for artist in L if artist not in artistList]
                    artistList.sort()
                    userData[user] = artistList
                count += 1
    else:
        menu(userData, user)

def show_preferences(userData, user):
    print(userData[user])

def enter_preferences(userData, user):
    """Saves user's preference to database
       Written by Terrence Zhang"""
    pref = input("Enter an artist that you like (Enter to finish):")
    if pref == "":
        if user not in userData:
            userData[user] = []
            userData = dict(sorted(userData.items()))
            menu(userData, user)
    else:
        if user not in userData:
            artistList = [pref.title().strip()]
            userData[user] = artistList
            userData = dict(sorted(userData.items()))
        else:
            L = [pref.title().strip()] + userData[user]
            artistList = []
            [artistList.append(artist) for artist in L if artist not in artistList]
            artistList.sort()
            userData[user] = artistList
        enter_preferences(userData, user)

def delete_preferences(userData, user):
    string = ""
    for i in range(len(userData[user])):
        line = str(i + 1) + "." + userData[user][i]
        string += line + "\n"
    pref = input("Enter an artist that you like to delete (Enter to finish):\n" + string)
    if pref != "" and type(int(pref)) == int:
        userData[user] = userData[user][:int(pref) - 1] + userData[user][int(pref):]

def getRecommendations(currUser, prefs, userData):
    '''Gets recommendations for a user (currUser) based on the users in
userData(a dictionary) and the user's preferences in prefs (a list).
Returns a list of recommended artists.
Written by Ariana Beckford'''
    users = userData.keys()
    if len(users) == 1:
        print("Not enough data to create recommendations")
        print(menu(userData, users))
        # if statement above presents user with error message if there is one user in database, fixes recommendation bug
    bestUser = findBestUser(currUser, prefs, userData)
    if bestUser == None:
        print("No recommendations available at this time.")
        return []
    recommendations = drop(prefs, userData[bestUser])
    if recommendations == []:
        print("No recommendations available at this time.")
        return []
    else:
        recs = [*set(recommendations)]
        for artists in recs:
            print(artists)

def findBestUser(currUser, prefs, userData):
    '''Find the user whose tastes are closest to the current user. Return the best user's name
    Written by Ariana Beckford'''
    users = userData.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        if user[-1] == "$":
            continue
        elif userData[user] == userData[currUser]:
            continue
        else:
            score = numMatches(prefs, userData[user])
            if score > bestScore and currUser != user:
                bestScore = score
                bestUser = user
    if bestScore == 0:
        bestUser = None
    return bestUser

def drop(list1, list2):
    '''Return a new list that contains only the elements in list2 that were NOT in list1.
Written by Ariana Beckford'''
    list1.sort()
    list2.sort()
    list3 = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3

def numMatches(list1, list2):
    '''return the number of elements that match between two sorted lists
Written by Ariana Beckford'''
    list1.sort()
    list2.sort()
    matches = 0
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def popular_artists(userData):
    """ Prints the top 3 most popular artists, each in a new line. Written by Tristan Shabbick"""
    popDict = {}
    for (user, artists) in userData.items():
        if is_private(user) == False:
            for artist in artists:
                if artist in popDict:
                    popDict[artist] += 1
                else:
                    popDict[artist] = 1

    newPopDict = sorted(popDict.items(), key=lambda p: p[1], reverse=True)
    if len(newPopDict) == 0:
        print("Sorry, no artists found.")
    if len(newPopDict) == 1:
        print(newPopDict[0][0])
    if len(newPopDict) == 2:
        print(newPopDict[0][0])
        print(newPopDict[1][0])
    if len(newPopDict) >= 3:
        print(newPopDict[0][0])
        print(newPopDict[1][0])
        print(newPopDict[2][0])

def most_popular(userData):
    """Prints the magnitude (#) of the most popular artist. - Written by Tristan Shabbick """
    popDict = {}
    for (user, artists) in userData.items():
        if is_private(user) == False:
            for artist in artists:
                if artist in popDict:
                    popDict[artist] += 1
                else:
                    popDict[artist] = 1
    newPopDict = sorted(popDict.items(), key=lambda p: p[1], reverse=True)
    if newPopDict == []:
        print("Sorry, no artists found.")
    else:
        print(newPopDict[0][1])

def likes_the_most(userData):
    """ Prints the user with the most liked artists. Written by Tristan Shabbick"""
    most_liked = max(filter(lambda user: not is_private(user[0]), userData.items()), key=lambda p: len(p[1]))
    artists_liked = len(most_liked[1])
    if artists_liked == 0:
        print("Sorry, no artists found.")
    else:
        print(most_liked[0])

def is_private(user):
    """Helper function, if a user is private, returns true, otherwise false - Written by Tristan Shabbick"""
    return user[-1] == "$"

def save_and_quit(userData):
    """Saves data from database to text file
       Written by Terrence Zhang"""
    with open(PREF_FILE, "w") as file:
        for user in userData:
            artists = ",".join(userData[user])
            line = user + ":" + artists + "\n"
            file.write(line)
        file.close()

def menu(userData, user):
    """Prints menu of program
       Written by Terrence Zhang"""
    running = True
    while running:
        prompt = input(
            "Enter a letter to choose an option:\ns - Show preferences\ne - Enter preferences\nd - Delete preferences"
            "\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which "
            "user has the most likes\nq - Save and quit")
        if prompt == "s":
            show_preferences(userData, user)
        if prompt == "e":
            userData[user] = []
            enter_preferences(userData, user)
        if prompt == "d":
            delete_preferences(userData, user)
        if prompt == "r":
            getRecommendations(user, userData[user], userData)
        if prompt == "p":
            popular_artists(userData)
        if prompt == "h":
            most_popular(userData)
        if prompt == "m":
            likes_the_most(userData)
        if prompt == "q":
            save_and_quit(userData)
            running = False
    return
