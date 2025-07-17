import os
from caption_model import generate_caption

def main():
    print(" Image Captioning AI (Python Only)")
    print("-----------------------------------")

    while True:
        img_path = input("\n Enter image file path (or type 'exit' to quit): ").strip()

        if img_path.lower() == 'exit':
            print("Exiting... Have a great day!")
            break

        if not os.path.isfile(img_path):
            print("Error: File does not exist. Try again.")
            continue

        print("\nGenerating caption, please wait...")
        caption = generate_caption(img_path)
        print(f"\nCaption: {caption}")

if __name__ == '__main__':
    main()
