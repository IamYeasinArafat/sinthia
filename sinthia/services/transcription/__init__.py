from .transcriber import TranscriptionModel

_transcriber_instance = None

def get_transcriber():
    global _transcriber_instance
    if _transcriber_instance is None:
        _transcriber_instance = TranscriptionModel()
    return _transcriber_instance

__all__ = ["TranscriptionModel", "get_transcriber"]
