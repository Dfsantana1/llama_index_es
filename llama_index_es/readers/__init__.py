"""Data Connectors for LlamaIndex.

This module contains the data connectors for LlamaIndex. Each connector inherits
from a `BaseReader` class, connects to a data source, and loads Document objects
from that data source.

You may also choose to construct Document objects manually, for instance
in our `Insert How-To Guide <../how_to/insert.html>`_. See below for the API
definition of a Document - the bare minimum is a `text` property.

"""

from llama_index_es.readers.bagel import BagelReader
from llama_index_es.readers.base import ReaderConfig
from llama_index_es.readers.chatgpt_plugin import ChatGPTRetrievalPluginReader
from llama_index_es.readers.chroma import ChromaReader
from llama_index_es.readers.dashvector import DashVectorReader
from llama_index_es.readers.deeplake import DeepLakeReader
from llama_index_es.readers.discord_reader import DiscordReader
from llama_index_es.readers.download import download_loader
from llama_index_es.readers.elasticsearch import ElasticsearchReader
from llama_index_es.readers.faiss import FaissReader

# readers
from llama_index_es.readers.file.base import SimpleDirectoryReader
from llama_index_es.readers.file.docs_reader import PDFReader
from llama_index_es.readers.file.html_reader import HTMLTagReader
from llama_index_es.readers.github_readers.github_repository_reader import (
    GithubRepositoryReader,
)
from llama_index_es.readers.google_readers.gdocs import GoogleDocsReader
from llama_index_es.readers.json import JSONReader
from llama_index_es.readers.make_com.wrapper import MakeWrapper
from llama_index_es.readers.mbox import MboxReader
from llama_index_es.readers.metal import MetalReader
from llama_index_es.readers.milvus import MilvusReader
from llama_index_es.readers.mongo import SimpleMongoReader
from llama_index_es.readers.myscale import MyScaleReader
from llama_index_es.readers.notion import NotionPageReader
from llama_index_es.readers.obsidian import ObsidianReader
from llama_index_es.readers.pinecone import PineconeReader
from llama_index_es.readers.psychic import PsychicReader
from llama_index_es.readers.qdrant import QdrantReader
from llama_index_es.readers.slack import SlackReader
from llama_index_es.readers.steamship.file_reader import SteamshipFileReader
from llama_index_es.readers.string_iterable import StringIterableReader
from llama_index_es.readers.twitter import TwitterTweetReader
from llama_index_es.readers.weaviate.reader import WeaviateReader
from llama_index_es.readers.web import (
    BeautifulSoupWebReader,
    RssReader,
    SimpleWebPageReader,
    TrafilaturaWebReader,
)
from llama_index_es.readers.wikipedia import WikipediaReader
from llama_index_es.readers.youtube_transcript import YoutubeTranscriptReader
from llama_index_es.schema import Document

__all__ = [
    "WikipediaReader",
    "YoutubeTranscriptReader",
    "SimpleDirectoryReader",
    "JSONReader",
    "SimpleMongoReader",
    "NotionPageReader",
    "GoogleDocsReader",
    "MetalReader",
    "DiscordReader",
    "SlackReader",
    "WeaviateReader",
    "PineconeReader",
    "PsychicReader",
    "QdrantReader",
    "MilvusReader",
    "ChromaReader",
    "DeepLakeReader",
    "FaissReader",
    "MyScaleReader",
    "Document",
    "StringIterableReader",
    "SimpleWebPageReader",
    "BeautifulSoupWebReader",
    "TrafilaturaWebReader",
    "RssReader",
    "MakeWrapper",
    "TwitterTweetReader",
    "ObsidianReader",
    "GithubRepositoryReader",
    "MboxReader",
    "ElasticsearchReader",
    "SteamshipFileReader",
    "ChatGPTRetrievalPluginReader",
    "BagelReader",
    "HTMLTagReader",
    "ReaderConfig",
    "PDFReader",
    "DashVectorReader",
    "download_loader",
]
