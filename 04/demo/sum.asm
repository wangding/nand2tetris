// 1+...+10
// R1=55

// i=1
@i
M=1

// sum=0
@sum
M=0

(LOOP)
// if (i-10)>0 goto STOP
@i
D=M       // D=i
@10
D=D-A     // D=i-10
@STOP
D;JGT

// sum=sum+i
@sum
D=M       // D=sum
@i
D=D+M     // D=sum+i
@sum
M=D       // sum=sum+i

// i=i+1
@i
M=M+1

// Goto LOOP
@LOOP
0;JMP

(STOP)
// R1 = sum
@sum
D=M
@R1
M=D

(END)
@END
0;JMP