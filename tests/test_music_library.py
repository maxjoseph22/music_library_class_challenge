from lib.music_library import *

def test_music_library_inits_with_empty_list():
    music_library = Music_Library()
    assert music_library.library == []

def test_add_one_track():
    music_library = Music_Library()
    music_library.add_track("Work")
    assert music_library.library == ["Work"]

def test_add_three_tracks():
    music_library = Music_Library()
    music_library.add_track("Work")
    music_library.add_track("Binding")
    music_library.add_track("Song 2")
    assert music_library.library == ["Work", "Binding", "Song 2"]

def test_track_list():
    music_library = Music_Library()
    music_library.add_track("Work")
    music_library.add_track("Binding")
    music_library.add_track("Song 2")
    assert music_library.track_list() == ["Work", "Binding", "Song 2"]
