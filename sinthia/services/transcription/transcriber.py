from parakeet_mlx import from_pretrained, BaseParakeet
from sinthia.core.config import appConfig
from sinthia.core.logging import init_logging
import logging
from pathlib import Path

init_logging()
logger = logging.getLogger("sinthia.transcription")

class TranscriptionModel:
    def __init__(self, model_name=None):
        self.model_name = model_name or appConfig.transcription_model
        self.model: BaseParakeet | None = None

    def load(self):
        if self.model is None:
            logger.debug(f"Loading transcription model: {self.model_name}")
            try:
                self.model = from_pretrained(self.model_name)
                logger.debug(f"Successfully loaded model: {self.model_name}")
            except Exception as e:
                logger.error(f"Failed to load model {self.model_name}: {e}")
                raise

    def transcribe(self, audio_path: Path):
        if self.model is None:
            self.load()
            if self.model is None:
                logger.error("In attempt to transcribe: Model is not loaded after attempting to load.")
                raise RuntimeError("Transcription model is not loaded.")

        logger.debug(f"Transcribing audio from: {audio_path}")
        try:
            transcription = self.model.transcribe(audio_path)
            logger.debug(f"Transcription successful for file: {audio_path}")
            return transcription
        except Exception as e:
            logger.error(f"Transcription failed")
