import argparse
from summarizer import process_document
from create_audio import create_audio
import os

def main():

    parser = argparse.ArgumentParser(description='Create brainrot audio from PDF document')
    parser.add_argument('--document', type=str, required=True, help='Path to PDF document')
    parser.add_argument('--out', type=str, required=True, help='Output audio file path')
    parser.add_argument('--voice', type=str, default='Brian', help='Voice to use (default: Brian)')
    
    args = parser.parse_args()

    try:
        if not os.path.exists(args.document):
            raise FileNotFoundError(f"Document not found: {args.document}")

        print("Processing document...")
        summary = process_document(args.document)

        print("Generating audio...")
        create_audio(summary, args.voice, args.out)

        print(f"Successfully created brainrot audio at: {args.out}")

    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()