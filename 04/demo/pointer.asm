// pointer.asm
// 从基址 R1 开始，将前面 R0 个字段置为 -1
// 例如：首先设置 RO = 3

// n = 0
@n
M=0

(LOOP)
// if n==R0 goto END
@n
D=M
@R0
D=D-M
@END
D;JEQ

// *(R1 + n) = -1
@1
D=A
@n
A=D+M
M=-1

// n = n + 1
@n
M=M+1

// goto LOOP
@LOOP
0;JMP

(END)
@END
0;JMP