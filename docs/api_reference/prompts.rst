.. _Prompt-Templates:

Prompt Templates
=================

These are the reference prompt templates.

We first show links to default prompts.

We then show the base prompt template class and its subclasses.

Default Prompts
^^^^^^^^^^^^^^^^^


* `Completion prompt templates <https://github.com/jerryjliu/llama_index_es/blob/main/llama_index_es/prompts/default_prompts.py>`_.
* `Chat prompt templates <https://github.com/jerryjliu/llama_index_es/blob/main/llama_index_es/prompts/chat_prompts.py>`_.
* `Selector prompt templates <https://github.com/jerryjliu/llama_index_es/blob/main/llama_index_es/prompts/default_prompt_selectors.py>`_.



Prompt Classes
^^^^^^^^^^^^^^^^^

.. autopydantic_model:: llama_index_es.prompts.base.BasePromptTemplate

.. autopydantic_model:: llama_index_es.prompts.base.PromptTemplate

.. autopydantic_model:: llama_index_es.prompts.base.ChatPromptTemplate

.. autopydantic_model:: llama_index_es.prompts.base.SelectorPromptTemplate

.. autopydantic_model:: llama_index_es.prompts.base.LangchainPromptTemplate


Subclass Prompts (deprecated)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Deprecated, but still available for reference at `this link <https://github.com/jerryjliu/llama_index_es/blob/113109365b216428440b19eb23c9fae749d6880a/llama_index_es/prompts/prompts.py>`_.
