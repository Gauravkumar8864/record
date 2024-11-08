import pyaudio
import wave
import keyboard


def record_audio(filename):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    frames = []

    try:
        while True:
            if keyboard.is_pressed('space'):
                print("Recording stopped")
                break
            data = stream.read(1024)
            frames.append(data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

        sound_file = wave.open(filename, "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
        print(f"Recording saved as {filename}")


def main():
    count = 1
    while True:
        input("Press Enter to start recording, and press Space to stop...")
        filename = f"recording_{count}.wav"
        record_audio(filename)
        count += 1
        if input("Press 'q' to quit or any other key to record another file: ").lower() == 'q':
            break


if __name__ == "__main__":
    main()
