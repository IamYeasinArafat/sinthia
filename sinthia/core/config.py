from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SINTHIA_ROOT_DIR = PROJECT_ROOT_DIR / "sinthia"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT_DIR / ".env.development",
        env_file_encoding="utf-8"
    )

    transcription_model: str = Field( description="Model used for transcription.")
    audio_sample_rate: int = Field(default=16000, description="Sample rate for audio processing.")

appConfig = Settings()
