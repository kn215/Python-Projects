def make_album(artist_name, album_name, song_list=None):
    """A function for displaying full album information"""
    album_dict = {
        'artist_name': artist_name.title(),
        'album_name': album_name.title(),
    }
    if song_list:
        album_dict['song_list'] = song_list
    return album_dict

artist_prompt = "Who is your favorite artist?: "
album_prompt = "What is your favorite album by them?: "

while True:
   artist_name = input(artist_prompt)
   if artist_name == 'quit':
      break
   
   album_name = input(album_prompt)
   if album_name == 'quit':
      break
   
   album = make_album (artist_name, album_name)
print(album)
    
album = make_album('no use for a name', 'making friends')
print(album)

album = make_album('red hot chili peppers','californication', '10')
print(album)

album = make_album('set your goals', 'mutiny', '11')
print(album)

#Prompts for input