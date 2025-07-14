// 循环读取键盘

(LOOP)
@KBD
D=M
@R0
M=D
@LOOP
0;JMP

(END)
@END
0;JMP