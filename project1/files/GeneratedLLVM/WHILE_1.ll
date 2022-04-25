@.str = private unnamed_addr constant [5 x i8] c"%d;\0A\00", align 1
@.str1 = private unnamed_addr constant [4 x i8] c"%s\0A\00", align 1
@.str2 = private unnamed_addr constant [10 x i8] c"Reached 4\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %2, align 4
  br label %3

3:
  %4 = load i32, i32* %2, align 4
  %5 = icmp slt i32 %4, 5
  br i1 %5, label %6, label %16

6:
  %7 = load i32, i32* %2, align 4
  %8 = add i32 1, %7
  store i32 %8, i32* %2, align 4
  %9 = load i32, i32* %2, align 4
  %10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i64 0, i64 0), i32 %9)
  %11 = load i32, i32* %2, align 4
  %12 = icmp eq i32 %11, 4
  br i1 %12, label %13, label %15

13:
  %14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str1, i64 0, i64 0), i8* getelementptr inbounds ([10 x i8], [10 x i8]* @.str2, i64 0, i64 0))
  br label %15

15:
  br label %3

16:
  ret i32 1
}

declare dso_local i32 @printf(i8*, ...)
