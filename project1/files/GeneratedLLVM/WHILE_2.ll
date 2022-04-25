@.str = private unnamed_addr constant [5 x i8] c"%d;\0A\00", align 1
@.str1 = private unnamed_addr constant [20 x i8] c"i is %d ga naar 0: \00", align 1
@.str2 = private unnamed_addr constant [9 x i8] c"---> %d \00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %2, align 4
  br label %3

3:
  %4 = load i32, i32* %2, align 4
  %5 = icmp slt i32 %4, 5
  br i1 %5, label %6, label %30

6:
  %7 = load i32, i32* %2, align 4
  %8 = add i32 1, %7
  store i32 %8, i32* %2, align 4
  %9 = load i32, i32* %2, align 4
  %10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i64 0, i64 0), i32 %9)
  %11 = load i32, i32* %2, align 4
  %12 = icmp eq i32 %11, 4
  br i1 %12, label %13, label %25

13:
  %14 = load i32, i32* %2, align 4
  %15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.str1, i64 0, i64 0), i32 %14)
  br label %16

16:
  %17 = load i32, i32* %2, align 4
  %18 = icmp ne i32 %17, 0
  br i1 %18, label %19, label %24

19:
  %20 = load i32, i32* %2, align 4
  %21 = sub i32 %20, 1
  store i32 %21, i32* %2, align 4
  %22 = load i32, i32* %2, align 4
  %23 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str2, i64 0, i64 0), i32 %22)
  br label %16

24:
  br label %25

25:
  %26 = load i32, i32* %2, align 4
  %27 = icmp eq i32 %26, 0
  br i1 %27, label %28, label %29

28:
  br label %30

29:
  br label %3

30:
  ret i32 1
}

declare dso_local i32 @printf(i8*, ...)
