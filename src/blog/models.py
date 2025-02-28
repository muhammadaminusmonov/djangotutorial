from datetime import date

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

# # 1) Yangi “Beatles Blog” nomli Blog obyektini yarating (name=
# battles_blog = Blog(name='Battles blog', tagline='Something')
# # battles_blog.save()

# # 2) “Cheddar Talk” nomli Blog obyektini bor deb faraz qiling. Uning name="Cheddar Talk" va tagline="Say cheese!"
# # bo‘lsin. Ushbu blogni bazadan qaytarish mumkinligini tekshiring.
# cheddar_talk = Blog(name='Cheddar Talk', tagline='Say cheese!')
# # cheddar_talk.save()
# get_blog = Blog.objects.get(tagline='Say cheese!')
# print(get_blog)

# # 3) Bir nechta Author obyektlari kiriting (masalan, “John”, “Paul”, “Ringo”, “George” nomli). Nomida “o” harfi bor
# # mualliflarni izlab toping.
# get_authors = Author.objects.filter(name__contains='%o%')
# print("worked", get_authors)

# # 4) Entry modelida turli postlar (headline, pub_date) mavjud deylik. Ularning ba’zilari 2021-yilda, ba’zilari
# # 2010-yilda chop etilgan. Filtrlash yordamida 2021-yilda chop etilgan yozuvlarni ajratib oling.
# get_entry_by_date = Entry.objects.filter(pub_date__year=2021)
# print(f"worked well: {get_entry_by_date}")

# # 5) Barcha Entry obyektlarini sanaga qarab (pub_date) tartiblang, keyin dastlabki 3 ta yozuvni cheklang. So‘ng ularni
# # ko‘rishingizga ishonch hosil qiling.
# get_first_three_entry = Entry.objects.order_by("-pub_date")[:3]
# for i in get_first_three_entry:
#     print(i)

# # 6) Entry obyektlari sarlavhasida (“headline”) “Bio” so‘zini (harf registriga e’tibor bermasdan) o‘z ichiga olgan
# # postlarni izlab toping.
# get_entry_by_headline = Entry.objects.filter(headline__contains='bio')
# print(get_entry_by_headline)

# # 7) Ma’lum bir Blog (masalan, “Cheddar Talk”) ga tegishli barcha Entry obyektlarini izlab toping. Natijada qaytarilgan
# # yozuvlarning haqiqatan ham o‘sha blog bilan bog‘liqligini tasdiqlang.
# cheddar_talk_blog = Blog.objects.get(name="Cheddar Talk")
# get_entry_by_blog = Entry.objects.filter(blog=cheddar_talk_blog)
# for i in get_entry_by_blog:
#     print(i)

# 8) Entry va Author orasida ManyToMany aloqalar bo‘lganini inobatga oling. Mualliflaridan “John” bo‘lgan postlarni
# aniqlang.
get_entry = Entry.objects.filter(authors__name='John')
print(get_entry)

# 9) Bir nechta Entry “Beatles Blog”ga tegishli bo‘lsin, shuningdek bu postlarda mualliflari orasida “George” va “Paul”
# mavjud deb faraz qiling. Faqat “George” muallifi bor postlarni tanlab olish uchun tegishli filtr-larni qo‘llang.

# 10) Entry obyektlaridan 2015-01-01 dan 2020-12-31 gacha bo‘lgan oraliqda chop etilganlarini toping va ularning sonini
# tekshiring.

# 11) Agar Entry modelida “view_count” va “comment_count” integer maydonlari bo‘lsa, “view_count” “comment_count”dan
# katta bo‘lgan yozuvlarni ajratib oling.

# 12) Shu Entry lardan biri:
#    – headline="Django i18n",
#    – pub_date=2024-03-15,
#    – comment_count=500,
#    – pingback_count=400
#    Bo‘lsa, “comment_count” va “pingback_count” ustidan arifmetik ifodalar bilan filtr qo‘llab, natijasini tekshiring.

# 13) Ma’lum bir “Lennon” so‘zi sarlavhaga ega Entry postlari bilan bog‘liq bo‘lgan Blog obyektlarini toping.

# 14) “Jazz Blog” (tagline="Smooth & All That Jazz") va “Pop Music Blog” (tagline="Chart Toppers") kabi yangi bloglar
# yarating. tagline maydonida “music” so‘zi bo‘lgan bloglarni filtrlab chiqing.

# 15) Bitta Entry obyektida sarlavha “Django” va “Tips” so‘zlarini o‘z ichiga olsa (masalan, “Django Tips & Tricks”),
# uni topish uchun ketma-ket filtrlash yoki bitta filter() ichida ikkita shartdan foydalanib izlab ko‘ring.