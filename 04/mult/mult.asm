// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// function: R2 = R0 * R1
// 例如：R0=2, R1=3, R2=6

// i = 0
@i
M=0

// sum = 0
@sum
M=0

// (LOOP)
(LOOP)

//    if R0 - i == 0 then Goto STOP
@R0
D=M
@i
D=D-M
@STOP
D;JEQ

//    sum = sum + R1
@sum
D=M
@R1
D=D+M
@sum
M=D

//    i = i+1
@i
M=M+1

//    Goto LOOP
@LOOP
0;JMP

// (STOP)
(STOP)
//    R2 = sum
@sum
D=M
@R2
M=D

(END)
@END
0;JMP