"""Vector-store based data structures."""

from llama_index_es.indices.multi_modal.base import MultiModalVectorStoreIndex
from llama_index_es.indices.multi_modal.retriever import MultiModalVectorIndexRetriever

__all__ = [
    "MultiModalVectorStoreIndex",
    "MultiModalVectorIndexRetriever",
]
