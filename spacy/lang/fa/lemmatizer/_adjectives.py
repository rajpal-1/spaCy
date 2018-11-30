# coding: utf8
from __future__ import unicode_literals


ADJECTIVES = set(
    """
صفر
صفرم
صفر‌ام
یک
یکم
یک‌ام
اول
نخست
دو
دوم
دو‌ام
سه
سوم
چهار
چهارم
پنج
پنجم
پنج‌ام
شش
ششم
شش‌ام
هفت
هفتم
هفت‌ام
هشت
هشتم
هشت‌ام
نه
نهم
نه‌ام
ده
دهم
ده‌ام
یازده
یازدهم
یازده‌ام
دوازده
دوازدهم
دوازده‌ام
سیزده
سیزدهم
سیزده‌ام
چهارده
چهاردهم
چهارده‌ام
پانزده
پانزدهم
پانزده‌ام
پونزده
پونزدهم
پونزده‌ام
شانزده
شانزدهم
شانزده‌ام
شونزده
شونزدهم
شونزده‌ام
هفده
هفدهم
هفده‌ام
هجده
هجدهم
هجده‌ام
هیجده
هیجدهم
هیجده‌ام
نوزده
نوزدهم
نوزده‌ام
بیست
بیستم
بیست‌ام
سی
سی‌ام
چهل
چهلم
چهل‌ام
پنجاه
پنجاهم
پنجاه‌ام
شصت
شصتم
شصت‌ام
هفتاد
هفتادم
هفتاد‌ام
هشتاد
هشتادم
هشتاد‌ام
نود
نودم
نود‌ام
صد
صدم
یکصد
یکصدم
یک‌صد
یک‌صدم
دویست
دویستم
دویست‌ام
سیصد
سیصدم
سیصد‌ام
چهارصد
چهارصدم
چهارصد‌ام
پانصد
پانصدم
پانصد‌ام
پونصد
پونصدم
پونصد‌ام
ششصد
ششصدم
ششصد‌ام
شیشصد
شیشصدم
شیشصد‌ام
هفتصد
هفتصدم
هفتصد‌ام
هفصد
هفصدم
هفصد‌ام
هشتصد
هشتصدم
هشتصد‌ام
نهصد
نهصدم
نهصد‌ام
هزار
هزارم
هزار‌ام
میلیون
میلیونم
میلیون‌ام
میلیارد
میلیاردم
میلیارد‌ام
بیلیون
بیلیونم
بیلیون‌ام
بیلیارد
بیلیاردم
بیلیارد‌ام
تریلیون
تریلیونم
تریلیون‌ام
تریلیارد
تریلیاردم
تریلیارد‌ام
کوادریلیون
کوادریلیونم
کوادریلیون‌ام
کادریلیارد
کادریلیاردم
کادریلیارد‌ام
کوینتیلیون
کوینتیلیونم
کوینتیلیون‌ام
آبستن
آبکی
آبی
آب‌ندیده
آتی
آخته
آخر
آراسته
آرام
آرامش‌بخش
آرام‌بخشی
آرایشی
آرزومند
آرمانی
آرمیده
آزاد
آزادمنشی
آزاد‌ید
آزاردهنده
آزار‌دهنده
آزار‌دهندهٔ
آزرده
آزمایشگاهی
آسان
آسانگیر
آسمانی
آسوده
آسیایی
آسیب‌دیده
آسیب‌پذیر
آشامیدنی
آشفته
آشنا
آشنای
آشوب‌طلب
آشکار
آشکاری
آشکار‌شده
آفریقایی
آلاینده
آلمانی
آلوده
آلومینیومی
آماده
آمادهٔ
آماری
آمده
آمریکایی
آموزشی
آموزنده
آمیخته
آنالوگ
آنتی‌سپتیک
آنتی‌وایرال
آنی
آهنی
آورده
آویزان
آکادمیک
آکنده
آگاه
آینده
آینده‌نگر
آینه‌کردار
آیینی
ائتلافی
ابتدایی
ابداعی
ابدی
ابزار‌خورده
ابطال‌شدنی
ابله
اتفاقیه
اتمی
اثبات‌ناپذیر
اثرگذار
اثر‌گذار
اجبارآمیز
اجباری
اجتماعی
اجتماعی‌
اجدادی
اجدادی‌
اجرایی
اجمالی
احتمالی
احساساتی
احساسی
اختصاصی
اختلافی
اخلاقی
اخیر
اداری
ادبی
ادب‌شناس
ادراری
ادعایی
ادیب
ارائه‌شده
اراکی
ارتباطی
ارتجاعی
ارجمند
اردنی
اردو
ارزان
ارزشمند
ارزشمندی
ارزشگرایانه
ارزشی
ارزنده
ارزندهٔ
ارزی
ارزی‌
ارشد
ارضی
اروماتیک
اروپائی
اروپایی
ارگانیک
از‌بین‌برنده
از‌دست‌رفته
از‌هم‌گسسته
اساسی
اساطیری
استادانه
استالینیست
استامپی
استاندارد
استبدادی
استحاله
استخراجی
استخوانی
استراتژیک
استرالیایی
استقلال‌یافته
استوار
استیلیزه
اسرع
اسفل
اسف‌انگیز
اسلامگرای
اسلامی
اسلامی‌
اسلام‌گرا
اسلوموشن
اسمی
اسپانیایی
اشتباهی
اشرافی
اشغالگر
اشکانی
اصفهانی
اصلاحی
اصلاح‌طلب
اصلاح‌طلبانه
اصلاح‌گر
اصلاح‌گرا
اصلاح‌گرایانه
اصلی
اصولگرا
اصولی
اصیل
اضافه
اضافه‌تری
اضافی
اضطراری
اطلاعاتی
اطمینان‌بخش
اعتباری
اعتقادی
اعزامی
اعطایی
اعظم
اعلام‌شده
اعلای
اعم
اعمال‌شده
اغلب
افازیک
افراطی
افزایشی
افزوده
افزودهٔ
افزون
افسرده
افضل
افغانی
اقتصادی
اقصی
اقلیدسی
اقلیمی
التقاطی
التهابی
الجزایری
الحاقی
الزامی
الهی
الکترونیک
الکترونیکی
الکلی
الیت
امامی
امان
امانتدار
امانتی
امدادرسانی
امدادگر
امدادی
امروزی
امریکایی
امن
امنیتی
اموی
امکان‌پذیر
امیدوار
امیدوارکننده
انباشته
انبوه
انتخاباتی
انتخابی
انتخابیه
انتظامی
انتقادی
انجام‌شده
انجام‌گرفته
انحرافی
انداخته
اندوهناک
اندک
اندکی
اندیشمندی
اندیشگی
انرژی‌بخش
انرژی‌زا
انرژی‌زایی
انسانی
انسانیِ
انسان‌دوست
انعطاف‌ناپذیر
انفرادی
انفعالی
انقلابی
انکارناپذیر
انگاشته
انگشتری
انگلی
انگلیسی
انگیزشی
انیمیشنی
اهانت‌آمیز
اهانت‌آمیزی
اهدایی
اهلی
اهم
اول
اولی
اولیه
اوکراینی
اکبر
اکتشافی
اکتیو
اکثر
اکراه
اکرم
اکسیده
اکشن
اکلیلی
اکونومیک
ایالتی
ایتالیایی
ایجاد‌شده
ایداولوژیک
ایرانی
ایرانی‌
ایرانی‌نژاد
ایران‌زا
ایستاده
ایمانی
ایمنی
اینترنتی
باارزش
بااطلاع
باایمان
باتجربه
باتقوای
باحیا
باختری
بادی
بارانی
باردار
بارداری
بارزی
باریکی
باز
بازاری
بازشماری‌شده
بازمانده
بازنشسته
بازگشتی
باستان
باستانی
باشکوهی
باصفا
باطل
باطلی
باظرافت
باعث
باغی
باقی
باقیمانده
باقی‌مانده
بالاتری
بالادستی
بالای
بالایی
بالغ
بالقوه
بانشاط
بانکی
باوفا
باکتریایی
با‌ادب
با‌ارزش
با‌ارزشی
با‌اقتدار
با‌انصاف
با‌تجربه
با‌تدبیر
با‌سابقه
با‌شکوهی
با‌عزت
با‌فکر
با‌نمک
بجا
بحث‌انگیز
بحرانی
بحران‌ساز
بخشنده
بد
بدجنس
بدخط
بدخیم
بدنام
بدنی
بدگمان
بدی
بدیع
بدیعی
بدیل
بدیهی
برآورده
برادرانه
برافراشته
براق
برانداز
برانگیزاننده
برجسته
برجستهٔ
برجسته‌یی
برحذر
برخوردار
بردبار
برطرف
برعکس
برفکی
برق
برقرار
برنامه‌پرکن
برنده
برنزی
برهم
برهنه
برهنه‌
بروسلایی
برون‌زا
برون‌ساحلی
برون‌مرزی
برپا
برگ
برگردانده
برگزار
برگزیده
برگشتی
برگ‌ریزان
بریده
بزرگ
بزرگش
بزرگوار
بزرگی
بستری
بسته
بسنده
بسیار
بسیاری
بشاش
بشردوست
بشردوستانه
بشقابی
بصری
بطای
بعد
بعدی
بعید
بلند
بلندمدت
بلندپایه
بلندی
بلورینی
بلوچ
بلیغ
بندری
بنیانی
به
بهاری
بهتان
بهتری
بهت‌انگیز
بهت‌زده
بهداشتی
بهره‌مند
بهشتی
بهینه
بهینه‌ساز
به‌روز
به‌قاعده
به‌موقع
به‌نام
به‌کار‌رفته
بوده
بومی
بچه‌دار
بیابانی
بیدار
بیرونی
بیزار
بیستم
بیش
بیشتری
بیشماری
بیضی‌شکل
بیمار
بیماری
بیماری‌زا
بیماری‌زای
بین‌الملل
بین‌المللی
بیهوده
بیوشیمیایی
بیکار
بیگانه
بیگاه
بیگناه
بی‌آب
بی‌آزار
بی‌اثر
بی‌اختیار
بی‌ارزش
بی‌اساس
بی‌اطلاع
بی‌اعتبار
بی‌انتها
بی‌بهره‌
بی‌تاب
بی‌تفاوت
بی‌ثبات
بی‌ثمر
بی‌جان
بی‌حدومرز
بی‌حساب
بی‌خار
بی‌خبر
بی‌خطر
بی‌خود
بی‌دریغ
بی‌دفاع
بی‌ربط
بی‌رویه
بی‌زار
بی‌زبانی
بی‌سابقه
بی‌سروته‌شده
بی‌سواد
بی‌شاخ
بی‌شمار
بی‌صاحب
بی‌طاقت
بی‌طرف
بی‌طپش
بی‌فایده
بی‌مسئل
بی‌معنا
بی‌معنی
بی‌مهار
بی‌مورد
بی‌نتیجه
بی‌نظیر
بی‌نهایت
بی‌نی
بی‌نیاز
بی‌پاسخ
بی‌پایان
بی‌پایه
بی‌پروا
بی‌کار
بی‌گناه
بی‌گناهی
تأثیربرانگیز
تأثیرگذار
تألیفی
تئوریک
تابستانی
تابعه
تابناک
تاریخی
تاریک
تاریکی
تازه
تازه‌تری
تازه‌داماد
تازه‌کار
تازه‌یی
تایوانی
تایپه
تاییدشده
تبتی
تبلیغاتی
تبلیغاتیِ
تبهکاری
تجارتی
تجاری
تجدیدنظرطلب
تجدیدنظر‌طلبانه
تجدید‌کننده
تجربه‌شده
تجربی
تجسمی
تجملی
تجویزی
تحتانی
تحریریه
تحریک‌کننده
تحسین‌برانگیز
تحسین‌کننده
تحصیلی
تحصیل‌کرده
تحقیقاتی
تحقیقی
تحلیلی
تحمیلی
تخصصی
تخیلی
تخیلی‌
تدارکاتی
تدریجی
ترافیکی
ترانزیتی
ترسان
ترسناک
ترسو
ترشحی
ترفیع
ترقیخواهانه
ترقی‌خواهانه
تزئینی
تزریقی
تشخیصی
تشریفاتی
تشنه
تشکیلاتی
تشکیلاتی‌
تصادفی
تصفیه‌کننده
تصویبی
تصویب‌شده
تصویری
تضییع‌کننده
تعجب‌انگیز
تعطیل
تعطیل‌شده
تعمدی
تعمیرکار
تعیین‌شده
تعیین‌کننده
تفریحی
تقریبی
تقویتی
تلخ
تلخ‌زبان
تلفنی
تلف‌شده
تلویزیونی
تمام
تمام‌شدنی
تمام‌شده
تمام‌لبه
تمام‌نما
تمام‌وقت
تمدنی
تمیز
تناقض‌آمیز
تناور
تند
تندرو
تندروی
تنظیم‌شده
تنظیم‌کننده
تنفسی
تنها
تنومند
تنک
تنگ
تنگاتنگ
تنگ‌نظر
تهرانی
تهیه‌شده
تهیه‌کننده
تهی‌دست
توأم
توافقی
توانا
توانمند
توجیه‌پذیر
توحیدی
تورمی
تورم‌زا
توریستی
توسعه‌یافته
توقیف‌شده
تولیدکننده
تولیدگرا
تولیدی
تو‌در‌تو
تکان‌دهنده
تکراری
تکنولوژیکی
تکنیکی
تک‌ساحتی
تک‌پای
تک‌چشم
تیرانداز
تیره
تیز
تیزی
تیمی
ثابت
ثانوی
جاار
جاذبه
جاری
جاسوسی
جالب
جالبی
جامد
جامع
جامعه‌شناختی
جانوری
جانی
جان‌به‌لب
جاودانه
جاودانی
جاویدان
جبری
جدا
جداگانه
جدای
جدی
جدید
جدیدی
جدی‌تری
جذاب
جذابی
جرمزا
جزء
جزئی
جزایی
جسته
جسمانی
جسمی
جعلی
جفت
جمع
جمعی
جناحی
جناقی
جنایتکار
جنایی
جنبی
جنت‌نشان
جنجالی
جنجال‌انگیز
جنوبی
جنگلی
جنگی
جهانی
جهان‌شمول
جهان‌نمای
جوان
جوانانه
جوانتری
جوانمرد
جوانی
جور
جوشان
جوی
جویا
جیبی
حائز
حاد
حادث
حاصله
حاضر
حاوی
حاکم
حاکی
حتمی
حتمی‌الاجرا
حجمی
حداکثر
حداکثری
حذفی
حذف‌شده
حرارتی
حرام
حرمت‌شکن
حریف
حزبی
حسابی
حساس
حساسی
حساسیت‌زا
حساسیت‌زای
حسنه
حضوری
حقه
حقوقدان
حقوقی
حقیر
حقیقی
حق‌شناس
حق‌طلب
حلال
حلقومی
حلق‌آویز
حلیم
حمل
حوزوی
حکمت‌آمیز
حکومتی
حکیم
حیرت‌آور
حیرت‌انگیز
حیرت‌برانگیز
حیوانی
خائن
خارجه
خارجی
خارج‌شده
خاص
خاصی
خاضع
خاطرجمع
خاطی
خالی
خام
خاموش
خانوادگی
خانگی
خاکستری
خاکی
خبره
خبری
خجالتی
خدایی
خدشه‌دار
خدماتی
خراب
خرامان
خردسال
خرده‌فرهنگی
خرسند‌کننده
خرم
خرمی
خروجی
خزنده
خسارت‌دیده
خسته
خسته‌
خستگی‌ناپذیر
خشن
خشنود
خشنی
خشونت‌بار
خشک
خصوصی
خطاپوش
خطرناک
خطرناکی
خطی
خطیب
خطیر
خطیری
خط‌دهنده
خفه
خلاصه
خلاف
خلاق
خم
خمیده
خنثی
خندان
خنک
خواسته
خوب
خوبی
خودسر
خودکار
خودکامه
خودی
خوش
خوشایند
خوشایندی
خوشبخت
خوشبو
خوشبو‌کننده
خوشحال
خوشرفتار
خوشمزه
خوشوقت
خوشگوار
خوشی
خوش‌اخلاق
خوش‌خیم
خوش‌دست
خوش‌دهان
خوش‌رفتار
خوش‌سخن
خوش‌فرجام
خوش‌فکر
خوش‌نام
خونرنگ
خونسرد
خونی
خیال‌پرداز
خیال‌پردازانه
خیانتکار
خیر
خیراندیش
خیرخواه
خیره
خیره‌کننده
خیری
خیس
دائر
دائم
دائمی
داخلی
دارا
دارای
دارویی
داستانی
داغول‌باز
دامی
دانشجویی
دانشمند
دانشگاهی
داوطلب
داوطلبانه
دایر
دایمی
دخیل
درآمده
درآورده
دراز
درازمدت
درازی
دربرگیرنده
درحال‌گذار
درختی
درخشان
درخشانی
درخور
دردناک
درست
درستکردار
درستی
درست‌کردار
درشت
درصدد
درفشان
درمانی
دروغ
دروغگو
دروغگوی
درونی
درون‌استانی
درگیر
دریافتی
دریایی
در‌آمده
در‌برگیرندهٔ
در‌حال‌توسعه
در‌خور
در‌رفته
در‌هم‌تنیدهٔ
دستباف
دستجمعی
دسته‌جمعی
دستوری
دستگیر
دستی
دست‌آموز
دست‌افشان
دست‌به‌کار
دست‌ساز
دست‌کمی
دست‌یافتنی‌
دشمن
دشوار
دشواری
دعوت‌شده
دفاعی
دفعی
دقیق
دقیق‌تری
دلاری
دلالی
دلخواه
دلرحم
دلسوز
دلهره‌آور
دلپذیر
دلگشا
دلگیر
دل‌زندهٔ
دل‌مشغول
دموکراتیک
دمکراتیک
دهشتناک
دهم
دهمی
دوازدهم
دوجانبه
دوخته
دودوزه‌باز
دور
دورافتاده
دوراندیش
دوردست
دور‌دست
دوست
دوستانه
دوست‌داشتنی
دوسوی
دوقسمتی
دوقلو
دولتی
دوم
دومی
دوم‌خردادی
دونفره
دوگانه
دو‌جانبه
دو‌زبانه
دو‌فوریتی
دچار
دکتری
دگر
دگراندیش
دگرگون
دیابتی
دیجیتال
دیجیتالی
دیر
دیری
دیر‌فهم
دیر‌قدمت
دیم
دینی
دین‌ستیزی
دیواری
دیوانه‌
دیپلماتیک
دیگر
دیگری
دیگه
ذهنی
ذوب‌شده
ذکر‌شده
ذکور
ذیربط
ذیل
رإف
راحت
راحت‌تری
راحل
رادیویی
رادیو‌اکتیو
رازدار
راست
راستگو
راستی
راسخ
راضی
رافضی
راهبردی
راهنما
راهگشای
رایج
رایگان
ربات
ربانی
رزمی
رسای
رسمی
رسوا
رسیده
رسیدگی‌کننده
رشتی
رشد‌دهنده
رفتاری
رفته
رفیع
رقابتی
رقص‌وار
رنجور
رنگارنگ
رنگارنگی
رهگشا
روا
روائی
روان
روانه
روانی
روبرو
روبه‌رو
روحانی
روحی
روحی‌
روراست
روز
روزانه
روزمره
روزه
روزی‌گذار
روس
روستایی
روسی
روشن
روشنفکر
روشنفکری
روشنی
روند
رویایی
ریاضی‌دان
ریالی
ریخته‌شده
ریختی
ریز
ریزبافت
ریشه‌دار
ریشه‌کن
ریوی
ریگی
رییسه
زار
زاهدانه
زاید
زایل
زبانی
زبر
زبردست
زخمی
زرنگ
زرنگی
زرینی
زرین‌فام
زشت
زشتی
زمانی
زمان‌بندی‌شده
زمان‌شناسی
زمستانی
زمینه‌ساز
زمینی
زنانه
زنانهٔ
زنانه‌یی
زنبوری
زنبوری‌
زنجانی
زنجیر‌شده
زندانی
زنده
زنده‌
زندگی‌دوست
زننده
زنگباری
زود
زودباور
زودرس
زودگذر
زود‌هضمی
زیاد
زیادی
زیانبخش
زیان‌بار
زیبا
زیباشناختی
زیبای
زیبایی
زیر
زیربنایی
زیرزمینی
زیرلاکی
زیرک
زیرک‌
زیست‌محیطی
زینتی
زیگ‌زاگ‌گونه
سابق
ساحلی
ساختاری
ساختمانی
ساخته
ساختهٔ
ساخته‌شده
ساختگی
ساده
ساده‌
سازمانی
سازمان‌یافته
سازنده
سازگار
ساعته
ساعتی
ساقط
ساقط‌شده
سالانه
سالم
سالمند
ساله
سالهٔ
ساله‌
سالگی
سالیانه
سامانی
سانتی‌متری
ساکت
ساکن
سبز
سبک
سبکبال
سبکسر
ستایشی
ستاینده
ستمدیده‌یی
ستم‌شاهی
سحرانگیز
سخت
سختگیر
سرانه
سربلند
سربه‌نیست
سرخ
سرخوش
سرد
سردسیری
سرزده
سرسخت
سرشار
سرشناس
سرطانی
سرطان‌زا
سرمست
سرنگون
سروده
سرپایی
سرکش
سرکوب‌کننده
سرگردان
سرگرم
سرگرم‌کننده
سری
سریع
سریعتری
سر‌درگم
سست
سستی
سطحی
سطحی‌نگر
سعودی
سفالی
سفت
سفید
سفیدرنگ
سفیدپوست
سفیدپوش
سلبی
سلحشور
سلطانی
سلطنتی
سلولی
سلیم
سمعی
سمی
سنتی
سنت‌گرای
سنجیده
سنگی
سهامی
سهوی
سهیم
سه‌جلدی
سه‌ساله
سه‌فرسخی
سه‌گانه
سواره
سواری
سوای
سوخته
سودآور
سودازده
سودمند
سوسیالیستی
سوم
سومی
سوپرالیت
سوگوار
سپاسگزار
سپید
سکتاریسم
سکولار
سکولارولاییک
سگ‌باز
سیاحتی
سیار
سیاسی
سیاه
سیر
سیراب
سیرجانی
سیزدهم
سیستمی
سیفلیسی
سیلندری
سیل‌آسا
سیم‌گون
سینمایی
سیگاری
سی‌سؤالی
شاخص
شاخ‌دار
شاد
شاداب
شادمان
شاعرانه
شاعری
شاغل
شامخ
شامل
شانزدهم
شاهد
شایان
شایسته
شایستهٔ
شایع
شایعه‌پرداز
شبیه
شتابزده
شجاع
شجاعی
شخصی
شخصیتی
شدید
شدیدی
شراب‌خوار
شرعی
شرقی
شرقیِ
شرکت‌کننده
شریف
ششم
شش‌دانگی
شش‌نفره
شعاری
شعری
شعله‌ور
شغلی
شفاف
شفاهی
شل
شمالی
شمرده
شمسی
شناخته
شناخته‌شده
شناور
شنفته
شنوا
شنیده
شهرستانی
شهروندی
شهری
شهیر
شوخ
شور
شورایی
شوم
شوکه
شکاک
شکربار
شکسته
شکست‌خورده
شکفته
شکننده
شکوهمند
شکیبا
شک‌برانگیز
شگفت
شگفت‌آور
شگفت‌انگیز
شیبدار
شیرازی
شیطانی
شیفتهٔ
شیمیایی
شیک
صاحب‌نام
صادر
صادراتی
صادقانه
صاف
صالح
صبحگاهی
صبور
صحرائی
صحیح
صحیح‌تری
صدساله
صرف
صریح
صغیر
صلیبی
صمیمی
صنعتی
صنفی
صهیونیستی
صوتی
صورت‌گرفته
صیادی
ضبط‌شده
ضد
ضدارزش
ضداسلامی
ضدانقلابی
ضدعشقی
ضدمیگرن
ضد‌استبدادی
ضد‌استعماری
ضروری
ضروری‌
ضعیف
ضعیف‌النفس
ضمیمه
طاقت‌فرسا
طبقاتی
طبیعی
طلائی
طلایی
طلا‌نشانده
طنزآمیز
طولانی
طولانی‌مدت
طویلی
طیب
ظالمانه
ظاهری
ظریف
ظریفی
عاجز
عادتی
عادل
عادلانه
عادلِ
عادی
عارض
عارفانه
عاری
عاشق
عاشقانه
عاطفی
عاقل
عالی
عالیقدر
عالیه
عالی‌رتبه
عالی‌مقام
عام
عامه
عتیقه
عثمانی
عجیب
عربی
عربی‌شناس
عرب‌زبان
عرفانی
عرفی
عروقی
عریض
عزیز
عزیزِ
عشایری
عشقی
عشق‌انگیز
عصبانی
عصبی
عضو
عظام
عظیم
عظیمی
عظیم‌الجثه
عفونی
عقب‌افتاده
عقدکرده
عقلی
عقیدتی
علاقه‌مند
علمی
علمیه
علمیی
علنی
عمد
عمده
عمدهٔ
عمده‌یی
عمدی
عمرانی
عملگرا
عملی
عملیاتی
عملی‌
عمودی
عمومی
عمیق
عمیقی
عنبرین‌بو
عنود
عهد‌نگهدار
عیان
عینی
غائب
غاصب
غافل
غافلگیر
غافلگیرکننده
غایی
غبارآلود
غذاخوری
غذایی
غذایی‌
غربی
غربیِ
غرق
غرقِ
غره
غریب
غریبه
غریبی
غلط
غلطِ
غلیظ
غمزده
غم‌آباد
غم‌آلود
غم‌انگیز
غنی
غنی‌شده
غنی‌یی
غوطه‌ور
غول‌پیکر
غیرآهنی
غیراخلاقی
غیراستاندارد
غیراسلامی
غیراصلی
غیراصولی
غیرافسرده
غیراقلیدسی
غیرانقلابی
غیردوستانه
غیردولتی
غیردینی
غیررسمی
غیرسیاسی
غیرطبیعی
غیرعادلانه‌یی
غیرعادی
غیرعرب
غیرقانونی
غیرمارکسیست
غیرمترقبه
غیرمتعارف
غیرمحتمل
غیرمحقق
غیرمذهبی
غیرمستقیم
غیرمستقیمی
غیرمسلح
غیرمسیحی
غیرمعنوی
غیرملی
غیرمنتظره
غیرمنطقی
غیرمنقول
غیرموثق
غیرنظامی
غیرنفتی
غیرواقعی
غیرکلیشه
غیر‌انتخابی
غیر‌تخصصی
غیر‌رسمی
غیور
فئودالی
فاتح
فاحش
فارسی
فارسی‌دان
فارسی‌زبان
فارغ
فاسد
فاش
فاصل
فاضل
فاضله
فاطمی
فاقد
فانتزی
فانی
فداکار
فدرال
فراری
فراملی
فراموش
فرانسه
فرانسوی
فراوان
فراوانی
فراگیر
فراگیری
فربه
فرخنده
فردی
فردی‌
فرزانه
فرساینده
فرضی
فرعی
فرنگی
فرهنگی
فرهنگی‌
فرهنگ‌دوست
فروتن
فروخته
فروخته‌شده
فروزان
فروشندگی
فروگذار
فرو‌ریخته
فریبنده
فسخ‌شده
فسرده
فشرده
فصلی
فصیح
فضایی
فضایی‌
فضیلت‌ها
فعال
فعلی
فقهی
فقید
فقیر
فلزی
فلسفی
فلسفیی
فلکی
فنلاندی
فنی
فهمیده
فهیم
فوری
فوریتی
فوری‌
فوق
فوقانی
فوق‌الذکر
فوق‌العاده
فکری
فیروزه‌گون
فیزیولوژیکی
فیزیکی
فیلسوف
فیلیپینی
فی‌سبیل‌الله
قائل
قائم
قابل
قابل‌اتکاء
قابل‌توجه
قابل‌توجهی
قابل‌قبول
قابل‌مشاهده
قابل‌مقایسه
قابل‌نفی
قابل‌یادآوری
قادر
قاطبه
قاطع
قالبی‌شده
قانع
قانونمند
قانونی
قاچاقچی
قبطی
قبل
قبلی
قبلی‌
قبول
قبیله‌یی
قدرتمند
قدرتی
قدیم
قدیمی
قرآنی
قرض‌الحسنه
قرمز
قرمزی
قریب
قشنگ
قشنگتری
قشنگی
قضائیه
قضایی
قطعی
قفقازی
قلابی
قلبی
قلدری
قمری
قهرمانی
قهریه
قومی
قوی
قیصری
قیمتی
لاابالی
لاتینی‌نویس
لازم
لازمه
لاغر
لاینقطع
لاییک
لبالب
لبریز
لذت‌طلب
لطیف
لعابدار
لهجه‌دار
لوکس
لیبرال
م
مأثر
مؤثر
مؤثری
مؤمن
مؤمنی
مإدبانه
ماجراجو
مادام‌العمر
مادری
ماده
مادی
مارکسیست
مارکسیستی
مازاد
ماشینی
ماشین‌رو
ماشین‌زده
مالایلزم
مالی
مالیه
مالی‌
ماندنی
مانده
ماندگار
ماهانه
ماهری
ماهه
مایل
مبارز
مبارک
مبارکه
مبتذل
مبتلا
مبتنی
مبذول
مبرا
مبسوط
مبهمی
متأثر
متؤثر
متاثر
متبادر
متبحر
متبرک
متبسم
متجاوز
متجدد
متجددی
متجملانه
متحد
متحده
متحرک
متحمل
متحول
متخصص
متخلص
متدینی
متذکر
متروک
متروکه
متزلزل
متشکر
متشکل
متصل
متصور
متضاد
متضرر
متضمن
متعادل
متعارض
متعارف
متعال
متعدد
متعددی
متعصب
متعلق
متعهد
متغیر
متفاوت
متفاوتی
متفرق
متفکر
متقابل
متقاضی
متقن
متقی
متلاشی
متمادی
متمایل
متمرکز
متمم
متمولی
متناسب
متناقض
متنبی
متنبی‌خوان
متنوع
متنوعی
متهم
متواضع
متوالی
متوجه
متوسط
متوسطه
متوسل
متوفی
متوقف
متکثر
متکی
مثبت
مثبته
مثبتی
مجاز
مجانی
مجبور
مجدد
مجددی
مجذوب
مجرد
مجرم
مجروح
مجزا
مجسم
مجعول
مجلل
مجمل
مجهز
محافظتی
محافظه‌کار
محبوب
محتاج
محترم
محترمی
محتمل
محتوم
محدود
محدودکننده
محدودی
محروم
محرک
محسوب
محسوس
محض
محفوظ
محقق
محلی
محو
محوری
محکم
محکمی
محکم‌تری
محکوم
محیطی
مخابراتی
مخالف
مختصر
مختصری
مختل
مختلف
مختلفی
مخدر
مخدوش
مخرب
مخصوص
مخفی
مخلص
مخلوع
مد
مداخله‌جویانه
مدارا
مداوم
مدبرانه
مدرسی
مدرن
مدعی
مدنی
مدور
مدون
مدیدی
مدیریتی
مدیون
مذموم
مذهبی
مذهبی‌
مذهبی‌سنتی
مذکر
مذکور
مراقبتی
مربع
مربوط
مربوطه
مرتب
مرتبط
مرتفع
مرتکب
مردانه
مردد
مردمی
مردم‌نواز
مرده
مرزی
مرسوم
مرمت‌شده
مرمری
مرموز
مرهون
مرکب
مرکزی
مرگبار
مریض
مزبور
مزدور
مزمن
مزید
مسؤله‌داری
مسئله‌دار
مسئول
مسئولیت‌آور
مساعد
مسافرکش
مسافری
مسالمت‌آمیز
مساولانه
مساوی
مست
مستبدی
مستثنی
مستحضر
مستحق
مستحکم
مستحکمی
مستدل
مستعد
مستقر
مستقل
مستقلی
مستقیم
مستمر
مستندگونه
مستور
مستوی
مستی‌بخش
مسجل
مسدود
مسدود‌شده
مسرفانه
مسلح
مسلط
مسلم
مسلمان
مسلمانِ
مسموم
مسمومی
مسن
مسوول
مسکن
مسکونی
مسکوک
مسیحی
مشابه
مشابهی
مشارکتی
مشارکت‌جو
مشاهده‌شده
مشبک
مشتاق
مشتبه
مشترک
مشترکی
مشتمل
مشخص
مشخصی
مشرف
مشروط
مشروطه
مشروع
مشغول
مشفق
مشمول
مشهودی
مشهور
مشهوری
مشورتی
مشکل
مشکل‌گشا
مشکوک
مصدوم
مصرفی
مصرف‌شده
مصرف‌کننده
مصری
مصلحانه
مصمم
مصنوعی
مصوب
مصون
مضاعف
مضاف
مضر
مطابق
مطالعاتی
مطبوع
مطبوعاتی
مطرح
مطرح‌شده
مطروحه
مطرود
مطلع
مطلق
مطلقه
مطلوب
مطلوبی
مطمئن
مظلوم
معادل
معارض
معاصر
معاند
معتاد
معتبر
معتبری
معتدل
معترض
معتقد
معجزه‌آسایی
معدنی
معدود
معدودی
معذور
معرفتی
معرق
معروف
معزول
معصوم
معضل‌ساز
معطر
معطل
معطوف
معظم
معقول
معقولی
معلا
معلق
معلمی
معلوم
معماگونه
معمم
معممی
معمول
معمولی
معنایی
معنوی
معنی‌دار
معوقه
معکوس
معیشتی
مغبون
مغذی
مغرض
مغرور
مغزی
مغفول
مغلوب
مغناطیسی
مفت
مفرغی
مفصل
مفصلی
مفقود
مفقوده
مفقود‌شده
مفهومی
مفید
مقابل
مقاربتی
مقاوم
مقبول
مقتضی
مقدس
مقدم
مقدماتی
مقدور
مقرر
مقرون
مقصر
مقید
مقیم
ملایم
ملحد
ملزوم
ملموس
ملکوتی
ملکولی
ملکی
ملی
ملی‌گرای
ممتاز
ممتازی
ممزوج
ممنوع
ممنوعه
ممنون
ممکن
مناسب
مناسبی
مناسب‌تری
منافق
منان
منبت‌کاری‌شده
منتخب
منتسب
منتشر
منتشرشده
منتشره
منتشر‌شده
منتظر
منتفی
منتقل
منتهی
منثور
منجر
منحرف
منحصر
منحصربه‌فرد
منحصربه‌فردی
منحصر‌بفرد
منحصر‌به‌فرد
منحط
منحل
منحنی
مندرج
منزوی
منسجم
منسوخ
منصرف
منصفانه
منصفه
منصوب
منطبق
منطقی
منظم
منظوم
منعقد
منعکس
منفجره
منفور
منفک
منفک‌شده
منفی
منقوش
منقول
منهدم
منوط
منکر
مهربان
مهربانی
مهرشده
مهلک
مهم
مهمی
مهم‌
مهندسی
مه‌آلود
مواجه
مواجه‌
موازی
مواظب
موافق
موثق
موثقی
موجه
موجهی
موجود
مودب
موردی
موزون
موسوم
موضوعی
موظف
موفق
موفقی
موفقیت‌آمیز
موقت
موقوفه
مولد
مونت
موهوم
موکول
مکانیکی
مکتوبی
مکرر
مکرری
مکشوف
مکشوفه
مکلف
مکمل
میانجی
میانسالی
میانه‌رو
میانی
میان‌بر
میان‌سال
میان‌مدت
میخواره
میدانی
میزبان
میسر
میلادی
میکروبی
میگرنی
می‌نوش
ناآشنا
ناآگاه
نائل
نااقلیدسی
ناامن
ناامید
ناب
ناباب
نابود
ناتوان
ناتورالیستی
ناخالص
ناخرسند
ناخشنود
ناخواسته
ناخوشایند
نادر
نادرست
نادرستی
نادیده
ناراحت
ناراضی
ناراضی‌
نارس
ناروا
ناز
نازل
نازک
نازکی
ناشایست
ناشناخته
ناشناس
ناشی
ناظر
نافرجام
ناقص
نالان
نامالوف
نامتجانس
نامتعارف
نامحتمل
نامحدود
نامحدودی
نامدار
نامداری
نامربوط
نامریی
نامساعد
نامشخصی
نامطلوب
نامطمئن
نامناسب
نامنظم
نامنقح
ناموزون
ناموفق
نامی
نامیده
نام‌آشنای
نانوشته
نان‌شناس
ناهمزمان
ناپخته
ناپدید
ناپیدا
ناچار
ناچیز
ناچیزی
ناکارآمد
ناکافی
ناکام
ناگهانی
نایاب
نایب‌قهرمانی
نا‌ملموس
نباتی
نبوده
نبوغ‌آمیز
نترس
نجاتگر
نجات‌بخش
نجنگیده
نجومی
نجیب
نخست
نخودی
نرم
نرم‌افزاری
نزدیک
نزدیکی
نزولی
نساجی
نسبی
نستعلیق
نسطوری
نشانگر
نظارتی
نظامی
نظام‌یافته
نظری
نظیف
نظیفی
نفتی
نفره
نفوذی
نفی‌کننده
نقد
نقدی
نقلی
نقیض
نمادینی
نمایان
نمایانی
نمایشی
نمایشی‌
نمرده
نمناک
نموده
نمونه
نهاده
نهادی
نهادینه
نهان
نهایی
نهفته
نو
نوجوان
نورانی
نورشناختی
نوزدهم
نوشته
نوپای
نوینی
نویی
نپخته
نژادی
نگار
نگاشته
نگران
نگهدارنده
نگینی
نیازمند
نیاورده
نیاکانی
نیایشی
نیرومند
نیرومندی
نیشابوری
نیفزوده
نیل‌گون
نیمه‌تمام
نیمه‌شناخته‌شده
نیمه‌نهایی
نیمه‌پایانی
نیمه‌گرمسیری
نیم‌خیز
نیوزیلندی
نیک
نیکو
نیکوکار
هالیوودی
هانمید
هجدهم
هجری
هخامنشی
هدایتگری
هدایت‌کننده
هدفمند
هراسان
هرزه‌نویس
هرقلی
هر‌از‌چند‌گاه
هزار‌تومانی
هزینه‌شده
هشتم
هشت‌ساله
هشت‌هزار‌متری
هشداردهنده
هشدار‌دهنده
هفتم
هفتگی
هفدهم
هلاکوای
هلندی
هلکو
هماهنگ
همجوار
همدردی‌برانگیز
همراه
همرنگ
همزمان
همسان
همسایه
همسایهٔ
همسن
همصدا
همفکر
همه‌جانبه
همه‌جانبه‌یی
همه‌ساله
همه‌گیر
هموار
همپای
همپایهٔ
همگام
همگانی
همگروه
همگون
همیشگی
هم‌آهنگ‌کننده
هم‌جناح
هم‌خانواده
هم‌دندان
هم‌سان
هم‌سن
هم‌طیف
هم‌نظر
هم‌گروه
هند
هندشناس
هندی
هنری
هنگفت
هوادار
هوایی
هوشیار
هویدا
هیدروسفالی
هیچکاره
هیچکارهٔ
وابسته
وابستهٔ
وابسته‌
واحد
واحده
واحدی
وارد
وارداتی
وارده
وارد‌شده
وارفته
واسط
واسطه‌گری
واضح
واضحی
واضح‌تری
وافر
واقع
واقعی
واقع‌بینانه
واقع‌بینانه‌تری
واقع‌گرا
واقع‌گرای
واقف
واقفند
والا
وانمود
واهی
واگذار
واگذارشده
واگرایانه
واگیردار
وجودی
وحدت‌آمیز
وحشتناک
وحشت‌آور
وحشی
ورزشکار
ورزشی
ورودی
وسطی
وسیع
وسیعی
وصف‌ناشدنی
وصله‌زده
وضعی
وضعیتی
وضوح
وفادار
وقفی
ونزوالایی
وهم‌آلود
ویران
ویرانش
ویران‌کننده
ویروسی
ویژه
ویژه‌یی
پادشاهی
پارسی
پارلمانی
پاره
پاره‌پاره
پانزدهم
پاک
پاکدامن
پاکستانی
پاکش
پایانی
پایان‌بخش
پایان‌ناپذیری
پایبند
پایدار
پای‌بند
پخته
پخته‌شده
پخش‌شده
پدرانه
پدید
پذیرا
پذیرای
پذیرایی
پذیرفتنی
پذیرفته
پر
پرآشوب
پراحساس
پراندوهی
پراهمیتی
پراکنده
پربار
پرباغ
پربرف
پرتجملی
پرتنش
پرتیراژ
پرثمر
پرخاشگرانه
پرخروش
پرخواننده
پرداخته
پرداختی
پرداخت‌نشده
پردرآمد
پررنگ
پرزرق
پرسابقه
پرسابقهٔ
پرسود
پرسُخُن
پرشور
پرشکوه
پرشکوهی
پرطرفدار
پرمحتوا
پرمحصول
پرمخاطب
پرنده‌خوار
پرنشاط
پرنور
پرنکته
پرنگار
پرهیبتی
پرواضح
پرورده
پروسیله‌تری
پروپاقرص
پرپر
پرپینه
پرکار
پرگذشت
پرگل
پرگو
پر‌خطر
پر‌دردسری
پر‌رویا
پر‌قدرتی
پر‌مسئولیت
پر‌معنایی
پر‌گذشت
پزشکی
پستی
پسندیده
پشتگرم
پشت‌سبزی
پشیمان
پشیمون
پف
پلاستیکی
پلیسی
پنجاه‌ساله
پنجاه‌نفره
پنجاه‌نفری
پنجساله
پنجم
پنجمی
پنهان
پهن
پهناور
پهن‌شده
پوستی
پوشیده
پولدار
پولی
پوک
پُرنقش
پژوهشی
پیاده
پیاپی
پیدا
پیر
پیرامونی
پیروز
پیشتاز
پیشرفته
پیشرو
پیش‌آمده
پیش‌بینی‌شده
پیش‌پا‌افتاده
پیش‌کسوت
پیغمبری
پیمان‌شکن
پیوسته
پیچیده
پیگیر
چالاک
چاپاری
چاپی
چاپ‌شده
چرخان
چرخانده
چریکی
چسبیده
چشمگیر
چشمگیری
چشم‌انداز
چشم‌نواز
چمدانی
چنانی
چند
چندانی
چندبعدی
چندساله
چندگانه‌اندیش
چند‌
چند‌بعدی
چند‌جانبه
چند‌سالهٔ
چند‌هزار‌ساله
چنینی
چهاردهم
چهاردهمی
چهارساله
چهارم
چهارمی
چهارگانه
چهل‌نفره
چوبی
چپ
چیره
چینی
ژاپنی
ژرف‌نگر
ژنتیک
ژنتیکی
ژنریک
ژنی
کاذب
کارآمد
کاربردی
کارشناسانه
کارگری
کارگشا
کاری
کاسته
کافر
کافی
کامل
کاملی
کامور
کامکار
کانادایی
کانتینری
کاوش
کایب
کبیر
کتابی
کتانی
کتبی
کتمان‌ناپذیر
کثیر
کثیرالانتشار
کثیری
کثیف
کذب
کر
کربنیزه
کرد
کرمانی
کرم‌خورده
کرم‌خورده‌
کریم
کساد
کسروی
کسری
کشته
کشت‌شده
کشف‌شده
کشنده
کشوری
کشیده
کل
کلاسیک
کلافه
کلامی
کلان
کلان‌نگر
کلک
کلی
کلیدی
کلیشه
کلیوی
کم
کمتری
کمدی
کمرنگ
کمری
کمونیست
کمونیستی
کمی
کمیاب
کمیک
کم‌جمعیت
کم‌حرف
کم‌رنگ
کم‌سابقه
کم‌سن
کم‌ظرفیت
کم‌نظیر
کنجکاو
کنجکاوی
کند
کنده
کندی
کنونی
کهن
کهنسال
کهنه
کهنهٔ
کوتاه
کوتاهی
کوتاه‌مدت
کوته‌بینانه
کودن
کورکننده
کورکورانه
کوهنورد
کوچولویی
کوچک
کوچکی
کویتی
کویری
کیفی
کیلومتری
گازی
گازی‌شکل
گدا
گذشته
گذشته‌
گرامی
گران
گرانبار
گرانبها
گرانبهای
گرانقدر
گران‌بهایی
گردن‌کلفتِ
گردون
گرفتار
گرفته
گرفته‌شده
گرم
گرمسیری
گروهی
گروگانگیر
گریزان
گزارشگر
گزارشی
گزنده‌گو
گزینشی
گسترده
گسترده‌تری
گشاد‌کننده
گشوده
گفتاری
گفتنی
گفته
گلخانه‌مانند
گله‌مند
گلی
گل‌افشان
گم
گمراه
گمراه‌کننده
گمنام
گنبدی
گهربار
گوارای
گوارشی
گوشتی
گوناگون
گوناگونی
گویا
گویای
گیاهی
گیج
یائسه
یادآور
یادشده
یاد‌شده
یازدهم
یافت‌شده
یخی
یزدی
یمنی
یهودی
یونانی
یکجا
یکجای
یکسان
یکسانی
یکسویه
یکم
یکه
یکپارچه
یک‌جانبه
یک‌دست
یک‌روزه
ییلاقی
""".split(
        "\n"
    )
)
