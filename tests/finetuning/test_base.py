"""Test finetuning engine."""
import pkgutil

import pytest


def test_torch_imports() -> None:
    """Test that torch is an optional dependency."""
    # importing fine-tuning modules should be ok
    from llama_index_es.finetuning import EmbeddingAdapterFinetuneEngine  # noqa
    from llama_index_es.finetuning import OpenAIFinetuneEngine  # noqa
    from llama_index_es.finetuning import SentenceTransformersFinetuneEngine  # noqa

    # if torch isn't installed, then these should fail
    if pkgutil.find_loader("torch") is None:
        with pytest.raises(ModuleNotFoundError):
            from llama_index_es.embeddings.adapter_utils import LinearLayer
            from llama_index_es.finetuning.embeddings.adapter_utils import train_model
    else:
        # else, importing these should be ok
        from llama_index_es.embeddings.adapter_utils import LinearLayer  # noqa
        from llama_index_es.finetuning.embeddings.adapter_utils import train_model  # noqa
