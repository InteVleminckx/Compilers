@.str = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 5, i32* %2, align 4
  store i32 10, i32* %3, align 4
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str, i64 0, i64 0))
  %5 = load i32, i32* %2, align 4
  %6 = icmp ne i32 %5, 4
  br i1 %6, label %7, label %9

7:
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str, i64 0, i64 0))
  br label %9

9:
  ret i32 1
}

declare dso_local i32 @printf(i8*, ...)
