# Wikipedia Extractive Text Summarizer + Keywords Identification (entropy-based)
Uses Beautiful Soup to read Wiki pages, Gensim to summarize, NLTK to process, and extracts keywords based on entropy: **everything in one beautiful code**. I was looking for similar codes throughout Github but most of them were very difficult to understand and use. I'm building this repo to provide simple, yet effective solution in extractive summarization and keyword identification.

**Program works best for 300+ words summary.**

## License
Please follow license guidelines in usage. **GNU General Public License v3.0**

## Requirements
- Gensim
- NLTK
- and others 
  
I provided requirements.txt. Simply input command below in the terminal.
```
    pip install -r requirements.txt
```

## How to Use
``` 
    python summarize.py <wiki-url> <summary length>
```
output:

wiki-summarizer-----written-by-@brucewlee(github)

Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a business partnership. The company's first product is the Apple I, a computer designed and hand-built entirely by Wozniak. To finance its creation, Jobs sold his only motorized means of transportation, a VW Microbus, for a few hundred dollars, and Wozniak sold his HP-65 calculator for US$500 . Wozniak debuted the first prototype at the Homebrew Computer Club in July 1976. The Apple I was sold as a motherboard with CPU, RAM, and basic textual-video chips—a base kit concept which would not yet be marketed as a complete personal computer. It went on sale soon after debut for US$666.66 .:180 Wozniak later said he was unaware of the coincidental mark of the beast in the number 666, and that he came up with the price because he liked "repeating digits". During his keynote speech at the Macworld Expo on January 9, 2007, Jobs announced that Apple Computer, Inc. would thereafter be known as "Apple Inc.", because the company had shifted its emphasis from computers to consumer electronics. This event also saw the announcement of the iPhone and the Apple TV. The company sold 270,000 iPhone units during the first 30 hours of sales, and the device was called "a game changer for the industry". Apple would achieve widespread success with its iPhone, iPod Touch, and iPad products, which introduced innovations in mobile phones, portable music players, and personal computers respectively. Furthermore, by early 2007, 800,000 Final Cut Pro users were registered.

keywords:

'iphone', 'ipad', 'jobs', 'macintosh', 'stores'


## Examples
### Python (programming language) (300 words)
```
    python summarize.py https://en.wikipedia.org/wiki/Python_\(programming_language\) 300
```
output-summary:

Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica  in the Netherlands as a successor to the ABC language , capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. He now shares his leadership as a member of a five-person steering council. In January 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member "Steering Council" to lead the project. Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management. It also features dynamic name resolution , which binds method and variable names during program execution. Python's developers strive to avoid premature optimization, and reject patches to non-critical parts of the CPython reference implementation that would offer marginal increases in speed at the cost of clarity. When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. The long-term plan is to support gradual typing and from Python 3.5, the syntax of the language allows specifying static types but they are not checked in the default implementation, CPython. Examples of the use of this prefix in names of Python applications or libraries include Pygame, a binding of SDL to Python ; PyQt and PyGTK, which bind Qt and GTK to Python respectively; and PyPy, a Python implementation originally written in Python.

output-keywords:

'python', 'class', 'classes', 'division', 'round', 'type'


### Steve Jobs (350 words)
```
    python summarize.py https://en.wikipedia.org/wiki/Steve_Jobs 350
```
output-summary:

He worked closely with designer Jony Ive to develop a line of products that had larger cultural ramifications, beginning in 1997 with the "Think different" advertising campaign and leading to the iMac, iTunes, iTunes Store, Apple Store, iPod, iPhone, App Store, and the iPad. In 2001, the original Mac OS was replaced with a completely new Mac OS X , based on NeXT's NeXTSTEP platform, giving the OS a modern Unix-based foundation for the first time. 1931), grew up in Homs, Syria, and was born into an Arab Muslim household. While an undergraduate at the American University of Beirut, Lebanon, he was a student activist and spent time in prison for his political activities. He pursued a PhD at the University of Wisconsin, where he met Joanne Carole Schieble, a Catholic of Swiss and German descent. As a doctoral candidate, Jandali was a teaching assistant for a course Schieble was taking, although both were the same age. Mona Simpson, Jobs's biological sister, notes that her maternal grandparents were not happy that their daughter was dating a Muslim. Walter Isaacson, author of the Steve Jobs biography, additionally states that Schieble's father "threatened to cut Joanne off completely" if she continued the relationship. The location of the Los Altos home meant that Jobs would be able to attend nearby Homestead High School, which had strong ties to Silicon Valley. He began his first year there in late 1968 along with Bill Fernandez.  Neither Jobs nor Fernandez  came from engineering households and thus decided to enroll in John McCollum's "Electronics 1." McCollum and the rebellious Jobs  would eventually clash and Jobs began to lose interest in the class.

output-keywords:

'brennan', 'apple', 'macintosh', 'disney', 'next', 'ipod', 'jandali', 'wozniak'


### University of Pennsylvania (300 words)
```
    python summarize.py https://en.wikipedia.org/wiki/University_of_Pennsylvania 300
```
output-summary:

In 2019, the university had an endowment of $14.65 billion, the sixth-largest endowment of all colleges in the United States, as well as a research budget of $1.02 billion. The university's athletics program, the Quakers, fields varsity teams in 33 sports as a member of the NCAA Division I Ivy League conference.
As of 2018, distinguished alumni include three U.S. Supreme Court justices, 32 U.S. senators, 46 U.S. governors, 163 members of the U.S. House of Representatives, eight signers of the Declaration of Independence, 12 signers of the U.S. Constitution, 24 members of the Continental Congress, 14 foreign heads of state, and two presidents of the United States, including the incumbent, Donald Trump. As of October 2019, 36 Nobel laureates, 80 members of the American Academy of Arts and Sciences, 64 billionaires, 29 Rhodes Scholars, 15 Marshall Scholars, and 16 Pulitzer Prize winners have been affiliated with the university. Penn has three claims to being the first university in the United States, according to university archives director Mark Frazier Lloyd: the 1765 founding of the first medical school in America made Penn the first institution to offer both "undergraduate" and professional education; the 1779 charter made it the first American institution of higher learning to take the name of "University"; and existing colleges were established as seminaries. Penn's educational innovations include the nation's first medical school in 1765; the first university teaching hospital in 1874; the Wharton School, the world's first collegiate business school, in 1881; the first American student union building, Houston Hall, in 1896; the country's second school of veterinary medicine; and the home of ENIAC, the world's first electronic, large-scale, general-purpose digital computer in 1946.

output-keywords:

'rugby', 'team', 'football', 'research', 'programs', 'founder', 'school', 'cricket', 'located', 'former'
