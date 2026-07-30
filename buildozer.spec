[app]

title = Doctor Frio
package.name = doctorfrio
package.domain = org.doctorfrio

source.dir =.
source.include_exts = py,png,jpg,jpeg
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow
orientation = portrait
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1