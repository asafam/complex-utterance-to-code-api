from abc import abstractclassmethod
from typing import Iterable, Optional, List, Union
from entities.generic import *
from entities.music import *
from providers.data_model import DataModel

class Music():
    
    @classmethod
    def play_music(
        cls,
        album: Optional[Album],
        artist: Optional[Artist],
        genre: Optional[Genre],
        playlist: Optional[Playlist],
        music_type: Optional[MusicType],
        song: Optional[Song],
    ) -> Iterable[MusicEntity]:
        data_model = DataModel()
        data = data_model.get_data(MusicEntity)
        if album:
            data = [x for x in data if x.data.get('album') == album]
            
        if artist:
            data = [x for x in data if x.data.get('artist') == artist]
            
        if genre:
            data = [x for x in data if x.data.get('genre') == genre]
            
        if playlist:
            data = [x for x in data if x.data.get('playlist') == playlist]
            
        if music_type:
            data = [x for x in data if x.data.get('music_type') == music_type]
            
        if song:
            data = [x for x in data if x.data.get('song') == song]
        
        return data
