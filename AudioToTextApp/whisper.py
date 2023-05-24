from transformers import *
import torch
import soundfile as sf
import os
import torchaudio

device = "cuda:0" if torch.cuda.is_available() else "cpu"

whisper_model_name = "openai/whisper-small"
whisper_processor = WhisperProcessor.from_pretrained(whisper_model_name)
whisper_model = WhisperForConditionalGeneration.from_pretrained(whisper_model_name).to(device)

def load_audio(audio_path):
  """Load the audio file & convert to 16,000 sampling rate"""
  # load our wav file
  speech, sr = torchaudio.load(audio_path)
  resampler = torchaudio.transforms.Resample(sr, 16000)
  speech = resampler(speech)
  return speech.squeeze()

def get_transcription_whisper(audio_path, model, processor, language="english", skip_special_tokens=True):
  # resample from whatever the audio sampling rate to 16000
  speech = load_audio(audio_path)
  # get the input features
  input_features = processor(speech, return_tensors="pt", sampling_rate=16000).input_features.to(device)
  # get special decoder tokens for the language
  forced_decoder_ids = processor.get_decoder_prompt_ids(language=language, task="transcribe")
  # perform inference
  predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
  # decode the IDs to text
  transcription = processor.batch_decode(predicted_ids, skip_special_tokens=skip_special_tokens)[0]
  return transcription

print(get_transcription_whisper("test_wav.wav", whisper_model, whisper_processor))