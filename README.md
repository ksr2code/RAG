# RAG Learning Resources

## 1. RAG & Information Retrieval Concepts

### YouTube Videos

| Topic | Link |
|-------|------|
| 3Blue1Brown - Attention in Transformers, Visually Explained | https://www.youtube.com/watch?v=eMlx5fFNoYw |
| Andrej Karpathy - Let's build GPT: from scratch | https://www.youtube.com/watch?v=kCc8FmEb1nY |
| Andrej Karpathy - Intro to Large Language Models | https://www.youtube.com/watch?v=zjkBMFhNj_g |
| James Briggs - BM25 Explained: Best Matching Algorithm for Search | https://www.youtube.com/watch?v=He08gVBH0LE |
| James Briggs - RAG Fundamentals | https://www.youtube.com/watch?v=wd7TZaXJMro |
| Fireship - RAG: Retrieval-Augmented Generation in 100 Seconds | https://www.youtube.com/watch?v=T-D1KVIuvjA |

### Articles & Docs

| Topic | Link |
|-------|------|
| TF-IDF (Wikipedia) | https://en.wikipedia.org/wiki/Tf%E2%80%93idf |
| BM25 / Okapi BM25 (Wikipedia) | https://en.wikipedia.org/wiki/Okapi_BM25 |
| LangChain - RAG Tutorial | https://python.langchain.com/docs/tutorials/rag/ |
| Pinecone - What is RAG? | https://www.pinecone.io/learn/retrieval-augmented-generation/ |
| Manning - Introduction to Information Retrieval (Free Online Book) | https://nlp.stanford.edu/IR-book/ |

---

## 2. Required Libraries (Per Subject)

### BM25 / TF-IDF

| Resource | Link |
|----------|------|
| bm25s - Fast BM25 in Python (GitHub) | https://github.com/xhluca/bm25s |
| bm25s - PyPI | https://pypi.org/project/bm25s/ |
| scikit-learn TfidfVectorizer Docs | https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html |
| James Briggs - TF-IDF with Python | https://www.pinecone.io/learn/tf-idf-information-retrieval/ |

### Hugging Face Transformers (Qwen3-0.6B)

| Resource | Link |
|----------|------|
| Transformers Quickstart | https://huggingface.co/docs/transformers/quicktour |
| Qwen3-0.6B Model Card | https://huggingface.co/Qwen/Qwen3-0.6B |
| AutoModelForCausalLM Docs | https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForCausalLM |
| AutoTokenizer Docs | https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoTokenizer |
| Generation Strategies (blog) | https://huggingface.co/blog/how-to-generate |

### Python Fire (CLI - Required)

| Resource | Link |
|----------|------|
| Python Fire GitHub | https://github.com/google/python-fire |
| Python Fire Guide & Docs | https://github.com/google/python-fire/blob/master/docs/guide.md |
| Python Fire Using a CLI | https://github.com/google/python-fire/blob/master/docs/using-cli.md |

### tqdm (Progress Bars - Required)

| Resource | Link |
|----------|------|
| tqdm Official Docs | https://tqdm.github.io/ |
| tqdm GitHub | https://github.com/tqdm/tqdm |

---

## 3. Chunking Strategies

### Python Code Chunking (AST-based)

| Resource | Link |
|----------|------|
| Python `ast` Module Docs | https://docs.python.org/3/library/ast.html |
| Green Tree Snakes - AST Tutorial | https://greentreesnakes.readthedocs.io/ |
| Real Python - Understanding the AST | https://realpython.com/abstract-syntax-tree-python/ |

### Text / Markdown Chunking

| Resource | Link |
|----------|------|
| LangChain Text Splitters Docs | https://python.langchain.com/docs/concepts/text_splitters/ |
| RecursiveCharacterTextSplitter | https://python.langchain.com/docs/how_to/recursive_text_splitter/ |

---

## 4. Evaluation Metrics

| Resource | Link |
|----------|------|
| Recall@k Explained (Pinecone) | https://www.pinecone.io/learn/offline-evaluation/ |
| BEIR Benchmark - Information Retrieval Metrics | https://arxiv.org/abs/2104.08663 |

---

## 5. YouTube Channels (General Reference)

| Channel | Focus | Link |
|---------|-------|------|
| James Briggs | Vector search, RAG, NLP | https://www.youtube.com/@jamesbriggs |
| Andrej Karpathy | Neural networks, LLMs from scratch | https://www.youtube.com/@AndrejKarpathy |
| 3Blue1Brown | Math & ML visualizations | https://www.youtube.com/@3blue1brown |
| Fireship | Quick tech overviews | https://www.youtube.com/@Fireship |
| StatQuest with Josh Starmer | Statistics & ML fundamentals | https://www.youtube.com/@statquest |

---

## 6. Project pre discovery steps

```
Day 1: BM25 / TF-IDF (Wikipedia + James Briggs BM25 video)
       + Pydantic quickstart docs

Day 2: HuggingFace Transformers quickstart
       + Load Qwen3-0.6B locally, try a simple prompt

Day 3: Python ast module + chunking strategies
       + Python Fire README + tqdm examples

Day 4: Start coding
```
