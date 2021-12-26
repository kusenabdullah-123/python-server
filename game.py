from connect import connection
database = connection()


def getDataAll():
    data = []
    database.execute("SELECT nama_game, desc_game FROM game")
    for nama_game, desc_game in database:
        data.append({
            'nama': nama_game,
            'desc': desc_game
        })
    return data
