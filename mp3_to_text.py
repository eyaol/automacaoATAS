import assemblyai as aai

aai.settings.api_key = "7ced294a7c0141019e71795c846de164"
transcriber = aai.Transcriber()

mp3_filename = '6c86141f2f744e12b33e0865b38ca36b.mp3'

config = aai.TranscriptionConfig( speaker_labels = True, speakers_expected = 2, language_code = 'pt' )

transcriber = aai.Transcriber()
transcricao = transcriber.transcribe(mp3_filename, config = config)


for sentenca in transcricao.utterances:
	print(f"Pessoa {sentenca.speaker}: {sentenca.text}")