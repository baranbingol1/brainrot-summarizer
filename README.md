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

## Example

Input : [Attention Paper](https://arxiv.org/abs/1706.03762)

Output (text) :

Yo, so this paper *Attention Is All You Need* is like the ultimate glow-up for neural networks. They dropped the Transformer, which is basically the GOAT of sequence transduction no cap! It's all about that attention magic, ditching the boring old recursions and convolutions like they're cheugy. 

Now, it's all fast and furious, hitting those training times like a boss. Peep these stats: it's flexing a 28.4 BLEU on English-to-German and a whopping 41.8 BLEU on English-to-French. Talk about bussin�! Plus, it's slaying in English constituency parsing too. 

The whole vibe is stacked self-attention and point-wise feed-forward layers, like a whole squad of multi-head attention just vibin' together. This setup is peak computational efficiency and translation quality, throwing shade at the old models. Pretty sus if you ask me, but we stan it! Periodt!

