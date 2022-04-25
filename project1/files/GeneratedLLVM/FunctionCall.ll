@.str = private unnamed_addr constant [7 x i8] c"Hello \00", align 1
@.str1 = private unnamed_addr constant [7 x i8] c"World\0A\00", align 1

define dso_local void @f() {
  %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str, i64 0, i64 0))
  ret void 
}


define dso_local void @g() {
  %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str1, i64 0, i64 0))
  call void @f()
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str1, i64 0, i64 0))
  ret void
}


define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  call void @f()
  call void @g()
  ret i32 1
}

declare dso_local i32 @printf(i8*, ...)
