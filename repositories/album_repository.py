from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository


def save(album):
    sql = "INSERT INTO albums(title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def find_album_by_id(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.find_artist_by_id(result["id"])
        album = Album(result["title"], result["genre"], artist, result["id"])
    return album


def list_all_albums():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.find_artist_by_id(row["id"])
        album = Album(row["title"], row["genre"], artist, row["id"])

        albums.append(album)
    return albums


def list_albums_by_artist(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]

    results = run_sql(sql, values)
    for row in results:
        album = Album(row["title"], row["genre"], artist, row["id"])
        albums.append(album)
    return albums


def delete_album(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def edit_album(album):
    sql = "UPDATE albums SET(title, genre, artist_id) = (%s,%s,%s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)
