from abc import abstractclassmethod
from typing import List, Optional, List, Union
from entities.generic import *
from entities.music import *
from providers.data_model import DataModel


class Music:
    @classmethod
    def play_music(
        cls,
        album: Optional[Album],
        artist: Optional[Artist],
        genre: Optional[Genre],
        playlist: Optional[Playlist],
        music_type: Optional[MusicType],
        song: Optional[Song],
    ) -> List[MusicEntity]:
        music = MusicEntity(
            album=album,
            artist=artist
            genre=genre,
            playlist=playlist,
            music_type=music_type,
            song=song,
        )        
        event = Event(music);
        
        return music

        return data

    # @classmethod
    # def like_music(
    #     cls,
    #     album: Optional[Album],
    #     artist: Optional[Artist],
    #     genre: Optional[Genre],
    #     playlist: Optional[Playlist],
    #     music_type: Optional[MusicType],
    #     song: Optional[Song],
    # ) -> List[MusicEntity]:
    #     like = MusicLikeEntity(
    #         date_time=date_time,
    #         recipient=recipient,
    #         content=content,
    #     )
    #     data_model = DataModel()
    #     data_model.append(message)
    #     return message
