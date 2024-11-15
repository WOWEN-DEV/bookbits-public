import time
import sys

def typewriter_effect(text, delay=0.01):
    """Simulate a typewriter effect for the given text."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is printed.

def display_book_bits_info():
    """Display information about Book Bits with styled formatting."""
    header = r"""
██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
██████╔╝██║   ██║██║   ██║█████╔╝ 
██╔══██╗██║   ██║██║   ██║██╔═██╗ 
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                  
██████╗ ██╗████████╗███████╗      
██╔══██╗██║╚══██╔══╝██╔════╝      
██████╔╝██║   ██║   ███████╗      
██╔══██╗██║   ██║   ╚════██║      
██████╔╝██║   ██║   ███████║      
╚═════╝ ╚═╝   ╚═╝   ╚══════╝ 
.                           
|                           
|-. . .                     
| | | |                     
`-' `-|                     
    `-'                     
,   .  ,-.  ,   . ,--. .  . 
| . | /   \ | . | |    |\ | 
| ) ) |   | | ) ) |-   | \| 
|/|/  \   / |/|/  |    |  | 
' '    `-'  ' '   `--' '  '                            
                                           
"""
    info = """
📚 Book Bits - Instant Audiobook for Every Book, in Every Language

Turn Your Books into Bit-Sized Professional Audio

Book Bits automates ebooks in EPUB format to audiobooks using AI tech-
nology. With a single click, you can transform any ebook into a profe-
ssional audiobook experience, enabling users to listen in their prefe-
rred language through automatic translation. This feature makes conte-
nt accessible across languages, providing a seamless reading experien-
ce for diverse audiences.

👉 Features:
    • AI-Powered Audiobook Creation: Automatically transform ebooks 
      (EPUB format) into professional-grade audiobooks with a single 
      click.
    • Multilingual Support: Listen to the book in your preferred lang-
      uage with seamless automatic AI translation.
    • Accessibility Across Languages: Enhance accessibility by bre-
      aking language barriers, making content available to diverse 
      audiences.
    • Effortless User Experience: Enjoy a smooth and intuitive process 
      for converting and accessing audiobooks.

Book Bits is built by Emma Hager (@uchusei), founder of WOWEN.

Connect with WOWEN
• Website: wowen.tech
• Email: emma@wowen.tech

About WOWEN
WOWEN is not just a company; we are a creative powerhouse with exper-
tise in full-stack development, FemTech, publishing, UX, design, and 
marketing. We have a unique ability to transform high-level strategy 
into practical implementation at the intersection of business develop-
ment, communication, and technology.

"""
    # Display the header with some animation
    typewriter_effect(header, delay=0.01)
    print()
    # Display the info section
    typewriter_effect(info, delay=0.03)

if __name__ == "__main__":
    display_book_bits_info()