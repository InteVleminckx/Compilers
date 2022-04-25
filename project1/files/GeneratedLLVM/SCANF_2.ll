@.str = private unnamed_addr constant [19 x i8] c"Enter two numbers:\00", align 1
@.str1 = private unnamed_addr constant [5 x i8] c"%d%d\00", align 1
@.str2 = private unnamed_addr constant [7 x i8] c"%d; %d\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([19 x i8], [19 x i8]* @.str, i64 0, i64 0))
  %5 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str1, i64 0, i64 0), i32* %2, i32* %3)
  %6 = load i32, i32* %2, align 4
  %7 = load i32, i32* %3, align 4
  %8 = icmp eq i32 %6, %7
  br i1 %8, label %9, label %13

9:
  %10 = load i32, i32* %2, align 4
  %11 = load i32, i32* %3, align 4
  %12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str2, i64 0, i64 0), i32 %10, i32 %11)
  br label %13

13:
  ret i32 1
}

declare dso_local i32 @printf(i8*, ...)
declare dso_local i32 @__isoc99_scanf(i8*, ...)
