from os.path import exists as file_exists
import sys

LEGAL_OPS = (4, 5, 23, 39,\
             40, 62, 68, 81)

THE_TABLE = ( (1, 0, 0), (1, 0, 2),\
             (2, 2, 1) )

MEM_SIZE  = 3 ** 10
CHAR_SET  = '5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1C' \
            'B6v^=I_0/8|jsb9m<.TVac`uY*MK\'X~xDl}REokN:#?G"i@'

print_op = 5
input_op = 23

def write_to_stdout(m):
    sys.stdout.write(m)
    sys.stdout.flush()

def the_op(n1, n2):
    return sum(THE_TABLE[n2 // 3 ** i % 3][n1 // 3 ** i % 3] * 3 ** i for i in range(10))

def rot_right(n):
    return (n % 3) * 3 ** 9 + n // 3

def init(src, mem):
    c = 0
    for i in src:
        if i.isspace():
            continue
        if (c + ord(i)) % 94 not in LEGAL_OPS:
            sys.exit('[error] invalid char in input file')
        if c == MEM_SIZE:
            sys.exit('[error] input file too long')
        
        mem[c] = ord(i)
        c += 1

    for i in range(c, MEM_SIZE):
        mem[i] = the_op( mem[i - 1], mem[i - 2] )

def run(mem):
    a = 0
    c = 0
    d = 0

    while True:
        op = ( c + mem[c] ) % 94

        if op == 4:
            c = mem[d]
            
        if op == print_op:
            write_to_stdout(chr(a % 256))
            
        if op == input_op:
            a = ord(sys.stdin.read(1))
            
        if op == 39:
            a = mem[d] = rot_right(mem[d])
            
        if op == 40:
            d = mem[d]
            
        if op == 62:
            a = mem[d] = the_op(a, mem[d])
            
        if op == 81:
            return

        mem[c] = ord( CHAR_SET[ mem[c] - 33 ] )
        c = (c + 1) % MEM_SIZE
        d = (d + 1) % MEM_SIZE

if __name__ == '__main__':
    if len(sys.argv) < 2 or not file_exists(sys.argv[1]):
        sys.exit('[error] no valid argument given\n'
                 '[usage] python malbolge.py <path-to-your-malbolge-file> spesification(optional)')

    if len(sys.argv) > 2 and sys.argv[2] == 'specification':
        print_op = 23
        input_op = 5
        write_to_stdout('[message] specification mode enabled\n')

    with open(sys.argv[1]) as file:
        source = file.read()
    
    mem = [0] * MEM_SIZE
    init(source, mem)
    run(mem)

    write_to_stdout('\n[message] execution completed\n')
    sys.exit(0)
