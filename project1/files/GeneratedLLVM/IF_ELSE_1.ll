@.str = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1
@.str1 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  store i32 5, i32* %2, align 4
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str, i64 0, i64 0))
  %4 = load i32, i32* %2, align 4
  %5 = icmp eq i32 %4, 5
  br i1 %5, label %6, label %8

6:
  %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str, i64 0, i64 0))
  br label %10

8:
  %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str1, i64 0, i64 0))
  br label %10

10:
  ret i32 1
}

declare dso_local i32 @printf(i8*, ...)
