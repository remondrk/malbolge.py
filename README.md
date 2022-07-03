Malbolge interpreter written in Python. <br>
[Malbolge](https://en.wikipedia.org/wiki/Malbolge) is an esoteric programming language designed to be impossible to program by humans.

## Usage
```console
python malbolge.py <path-to-your-malbolge-file> specification(optional)
```
Running the interpreter with 'specification' enables the 'specification mode' that is explained in the [notes](#notes) part

## Notes
In the original interpreter and the specification, instruction codes of input and output are reversed with respect to each other. This interpreter is based on the original interpreter, not the specification, unless 'specification mode' is enabled. Note that most of the malbolge code in the internet is written according to the original interpreter.

## References
[Malbolge - Esolang](https://esolangs.org/wiki/Malbolge) <br>
[Original interpreter and specifications](https://web.archive.org/web/20000815230017/http:/www.mines.edu/students/b/bolmstea/malbolge/)