import re
from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository


def save(artist):
    sql = "INSERT INTO artists(name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0] ["id"]
    artist.id = id
    return artist

def delete_all():
    sql = 'DELETE FROM artists'
    run_sql(sql)

def find_artist_by_id(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist(result["name"], result["id"])
    return artist


def list_all_artists():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists