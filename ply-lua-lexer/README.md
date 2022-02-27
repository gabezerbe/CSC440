# ply-lua-lexer

## Usage

### lexer.py

A lua lexer built with Python's PLY library. lexer.py should be able to tokenize most if not all tokens one could use in the Lua language.

Uncomment line 71 through 81 to see terminal output

Run 
```
py lexer.py lex.lua
``` 
to produce the output of the lua lexer, 'lex.lua' being a set of lua input tokens for the lexer to attempt to tokenize

### parser.py

A lua parser built with Python's PLY library. parser.py is intended to be able to parse variable assignments and basic loops but currently errors out when reaching the 
```
while (x) do
``` 
loop

Run 
```
py lexer.py parse.lua
``` 
to produce the output of the parser. 'parse.lua' being a basic lua script for the parser to attempt to parse