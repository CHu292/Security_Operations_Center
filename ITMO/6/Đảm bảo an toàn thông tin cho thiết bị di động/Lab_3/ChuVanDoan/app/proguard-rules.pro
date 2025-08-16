# Giữ lại các class của okhttp3 và không cảnh báo lỗi
-keep class okhttp3.** { *; }
-dontwarn okhttp3.**
-dontwarn javax.annotation.**
-dontwarn org.codehaus.mojo.animal_sniffer.*
-dontwarn okio.**

# Giữ lại các class của BouncyCastle
-keep class org.bouncycastle.** { *; }
-dontwarn org.bouncycastle.**

# Giữ lại các class của Conscrypt
-keep class org.conscrypt.** { *; }
-dontwarn org.conscrypt.**

# Giữ lại các class của OpenJSSE
-keep class org.openjsse.** { *; }
-dontwarn org.openjsse.**

# Nếu bạn dùng retrofit:
-keep class retrofit2.** { *; }
-dontwarn retrofit2.**

# Nếu bạn dùng Gson:
-keep class com.google.gson.** { *; }
-dontwarn com.google.gson.**

# Nếu bạn dùng Room:
-keep class androidx.room.** { *; }
-dontwarn androidx.room.**

# Giữ lại model dùng cho API / Room
-keepclassmembers class * {
    @retrofit2.http.* <methods>;
}
-keepattributes Signature
-keepattributes *Annotation*

# (Tuỳ chọn) Giữ nguyên tên class để dễ debug:
# -keepattributes SourceFile,LineNumberTable
