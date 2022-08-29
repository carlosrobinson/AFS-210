
from random import randint

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None
        self.size = 0

    def getTitle(self):
        # self.size = self.size + 1
        return self.title

    def getArtist(self):
        return self.artist
    
    def __str__(self):
        # self.size +=1
        return str(self.title + '\n' "by " + self.artist)

    # def __eq__(self, other):
        # return ((self.title, self.artist) == (other.title, other.artist)) <----this method causes the program to crash
        # after adding two nodes to the list. 
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
    
    
class SimplePlayer():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.list = []
        self.size = 0
        self.count = 0
        self.currently_playing = False
        
    # Displays the play list.
    def display_play_list(self):
        self.size = 0
        if len(self.list):
            # Show the current song list order
            for song in self.list:
                print(self.size, ".", str(song.__str__()))
                self.size+=1
        else:
            print("Playlist is Empty.")
            
            
    # Add a song to the playlist.   
    def add_song(self, title, artist):
        self.size = 0
        new_song = Song(title, artist)  
        new_song.next = None
        if self.tail != None:
            new_song.prev = self.tail
            self.tail.next = new_song.next
            self.list.append(new_song)
        else:
            self.head = new_song
            self.list.append(new_song)
        self.tail = new_song
        # self.head = new_song
    
        
    # Deletes the song in the track of the playlist
    def delete_song(self, index) :# <-----work on this-----------------------------------------------
        # Delete the node at the index-th in the list.
            self.size = 0
            self.list.pop(index)     
 
        
    # Plays tne first song in the playlist.
    def play_song(self):
        if self.list == []:
            return "Playlist is Empty."
        else:
            self.currently_playing = True
            print("Playing....")  
            return self.seek()
    
    
    def new_song(self):
        return self.list[-1]
    
    
    def stop_player(self):
        if self.currently_playing == False:
            print('No song is Currently Playing Press "Play"')
        else:
            print("Stopping mediaplayer....")
            self.currently_playing = False
    
    
    # If Song is playing return the name of artist and song
    def current_song_playing(self):
        if self.currently_playing:
            print("Currently playing: ", end=" ")
            return self.seek()
        else:
            return 'Press "Play" to Play a song'


    # Sets the index to move media player forward or backwards in the playlist.
    def seek(self):
        return self.list[self.count]
    
    
    # Plays the next song in the playlist. 
    def next_Song(self):
        # self.size = 0
        if self.currently_playing:
            if self.count < len(self.list) :
                self.count += 1
                if self.count >= abs(len(self.list)):
                    self.count = 0
                print("Skipping Forward....") 
                return f'Now Playing:\n{self.seek()}'
            else:
                self.count  = 0
                return self.seek()
        else:
            return 'Press "Play" to Play a song'
        
        
    # Plays the previous song in the the playlist.
    def prev_Song(self):
        if self.currently_playing:
            if self.count <= len(self.list):
                self.count -= 1
                if self.count <= -abs(len(self.list)):
                    self.count = 0
                print("Skipping Back....")
                return f'Now Playing:\n{self.seek()}'
            else:
                self.count = 0
                return self.seek()
        else:
            return 'Press "Play" to Play a song'
        
        
    # Shuffles the playlist and displays the shuffled list.
    def shuffle_play_list(self):
        self.count = 0
        play_list = len(self.list)
        for i in range(play_list):
            shuffle =  randint(i, play_list -1)
            self.list[i], self.list[shuffle] = self.list[shuffle], self.list[i]
        self.display_play_list()


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("9. Stop")
    print("0. Exit")
    print(47 * "-")
  
    
media_player = SimplePlayer()
media_player.list.append(Song("End Of The Road", "Boys II Men"))
media_player.list.append(Song("Nobody's Supposed to Be Here", "Deborah Cox"))
media_player.list.append(Song("Just Kickin' It", "Xscape"))
media_player.list.append(Song("Right Here", "SWV"))
media_player.list.append(Song("All My Life", "K-Ci & JoJo"))
media_player.list.append(Song("Poison", "Bell Biv DeVoe"))
media_player.list.append(Song("Waterfalls", "TLC"))
media_player.list.append(Song("Ex-Factor", "Lauryn Hill"))
media_player.list.append(Song("Fantasy", "Mariah Carey"))
media_player.list.append(Song("Twisted", "Keith Sweat"))




while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        title = input("Please Enter the songs title: ")
        artist = input("Please enter the artist name: ")
        media_player.add_song(title, artist)
        print(f"New Song: {media_player.new_song()} Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        if media_player.list == []:
            print("Playlist is Empty.")
        else:
            track_number = int(input("Enter Song track: "))
            print(f"{media_player.list[track_number]} Removed from Playlist")
            media_player.delete_song(track_number)
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
      
        print(media_player.play_song())
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print(media_player.next_Song())    
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print(media_player.prev_Song())    
    elif choice == 6:
        # Randomly shuffle the playlist and play the first son
        # Display song name that is now playing
        print("Shuffling....")          
        media_player.shuffle_play_list()
    elif choice == 7:
        # Display the song name and artist of the currently playing song
         
        print(media_player.current_song_playing())   
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        media_player.display_play_list()
    elif choice == 9:
        # Stop playing current song
        media_player.stop_player()
    elif choice == 0:
        print("Goodbye.")
        break
    elif choice != range(0, 9, 1):
        print('PlEASE ENTER A NUMBER 0 - 9')
        
        