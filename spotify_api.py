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
print(songs.head(10))

flag = True
FirstLoading(flag)

'''
個々の音楽取得
'''

def SpotifyApi(tpl):

	def FirstLoading(flag):
		if flag == True:
			song_info = pd.DataFrame()
			song_info['URL'] = 0
			song_info['URL'] = song_info['URL'].astype(str)
			song_info['track'] = 0
			song_info['track'] = song_info['track'].astype(str)
			song_info['artist'] = 0
			song_info['artist'] = song_info['artist'].astype(str)

			i = 0
			for url in songs["URL"] : 
				df = pd.DataFrame.from_dict(spotify.audio_features(url))
				song_info = song_info.append(df)

				song_info.iat[i, 0] = url
				i += 1
			p = 0
			for track in songs["Track Name"]:
				song_info.iat[p, 1] = track
				p += 1
			q = 0
			for artist in songs["Artist"]:
				song_info.iat[q , 2] = artist
				q += 1

			flag = False

		else:
			print("二回目以降なのでスキップ")



	#index振り直し
	song_info=song_info.reset_index(drop=True)
	song_info["rank"] = song_info.index + 1

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
		ser_abs_diff = (song_info['valence']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = song_info[ser_abs_diff == min_val]

		href = ts['URL']
		art = ts['artist']
		name = ts['track']

		d = ts.to_dict()
		print(d)

		d_url = d['URL']
		print(d_url)
		d_art = d['artist']
		print(d_art)
		d_name = d['track']

		return d_art,d_name,d_url

	elif tpl[0] == 'contempt':
		print('a')		
		ser_abs_diff = (song_info['loudness']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = song_info[ser_abs_diff == min_val]

		href = ts['URL']
		art = ts['artist']
		name = ts['track']

		d = ts.to_dict()
		print(d)

		d_url = d['URL']
		print(d_url)
		d_art = d['artist']
		print(d_art)
		d_name = d['track']

		return d_art,d_name,d_url


	elif tpl[0] == 'disgust' or tpl[0] == 'fear':
		print('a')
		ser_abs_diff = (song_info['energy']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = song_info[ser_abs_diff == min_val]

		href = ts['URL']
		art = ts['artist']
		name = ts['track']

		d = ts.to_dict()
		print(d)

		d_url = d['URL']
		print(d_url)
		d_art = d['artist']
		print(d_art)
		d_name = d['track']

		return d_art,d_name,d_url

	elif tpl[0] == 'anger':
		print('anger')
		ser_abs_diff = (song_info['loudness']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = song_info[ser_abs_diff == min_val]

		href = ts['URL']
		art = ts['artist']
		name = ts['track']

		d = ts.to_dict()
		print(d)

		d_url = d['URL']
		print(d_url)
		d_art = d['artist']
		print(d_art)
		d_name = d['track']

		return d_art,d_name,d_url

	elif tpl[0] == 'neutral':
		print('neutral')

		ser_abs_diff = (song_info['valence']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = song_info[ser_abs_diff == min_val]

		href = ts['URL']
		art = ts['artist']
		name = ts['track']

		d = ts.to_dict()
		print(d)

		d_url = d['URL']
		print(d_url)
		d_art = d['artist']
		print(d_art)
		d_name = d['track']

		return d_art,d_name,d_url


	elif tpl[0] == 'sadness':
		print('sadness')

		ser_abs_diff = (song_info['acousticness']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = song_info[ser_abs_diff == min_val]

		href = ts['URL']
		art = ts['artist']
		name = ts['track']

		d = ts.to_dict()
		print(d)

		d_url = d['URL']
		print(d_url)
		d_art = d['artist']
		print(d_art)
		d_name = d['track']

		return d_art,d_name,d_url

	elif tpl[0] == 'surprise':
		print('surprise')
		ser_abs_diff = (song_info['danceability']-tpl[1]).abs()
		min_val = ser_abs_diff.min()

		ts = song_info[ser_abs_diff == min_val]

		href = ts['URL']
		art = ts['artist']
		name = ts['track']

		d = ts.to_dict()
		print(d)

		d_url = d['URL']
		print(d_url)
		d_art = d['artist']
		print(d_art)
		d_name = d['track']

		return d_art,d_name,d_url

	else:
		print('a')



