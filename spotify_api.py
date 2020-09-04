import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import json, csv
import face_api
import main

#認証
cliend_id = '2bff6a42cf5945b18f74077b578d4264'
cliend_secret = '8a8199b3631d4e6782b628dc5fb8b68c'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(cliend_id, cliend_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

songs = pd.read_csv("top100.csv", index_col=0)
songs.head(10)

print(songs.head(10))

'''
個々の音楽取得
'''

def SpotifyApi(tpl):
	song_info = pd.DataFrame()

	for url in songs["URL"] : 
	    df = pd.DataFrame.from_dict(spotify.audio_features(url))
	    song_info = song_info.append(df)
	#index振り直し
	song_info=df.reset_index(drop=True)
	song_info["rank"] = df.index + 1

	song_info.head(10)
	print(song_info.head(200))

	'''
	valence（曲の明るさ)ごとに並べ替え
	'''
	#song_info["top_20"]=(song_info["rank"] <= 20).astype(int)

	#tempo_range = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	#song_info["tempo_bin"] = pd.cut(song_info["valence"], tempo_range, labels = tempo_range[0:-1])

	#song_info.sample(10)
	#print(song_info.sample(10))


	if tpl[0] == 'happiness':
		print('happiness')
		ser_abs_diff = (df['valence']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		df[ser_abs_diff == min_val]
		print(df[ser_abs_diff == min_val])

		

	elif tpl[0] == 'contempt':
		print('a')
	elif tpl[0] == 'disgust' or tpl[0] == 'fear':
		print('a')
	elif tpl[0] == 'anger':
		print('a')
	elif tpl[0] == 'neutral':
		print('a')
	elif tpl[0] == 'sadness':
		print('a')
	elif tpl[0] == 'surprise':
		print('surprise') 
		#song_info=song_info.reset_index(drop=True)
		#song_info["rank"] = song_info.index + 1
		print(song_info)

		ser_abs_diff = (df['danceability']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = df[ser_abs_diff == min_val]
		#rank = ts["rank"]
		print(type(ts))
		print(ts)
		#print(rank)
		print(songs)
		#print(songs[ts[song_info.index + 1]])
		#return rank

		#main.getMusic(track_href)



	else:
		print('a')



