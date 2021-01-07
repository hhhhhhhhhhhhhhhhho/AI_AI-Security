import pyaudio
import wave

SAMPLE_RATE = 44100 # 흘러나오는 소리에 대해 초당 표본 추출 횟수
FORMAT = pyaudio.paInt16 # 추출표본 하나에 대해 16Bit 를 통해 저장한다는 말임. 초당 표본 데이터 크기 44100 * 16 Bit
CHANNELS = 1 # 표본 데이터 음성 흐름의 개수를 의미함. mono = 1 , streo = 2
CHUNK = 512 # stream.read 함수에서 한번에 일겅올 표본 개수를 의미함. 
RECORD_SECONDS = 5 # 음성 녹음 시간
WAVE_OUTPUT_FILENAME = "output.wav" # 음성 녹음을 저장할 파일의 이름

p = pyaudio.PyAudio() # pyaudio 객체를 p 가 가리키게 함. 

stream = p.open(format=FORMAT, channels = CHANNELS, rate = SAMPLE_RATE, input = True, frames_per_buffer = CHUNK)
#Stream 에서는 pyaudio open 함수를 이용하여 오디오 흐름(?)을 연다.

print("Start to record the audio")

freams = []


for i in range(0, int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    #read 함수로부터 읽어들인 data 를 frame 에 추가시켜 음성데이터를 만들어 낸다. 

print("Recording is finished. ")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(SAMPLE_RATE)
wf.writeframes(b''.join(frames))
wf.close()
# import 된 wave 녹음파일을 만든다. 