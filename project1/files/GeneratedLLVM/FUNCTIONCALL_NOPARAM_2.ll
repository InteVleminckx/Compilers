@.str = private unnamed_addr constant [3 x i8] c"a\0A\00", align 1
@.str1 = private unnamed_addr constant [3 x i8] c"b\0A\00", align 1
@.str2 = private unnamed_addr constant [3 x i8] c"c\0A\00", align 1

define dso_local void @a() {
  %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i64 0, i64 0))
  ret void
}


define dso_local void @b() {
  %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str1, i64 0, i64 0))
  call void @a()
  ret void
}


define dso_local void @c() {
  %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str2, i64 0, i64 0))
  call void @b()
  call void @a()
  ret void
}


define dso_local i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  call void @a()
  call void @b()
  call void @c()
  ret i32 1
}

declare dso_local i32 @printf(i8*, ...)
