@.str = private unnamed_addr constant [11 x i8] c"%d; %f; %c\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = alloca i32, align 4
  %3 = alloca float, align 4
  %4 = alloca i8, align 1
  store i32 5, i32* %2, align 4
  store float 0.5e+00, float* %3, align 4
  store i8 99, i8* %4, align 1
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.str, i64 0, i64 0), i32 5, double 0.5, i32 99)
  ret i32 0
}

declare dso_local i32 @printf(i8*, ...)
