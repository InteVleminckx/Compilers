@.str = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %2, align 4
  br label %3

3:
  %4 = load i32, i32* %2, align 4
  %5 = icmp slt i32 %4, 10
  br i1 %5, label %6, label %15

6:
  %7 = load i32, i32* %2, align 4
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i64 0, i64 0), i32 %7)
  %9 = load i32, i32* %2, align 4
  %10 = icmp eq i32 %9, 5
  br i1 %10, label %11, label %12

11:
  br label %15

12:
  %13 = load i32, i32* %2, align 4
  %14 = add i32 1, %13
  store i32 %14, i32* %2, align 4
  br label %3

15:
  ret i32 0
}

declare dso_local i32 @printf(i8*, ...)
