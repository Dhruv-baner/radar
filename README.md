# Radar
An agentic system that tracks the latest academic research on AI and ML, providing industry-wise insights


### 🎯 Project Overview

This system automatically:
1. **Discovers** latest AI research from ArXiv
2. **Analyzes** technical content and methodology
3. **Simplifies** complex concepts into accessible explanations
4. **Maps** research to real-world industry use cases


### 🏗️ Architecture

**Agent Workflow:**
```
ArXiv Search → Paper Analysis → Simplification → Industry Matching
```

**Tech Stack:**
- **Orchestration:** LangGraph
- **LLM:** Claude (Anthropic)
- **Vector DB:** ChromaDB
- **API:** FastAPI
- **Frontend:** Gradio
- **Storage:** SQLite
