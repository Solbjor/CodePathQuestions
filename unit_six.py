#class SongNode:
#	def __init__(self, song, next=None):
#		self.song = song
#		self.next = next

# For testing
#def print_linked_list(node):
#    current = node
#    while current:
#        print(current.song, end=" -> " if current.next else "")
#        current = current.next
#    print()

#node3 = SongNode("Bad Romance")		
#node2 = SongNode("Party Rock Anthem",node3)
#top_hits_2010s = SongNode("Uptown Funk", node2)



#print_linked_list(top_hits_2010s)

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    freq ={}
    current = playlist
    while current: #o(n) b/c we only used one loop
        artist = current.artist
        if artist in freq:
            freq[artist] +=1
        else:
            freq[artist] =1
        current = current.next
    return freq  

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))

#class SongNode:
 #   def __init__(self, song, artist, next=None):
  #      self.song = song
   #     self.artist = artist
    #    self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next: #O(N) where N is the number of nodes in the list (time complexity)
        if current.next.song == song: #O(1) because the only auxiliary pointer used 
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))
print_linked_list(remove_song(playlist, "Simple Twist of Fate"))


class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow.song == fast.song:
            return True
    return False
    
   #would the if statement go outside the loop instead? as like a final check 
   #no bc if fast meets the end of lists theres no more cycle. is that what ur asking? 
   #try it maybe
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))