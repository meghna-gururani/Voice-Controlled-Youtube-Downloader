from os import system as sys


def install (lib):
    stat = sys(f'pip install {lib}')
    if stat == 0:
        print(f'{lib} installed successfully')
        return True
    else:
        print(f'Failed to install {lib}')
        return False
    
libraries = [
    'pyttsx3',
    'beautifulsoup4',
    'urllib3',
    'moviepy',
    'pytube',
    'SpeechRecognition',
    'pyaudio'
]

for lib in libraries:
    install(lib)
