from user import User
import csv

with open('exhibitA-input.csv') as csvfile:
    print('start reading')
    reader = csv.reader(csvfile, delimiter='\t')
    users = []

    for i in range(1000):
        users.append(User()) 

    print('start operation row by row')
    for row in reader:
        if row[2] == 'CLIENT_ID':
            continue
        if '10/08/2016' not in row[3]:
            continue
        
        client_id = int(row[2])
        song_id = int(row[1])
        temp_user = User(client_id, song_id)
        user_exist = False
        if users[client_id].user_id == -1:
            users[client_id].user_id = client_id
            users[client_id].add_song_id(song_id)
        else:
            users[client_id].add_song_id(song_id)

    print('end reading operation')
    distinct_song_346 = 0
    max_songs_value = 0
    total_songs = 0
    print('find distinct number 346 users')
    for user in users:
        total_songs += len(user.song_id)
        print('user id: ', user.user_id, '#of songs: ', len(user.song_id))
        if len(user.song_id) == 346:
            distinct_song_346 += 1

        if len(user.song_id) > max_songs_value:
            max_songs_value = len(user.song_id)

    print('\n\n\n')    
    print('distinct song 346: ', distinct_song_346)
    print('max songs: ', max_songs_value)
    print('total songs: ', total_songs)

