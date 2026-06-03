[app]

# (str) Title of your application
# သင့် App ရဲ့ နာမည် (ပြောင်းလဲနိုင်ပါတယ်)
title = Myanmar AI Human Brain

# (str) Package name
# App ရဲ့ Package နာမည် (စာလုံးအသေးပဲ သုံးရပါမယ်)
package.name = myanmar_ai_human_brain

# (str) Package domain (needed for android packaging)
package.domain = org.kyawpaingko

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# App အတွက် လိုအပ်တဲ့ Python Libraries များ (kivy အပြင် အခြားလိုတာရှိရင် ကော်မာခံပြီး ထည့်ပါ)
requirements = python3,kivy

# (str) Supported orientations (valid options are: landscape, portrait, all)
# App ဖွင့်ရင် စခရင်ကို ဒေါင်လိုက်လား၊ အလျားလိုက်လား သတ်မှတ်တာပါ
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific configuration
# =============================================================================

# (list) Permissions
# App က တောင်းမယ့် Permissions များ (ဥပမာ- အင်တာနက် သုံးချင်ရင် INTERNET ကို # ဖြုတ်ပေးပါ)
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
# Android API Level သတ်မှတ်ချက် (33 သို့မဟုတ် 34 က လက်ရှိ အဆင်ပြေဆုံးပါ)
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Type of builds to run (debug or release)
android.release = False

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
