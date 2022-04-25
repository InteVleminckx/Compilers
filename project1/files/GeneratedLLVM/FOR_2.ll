@.str = private unnamed_addr constant [18 x i8] c"a = %d --> b's: |\00", align 1
@.str1 = private unnamed_addr constant [6 x i8] c" %d |\00", align 1
@.str2 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %2, align 4
  br label %3

3:
  %4 = load i32, i32* %2, align 4
  %5 = icmp slt i32 %4, 10
  br i1 %5, label %6, label %22

6:
  %7 = load i32, i32* %2, align 4
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([18 x i8], [18 x i8]* @.str, i64 0, i64 0), i32 %7)
  %9 = alloca i32, align 4
  store i32 0, i32* %9, align 4
  br label %10

10:
  %11 = load i32, i32* %9, align 4
  %12 = icmp slt i32 %11, 10
  br i1 %12, label %13, label %18

13:
  %14 = load i32, i32* %9, align 4
  %15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str1, i64 0, i64 0), i32 %14)
  %16 = load i32, i32* %9, align 4
  %17 = add i32 1, %16
  store i32 %17, i32* %9, align 4
  br label %10

18:
  %19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str2, i64 0, i64 0))
  %20 = load i32, i32* %2, align 4
  %21 = add i32 1, %20
  store i32 %21, i32* %2, align 4
  br label %3

22:
  ret i32 0
}

declare dso_local i32 @printf(i8*, ...)
