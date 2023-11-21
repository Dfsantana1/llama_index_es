"""Init file."""

from llama_index_es.embeddings.adapter import (
    AdapterEmbeddingModel,
    LinearAdapterEmbeddingModel,
)
from llama_index_es.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index_es.embeddings.base import BaseEmbedding, SimilarityMode
from llama_index_es.embeddings.bedrock import BedrockEmbedding
from llama_index_es.embeddings.clarifai import ClarifaiEmbedding
from llama_index_es.embeddings.clip import ClipEmbedding
from llama_index_es.embeddings.cohereai import CohereEmbedding
from llama_index_es.embeddings.elasticsearch import (
    ElasticsearchEmbedding,
    ElasticsearchEmbeddings,
)
from llama_index_es.embeddings.google import GoogleUnivSentEncoderEmbedding
from llama_index_es.embeddings.google_palm import GooglePaLMEmbedding
from llama_index_es.embeddings.gradient import GradientEmbedding
from llama_index_es.embeddings.huggingface import (
    HuggingFaceEmbedding,
    HuggingFaceInferenceAPIEmbedding,
    HuggingFaceInferenceAPIEmbeddings,
)
from llama_index_es.embeddings.huggingface_optimum import OptimumEmbedding
from llama_index_es.embeddings.huggingface_utils import DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
from llama_index_es.embeddings.instructor import InstructorEmbedding
from llama_index_es.embeddings.langchain import LangchainEmbedding
from llama_index_es.embeddings.llm_rails import LLMRailsEmbedding, LLMRailsEmbeddings
from llama_index_es.embeddings.openai import OpenAIEmbedding
from llama_index_es.embeddings.pooling import Pooling
from llama_index_es.embeddings.text_embeddings_inference import TextEmbeddingsInference
from llama_index_es.embeddings.utils import resolve_embed_model
from llama_index_es.embeddings.voyageai import VoyageEmbedding

__all__ = [
    "AdapterEmbeddingModel",
    "BedrockEmbedding",
    "ClarifaiEmbedding",
    "ClipEmbedding",
    "CohereEmbedding",
    "BaseEmbedding",
    "DEFAULT_HUGGINGFACE_EMBEDDING_MODEL",
    "ElasticsearchEmbedding",
    "GoogleUnivSentEncoderEmbedding",
    "GradientEmbedding",
    "HuggingFaceInferenceAPIEmbedding",
    "HuggingFaceEmbedding",
    "InstructorEmbedding",
    "LangchainEmbedding",
    "LinearAdapterEmbeddingModel",
    "LLMRailsEmbedding",
    "OpenAIEmbedding",
    "AzureOpenAIEmbedding",
    "OptimumEmbedding",
    "Pooling",
    "GooglePaLMEmbedding",
    "SimilarityMode",
    "TextEmbeddingsInference",
    "resolve_embed_model",
    # Deprecated, kept for backwards compatibility
    "LLMRailsEmbeddings",
    "ElasticsearchEmbeddings",
    "HuggingFaceInferenceAPIEmbeddings",
    "VoyageEmbedding",
]
