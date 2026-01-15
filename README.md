## 🔭 Radar: Research Intelligence Agent

> Automatically discover, analyze, and translate cutting-edge AI research from ArXiv into actionable insights.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-green.svg)](https://github.com/langchain-ai/langgraph)
[![Claude](https://img.shields.io/badge/Claude-Sonnet%204-purple.svg)](https://www.anthropic.com/claude)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

### **🎯 What is Radar?**

Radar is an intelligent agent system that bridges the gap between cutting-edge AI research and practical understanding. It automatically:

1. **Discovers** latest papers from ArXiv (AI/ML categories)
2. **Analyzes** technical content using LangGraph agents
3. **Translates** complex research into accessible explanations
4. **Maps** innovations to real-world applications

**Built for:** Product managers, investors, students, and professionals who need to stay current with AI research without a PhD.

### **📊 System Architecture**

![Agent Pipeline](docs/architecture.md)
```
ArXiv API → PDF Processing → Paper Analyzer → Simplifier → Structured Output
                                    ↓              ↓
                            Technical Insights  Accessible Explanations
```

**[View Full Architecture →](docs/architecture.md)**

### **✨ Key Features**

- **Automated Discovery**: Searches ArXiv daily for new AI/ML papers
- **Intelligent Analysis**: Multi-agent pipeline extracts key insights
- **Accessible Translation**: Converts jargon into plain language
- **Structured Output**: Clean, scannable format (Summary → Challenge → Solution → Technical Points)
- **Production-Ready**: 100% success rate on processing, ~60s per paper

### **🚀 Example Output**

**Input:** Dense 13-page academic paper on ensemble decoding  
**Output:** Clear 2-minute read with context and practical implications

**[See Before/After Comparison →](docs/example-output.md)**

### **🏗️ Tech Stack**

| Component | Technology |
|-----------|-----------|
| **Orchestration** | LangGraph |
| **LLM** | Claude Sonnet 4 (Anthropic) |
| **PDF Processing** | PyMuPDF |
| **Data Source** | ArXiv API |
| **Storage** | JSON/CSV |

### **📁 Project Structure**
```
radar/
├── notebooks/           # Development notebooks
│   ├── 01_arxiv_exploration.ipynb
│   ├── 02_paper_processing.ipynb
│   └── 03_agent_prototype.ipynb
├── src/                # Production code
│   ├── agents/        # LangGraph agent definitions
│   └── utils/         # Helper functions
├── data/
│   ├── raw/           # Downloaded PDFs
│   └── processed/     # Agent outputs
└── docs/              # Documentation & examples
```

## 🔧 Installation
```bash
# Clone repository
git clone https://github.com/Dhruv-baner/radar.git
cd radar

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up API key
cp .env.example .env
# Add your Anthropic API key to .env
```

### **💻 Usage**

**Run Notebooks**
```bash
jupyter notebook notebooks/
```

**Process Papers Programmatically**
```python
from src.agents import paper_analyzer_agent, simplifier_agent

# Load paper
paper_text = load_paper("paper.pdf")

# Run analysis
result = analyze_and_simplify(paper_text)

print(result['two_line_summary'])
```

### 🎓 About

**Built by:** Dhruv Banerjee  
**Goal:** Make AI research accessible and demonstrate agentic system design

---

**Radar** - *Detecting emerging AI breakthroughs before they hit the mainstream*