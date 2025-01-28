# brainrot-summarizer

Turn your boring documents into Gen Z summaries!

## Installation

1. Clone the repository

```bash
git clone https://github.com/baranbingol1/brainrot-summarizer.git
cd brainrot-summarizer
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

## Usage

```bash
python create_brainrot.py --document your_document.pdf --out output.mp3
```

### Available Options:

--document: Path to input PDF file (required)
--out: Path for output audio file (required)
--voice: ElevenLabs voice model to use (defaults to Brian)
