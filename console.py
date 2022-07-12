import pdb
from unittest import result
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


artist1 = Artist("Oasis")
artist_repository.save(artist1)
artist2 = Artist("The Stone Roses")
artist_repository.save(artist2)
artist3 = Artist("Radiohead")
artist_repository.save(artist3)


album1 = Album("Definitely Maybe", "Rock", artist1)
album_repository.save(album1)
album2 = Album("Second Coming", "Rock", artist2)
album_repository.save(album2)
album3 = Album("OK Computer", "Rock", artist3)
album_repository.save(album3)
album4 = Album("Greatest Hits", "Rock", artist1)
album_repository.save(album4)
# album_repository.delete_all()

# artist_repository.delete_all()

# result = artist_repository.find_artist_by_id(1)
# print(result.name)

# result = album_repository.find_album_by_id(1)
# print(result.title)

# result = artist_repository.list_all_artists()

# for artist in result:
#     print(artist.name)


# result = album_repository.list_all_albums()
# for album in result:
#     print(album.title)

# result = album_repository.list_albums_by_artist(artist1)
# for album in result:
#     print(album.title)

# artist_repository.delete_artist(2)

album_repository.delete_album(2)

pdb.set_trace()