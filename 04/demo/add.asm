// add.asm
// RAM[2] = RAM[0] + RAM[1] + 17
// 例如：首先设置 R0=10, R1=10, 则 R2=37

// D = RAM[0]
@R0
D=M

// D = D + RAM[1]
@R1
D=D+M

// D = D + 17
@17
D=D+A

// RAM[2] = D
@R2
M=D

(END)
@END
0;JMP
