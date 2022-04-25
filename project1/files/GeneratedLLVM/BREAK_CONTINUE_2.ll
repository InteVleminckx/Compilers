@.str = private unnamed_addr constant [15 x i8] c"i: %d, j: %d \0A\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %2, align 4
  store i32 0, i32* %3, align 4
  br label %4

4:
  %5 = load i32, i32* %2, align 4
  %6 = icmp slt i32 %5, 10
  br i1 %6, label %7, label %20

7:
  br label %8

8:
  %9 = load i32, i32* %3, align 4
  %10 = icmp slt i32 %9, 10
  br i1 %10, label %11, label %17

11:
  %12 = load i32, i32* %2, align 4
  %13 = load i32, i32* %3, align 4
  %14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.str, i64 0, i64 0), i32 %12, i32 %13)
  %15 = load i32, i32* %3, align 4
  %16 = add i32 1, %15
  store i32 %16, i32* %3, align 4
  br label %8

17:
  store i32 0, i32* %3, align 4
  %18 = load i32, i32* %2, align 4
  %19 = add i32 1, %18
  store i32 %19, i32* %2, align 4
  br label %4

20:
  ret i32 0
}

declare dso_local i32 @printf(i8*, ...)
