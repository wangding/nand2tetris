// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// addr = @SCREEN base address
@SCREEN
D=A
@addr
M=D

// (LOOP)
(LOOP)

//    if addr - @SCREEN - 100 = 0 then Goto END
@addr
D=M
@SCREEN
D=D-A
@100
D=D-A
@END
D;JEQ

//    set addr color black
@addr
A=M
M=1

//    addr = addr + 1
@addr
M=M+1

// Goto LOOP
@LOOP
0;JMP

(END)
@END
0;JMP