from cs101audio import *
import time

def main():
    
    bass_drum = Audio()
    bass_drum.open_audio_file("Bass-Drum-2.wav")
    
    snare_drum = Audio()
    snare_drum.open_audio_file("Snare.wav")
    
    
#     bar = loop_drum_beat(4, bass_drum, snare_drum)
#     bar.play()

    bar = loop_drum_beat_with_tempo(4, bass_drum, snare_drum, 500)
#     bar.play()
    
    four_bars = bar * 4
    
    four_bars.change_speed(0.8)
    
    four_bars.play()
    

    

def loop_drum_beat_with_tempo(notes_per_bar, bass, snare, ms_per_beat):
    """Loops a bass drum a few times and then a snare drum once.
    Number of total drum hits is given by notes_per_bar."""
    
    beat = Audio()
    
    # Trim the bass drum to last only ms_per_beat long
    bass_trimmed = bass[:ms_per_beat]
    
    ## Pad snare
    snare_padded = Audio(ms_per_beat)
    snare_padded.overlay(snare)
    
    for _ in range(notes_per_bar - 1):
        beat += bass_trimmed
        
    beat += snare_padded
    return beat
    
    
    
def loop_drum_beat(notes_per_bar, bass, snare):
    """Loops a bass drum a few times and then a snare drum once.
    Number of total drum hits is given by notes_per_bar."""
    
    beat = Audio()
    
    for _ in range(notes_per_bar - 1):
        beat += bass
        
    beat += snare
    return beat
    
    
    
    
if __name__ == "__main__":
    main()