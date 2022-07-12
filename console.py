import pdb
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


artist1 = Artist("Oasis")
artist_repository.save(artist1)

album1 = Album("Definitely Maybe", "Rock", artist1)
album_repository.save(album1)

# album_repository.delete_all()

# artist_repository.delete_all()

result = artist_repository.find_artist_by_id(1)
print(result.name)


pdb.set_trace()