@.str = private unnamed_addr constant [8 x i8] c"%s %s!\0A\00", align 1
@.str1 = private unnamed_addr constant [6 x i8] c"Hello\00", align 1
@.str2 = private unnamed_addr constant [6 x i8] c"World\00", align 1

define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str, i64 0, i64 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str1, i64 0, i64 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str2, i64 0, i64 0))
  ret i32 0
}

declare dso_local i32 @printf(i8*, ...)
