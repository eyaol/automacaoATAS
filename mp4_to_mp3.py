from moviepy.editor import *
import uuid

def mp4_to_mp3(mp4_filename, mp3_filename):
	arquivo_a_ser_convertido = AudioFileClip(mp4_filename)
	arquivo_a_ser_convertido.write_audiofile(mp3_filename)
	arquivo_a_ser_convertido.close()

if __name__ == "__main__":
  mp4_filename = '/Users/eniolee/Downloads/entrevista de Boechat com Jô Soares 360.mp4'
  mp3_filename = f'{uuid.uuid4().hex}.mp3'
  
  mp4_to_mp3(mp4_filename, mp3_filename)
