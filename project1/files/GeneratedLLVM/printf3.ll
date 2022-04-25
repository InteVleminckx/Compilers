@.str = private unnamed_addr constant [7 x i8] c"%d%f%c\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str, i64 0, i64 0), i32 10, double 0.5, i32 37)
  ret i32 0
}

declare dso_local i32 @printf(i8*, ...)
