# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fika = Character("Fika", image="fika") # Sumi
define sivi = Character("Sivi", image="sivi") # Miki
define alga = Character("Alga", image="alga") # Aoto
define arsi = Character("Arsi", image="arsi") # Miho
define mana = Character("Mana", image="mana") # Hana
define jara = Character("Jara", image="jara") # Sora
define siji = Character("Siji", image="siji") # Rin
define rika = Character("Rika", image="rika") # Kana
define lara = Character("Lara", image="lara") # Nora
define tica = Character("Tica", image="tica") # Chie
define hima = Character("Hima", image="hima") # Kousei
define piko = Character("Piko", image="piko") # Aiko

label start:
    jump east_2f_corridor

# This is the start of the Exploration Sub FSM.

label hall:
    scene bg hall ext with fade:
        zoom 1.9 yalign 0.2

    show hima open:
        zoom 1.0 pos(0.6, 0)

    hima open blush "Haii! Selamat datang kembali di Aula."
    hima open "Gimana gimana? Udah siap buat kuisnya?"

    show hima closed smile

    menu hall_menu:
        "Apa kamu sudah siap?"
        
        "Ya!":
            hima open "Bagus! Ikut aku ya. Kita akan tes pengetahuanmu tentang Informatika... Di luar!"
            jump hall

        "Hmmm kayanya belum siap. Aku pengen keliling-keliling dulu.":
            hima open blush "Oke, kamu bisa keliling-keliling lagi. Tapi jangan lupa untuk kembali ke aula ya!"
            jump east_2f_corridor

label east_2f_corridor:
    scene bg east 2nd floor corridor with fade:
        zoom 1.9

    menu east_2f_corridor_menu:
        "Kamu sedang berada di koridor timur. Ke mana kamu ingin pergi?"

        "← Masuk ke aula":
            jump hall

        "↑ Pergi ke lounge selatan":
            jump south_2f_lounge

        "↓ Pergi ke lounge utara":
            jump north_2f_lounge

label north_2f_lounge:
    scene bg north 2nd floor lounge with fade:
        zoom 1.9 yalign 1.0

    menu north_2f_lounge_menu:
        "Kamu sedang berada di lounge utara. Ke mana kamu ingin pergi?"

        "↓ Pergi ke koridor timur":
            jump east_2f_corridor

        "← Pergi ke koridor utara":
            jump north_2f_corridor
            
        "↗ Naik ke lantai ketiga":
            jump north_3f_lounge

        "↘ Turun ke lantai pertama":
            jump north_1f_lounge

label south_2f_lounge:
    scene bg south 2nd floor lounge with fade:
        zoom 1.9 yalign 0.9

    menu south_2f_lounge_menu:
        "Kamu sedang berada di lounge selatan. Ke mana kamu ingin pergi?"

        "↓ Pergi ke koridor timur":
            jump east_2f_corridor

        "→ Pergi ke koridor selatan":
            jump south_2f_corridor
            
        "↖ Naik ke lantai ketiga":
            jump south_3f_lounge

        "↙ Turun ke lantai pertama":
            jump south_1f_lounge

label north_2f_corridor:
    scene bg north 2nd floor corridor with fade:
        zoom 1.9

    menu north_2f_corridor_menu:
        "Kamu sedang berada di koridor utara. Ke mana kamu ingin pergi?"

        "← Lihat ruang TU":
            jump tu

        "↑ Pergi ke lounge utara":
            jump north_2f_lounge        

label tu:
    scene bg tu ext with fade:
        zoom 1.9

    "Oh jadi disini ruang TUnya."
    "Harus inget nih, biar kalo mau ngurusin surat gampang."
    "Ini di lantai 2 terus di sebelah utara. Inget... inget..."

    menu tu_menu:

        "Keluar dari ruang TU":
            jump north_2f_corridor

label south_2f_corridor:
    scene bg south 2nd floor corridor with fade:
        zoom 1.9

    menu south_2f_corridor_menu:
        "Kamu sedang berada di koridor selatan. Ke mana kamu ingin pergi?"

        "↓ Pergi ke lounge selatan":
            jump south_2f_lounge

label north_1f_lounge:
    scene bg north 1st floor lounge with fade:
        zoom 1.9 yalign 0.6

    menu north_1f_lounge_menu:
        "Kamu sedang berada di lounge utara. Ke mana kamu ingin pergi?"

        "↗ Naik ke lantai kedua":
            jump north_2f_lounge

        "← Pergi ke koridor utara":
            jump north_1f_corridor

        "↓ Pergi ke koridor timur":
            jump east_1f_corridor

label south_1f_lounge:
    scene bg south 1st floor lounge with fade:
        zoom 1.9 yalign 0.5

    menu south_1f_lounge_menu:
        "Kamu sedang berada di lounge selatan. Ke mana kamu ingin pergi?"

        "↖ Naik ke lantai kedua":
            jump south_2f_lounge

        "↓ Pergi ke koridor selatan":
            jump south_1f_corridor

        "← Pergi ke koridor timur":
            jump east_1f_corridor

label north_1f_corridor:
    scene bg north 1st floor corridor with fade:
        zoom 1.9 yalign 0.8

    menu north_1f_corridor_menu:
        "Kamu sedang berada di koridor utara. Ke mana kamu ingin pergi?"

        "↑ Pergi ke masjid":
            jump mosque

        "↓ Pergi ke lounge utara":
            jump north_1f_lounge

label mosque:
    scene bg mosque with fade:
        zoom 1.9 yalign 0.7

    "Ooooohh.... jadi disini masjidnya. Harus inget nih, biar kalo mau sholat bisa di sini."
    "Ini dimana ya? Oh ini di lantai 1 kan? Iya terus ini di sebelah utara. Harus inget sih."

    menu mosque_menu:

        "Keluar dari masjid":
            jump north_1f_corridor

label south_1f_corridor:
    scene bg south 1st floor corridor with fade:
        zoom 1.9 yalign 0.8

    menu south_1f_corridor_menu:
        "Kamu sedang berada di koridor selatan. Ke mana kamu ingin pergi?"

        "↑ Pergi ke PIKTI":
            jump pikti

        "← Lihat Lab Pascasarjana":
            jump lab_pascasarjana

        "↓ Pergi ke lounge selatan":
            jump south_1f_lounge

label pikti:
    scene bg pikti with fade:
        zoom 1.9 yalign 0.7

    show piko smile:
        zoom 1.0 pos(0.6, 0)

    "PIKTI? Apa nih?"

    piko shout "PIKTI itu singkatan dari Pendidikan Informatika dan Komputer Terapan Teknik Informatika ITS."
    piko shout blush "PIKTI itu tempat buat masyarakat umum yang ingin belajar tentang berbagai topik komputer dan IT.
    PIKTI menyediakan berbagai macam kursus seperti office automation, web, design, mobile programming, game, dan networking."
    piko shout "PIKTI juga menyediakan jadwal yang fleksibel, jadi kamu bisa mengambil kursus kapanpun kamu mau."
    piko frown blush "Setelah mengikuti kursus selama 1 tahun, kamu akan mendapatkan sertifikat."

    show piko smile blush
    "Oh wow, keren banget!"

    piko shout "Iya kan!. Kalau kamu punya teman atau keluarga yang ingin belajar tentang komputer dan IT,
    kamu bisa kasih tau mereka untuk datang ke PIKTI."

    show piko frown blush
    "Pasti sih. Terima kasih ya informasinya!"

    piko shout blush "Sama-sama!"
    show piko smile blush

    menu pikti_menu:

        "Keluar dari PIKTI":
            jump south_1f_corridor

label lab_pascasarjana:
    scene bg lab pasca with fade:
        zoom 1.9 yalign 0.5

    "Hmm Aku kira Informatika ITS cuma ada 7 lab buat masing-masing RMK"
    "Tapi ternyata ada juga lab buat mahasiswa pascasarjana."

    menu lab_pascasarjana_menu:

        "Keluar dari Lab Pascasarjana":
            jump south_1f_corridor

label east_1f_corridor:
    scene bg east 1st floor corridor with fade:
        zoom 1.9 yalign 0.7

    menu east_1f_corridor_menu:
        "Kamu sedang berada di koridor timur. Ke mana kamu ingin pergi?"

        "↑ Pergi ke lounge selatan":
            jump south_1f_lounge
        
        "↓ Pergi ke lounge utara":
            jump north_1f_lounge       

label north_3f_lounge:
    scene bg north 3rd floor lounge with fade:
        zoom 1.9 yalign 0.6

    menu north_3f_lounge_menu:
        "Kamu sedang berada di lounge utara. Ke mana kamu ingin pergi?"

        "→ Lihat kantor HMTC":
            jump hmtc

        "↘ Turun ke lantai pertama":
            jump north_2f_lounge

        "← Pergi ke koridor utara":
            jump north_3f_corridor

        "↓ Pergi ke koridor timur":
            jump east_3f_corridor
        
label south_3f_lounge:
    scene bg south 3rd floor lounge ext with fade:
        zoom 1.9

    menu south_3f_lounge_menu:
        "Kamu sedang berada di lounge selatan. Ke mana kamu ingin pergi?"

        "↙ Turun ke lantai ketiga":
            jump south_2f_lounge

        "→ Pergi ke koridor selatan":
            jump south_3f_corridor

        "↓ Pergi ke koridor timur":
            jump east_3f_corridor

label hmtc:
    scene bg hmtc ext with fade:
        zoom 1.9

    "Hmmm... Jadi disini kantor HMTC."

    show tica open:
        zoom 1.0 pos(0, 0.1)

    tica open "Yep bener!"

    show tica smile blush
    "Anjir! Muncul dari mana kamu?"

    tica open blush "Haha, maaf maaf. Tapi iya bener, HMTC biasanya ngejalanin program mereka di sini."
    tica open "Kayanya kamu udah tahu, tapi HMTC sebenernya itu singkatan dari Himpunan Mahasiswa Teknik Computer-Informatika. Udah tahu belum?"

    show tica frown
    "Sebenernya.. belum tahu sih. Tapi itu beneran?"

    tica closed open blush "Iya bener! Sejarahnya sebenarnya dimulai tahun 1989 pas HMTC pertama kali didirikan. Jurusannya dulu masih disebut Teknik Komputer."
    tica closed open "Tapi kayaknya HMTK udah dipake sama Teknik Kimia. Jadi mereka cuma pake Teknik Computer aja. Dan pas jurusan kemudian ganti nama lagi jadi Informatika, mereka cuma tambahin kata itu ke namanya!"

    show tica smile
    "Menarik! Kamu tau banyak banget tentang HMTC!"

    tica closed open blush "Haha... Itu cuma soalnya aku bosen di kost dan mulai baca-baca di internet."

    show tica frown blush
    "Minggu-minggu depan ini kamu gak bakalan bosen lagi sih wkwk"

    tica open "Bener bener haha..."

    show tica closed smile

    menu hmtc_menu:

        "Keluar dari kantor HMTC":
            jump north_3f_lounge

label north_3f_corridor:
    scene bg north 3rd floor corridor with fade:
        zoom 1.9 yalign 0.8

    menu north_3f_corridor_menu:
        "Kamu sedang berada di koridor utara. Ke mana kamu ingin pergi?"

        "← Masuk ke lab LP1":
            jump lp1

        "← Masuk ke lab KCV":
            jump kcv

        "← Masuk ke lab KBJ":
            jump kbj

        "← Masuk ke lab RPL":
            jump rpl

        "↑ Pergi ke lounge utara":
            jump north_3f_lounge

label lp1:
    scene bg lp1 ext with fade:
        zoom 1.9 yalign 0.2

    show siji frown closed:
        zoom 1.2 pos(0, 0.15)

    siji open smile closed "Hai hai! Namaku Siji! Hehehe..."
    siji open smile "Udah capek belum keliling Informatika? Mudah mudahan nggak yaa..."
    siji smile blush"Jadi.. sekarang kamu lagi di LP2. Apa tuh LP2? LP2 itu singkatan dari Laboratorium Pemrograman 2."
    siji open smile blush "Kalau kamu udah ke LP1, LP2 ini gak jauh beda sama LP1. LP2 ini juga laboratorium workshop!"
    siji open smile closed blush "Nah iyaa, jadi nanti di kuliah ada beberapa matkul yang bakal ada praktikumnya.
    Nah praktikumnya bakal diadain di lab ini."
    siji frown blush "Nanti biasanya sebelum praktikum, ada beberapa kelas yang diadain sama asisten matkul kalian. 
    Setelah beberapa minggu, barulah kalian praktikum!"
    siji open smile closed "Tenang aja gak usah takut sama praktikum hehehe... Mas mbak asistennya baik baik dan bakal ngajarin kalian sampai bisa kok!"
    siji open smile "Oh iya, sama kaya LP1 juga, kalau lab ini gak dipake kamu bisa aja kesini buat ngerjain tugas."
    siji frown closed blush "Nah.. udah paham kan?? Hehehe..."

    show siji smile blush closed

    menu lp1_menu:

        "Keluar dari lab LP1":
            jump north_3f_corridor

label kcv:
    scene bg kcv ext with fade:
        zoom 1.9

    show sivi closed smile:
        zoom 0.9 pos(0, 0.1)

    sivi open "Selamat datang!! Aku Sivi dari lab KCV!"
    sivi open blush "KCV itu singkatan Komputer Cerdas dan Visi. Ini adalah salah satu dari 7 RMK di Informatika ITS."
    sivi frown blush "Di RMK KCV kita belajar tentang Artificial Intelligence dan Computer Vision."
    sivi closed open "Mata kuliah wajib yang kamu akan ambil di RMK ini ada Kecerdasan Buatan dan Kecerdasan Komputasi.
    Di mata kuliah ini kamu akan belajar dasar-dasar AI."
    sivi closed open blush "Tapi ada juga mata kuliah pilihan yang bisa kamu ambil, seperti Pengolahan Citra Digital, Data Mining, Visi Komputer, dan banyak lagi."
    sivi open "Kalau kamu tertarik dengan AI dan CV, kamu bisa gabung ke lab KCV!"

    show sivi closed smile

    menu kcv_menu:

        "Keluar dari lab KCV":
            jump north_3f_corridor

label kbj:
    scene bg kbj ext with fade:
        zoom 1.9 yalign 0.1

    show jara closed smile:
        zoom 0.9 pos(0, 0.1)

    jara open "Selamat datang di lab KBJ! Aku akan jadi guide kamu hari ini. Oh, dan namaku Jara."
    jara closed open "KBJ adalah salah satu dari 7 RMK di Informatika ITS. Singkatan dari Komputer Berbasis Jaringan."
    jara open blush "Seperti namanya, RMK ini fokus ke infrastruktur dan aplikasi jaringan."
    jara blush smile "Ada satu mata kuliah wajib yang kamu akan ambil di RMK ini, yaitu Keamanan Informasi dan Jaringan."
    jara closed open blush "Mata kuliah lainnya pilihan. Ada Forensik Digital, Komputasi Awan, Sistem Terdistribusi, dan banyak lagi."
    jara open "Saat ini kami sedang membuka lowongan admin untuk lab kami. Kalau kamu tertarik, kamu bisa kontak aku nanti."

    show jara closed smile

    menu kbj_menu:

        "Keluar dari lab KBJ":
            jump north_3f_corridor

label rpl:
    scene bg rpl ext 2 with fade:
        zoom 1.9 yalign 0.2

    show rika closed open blush:
        zoom 0.9 pos(0.7, 0.1)

    rika open blush "Haloooo... Aku Rikaa! Aku admin di lab RPL ini. Jadi aku bakal jelasin tentang apa itu lab RPL!"
    rika open "Mungkin udah pada tahu kan, RPL itu singkatan dari Rekayasa Perangkat Lunak. RPL ini salah satu dari 7 RMK di Informatika"
    rika closed open "Dari namanya udah jelas ya... RPL ini fokus ke software development. 
    Ada beberapa mata kuliah yang wajib diambil di RMK ini, 
    yaitu Analisis dan Perancangan Sistem Informasi, Manajemen Pengembangan Perangkat Lunak, Rekayasa Kebutuhan, dan Arsitektur Perangkat Lunak."
    rika closed open blush "Selain itu, kalau kamu tertarik dengan software development, ada juga mata kuliah pilihan yang bisa kamu ambil nanti misanya Evolusi Perangkat Lunak, Penjaminan Mutu Perangkat Lunak dan lainnya!"
    rika closed frown "Kalau kamu tertarik banget, kami lagi buka lowongan admin nihh... Kami tunggu ya!"

    show rika smile

    menu rpl_menu:

        "Keluar dari lab RPL":
            jump north_3f_corridor

label south_3f_corridor:
    scene bg south 3rd floor corridor with fade:
        zoom 1.9 yalign 0.8

    menu south_3f_corridor_menu:
        "Kamu sedang berada di koridor selatan. Ke mana kamu ingin pergi?"

        "↓ Pergi ke lounge selatan":
            jump south_3f_lounge

        "← Masuk ke lab LP2":
            jump lp2

        "← Masuk ke lab Alpro":
            jump alpro

        "← Masuk ke lab MI":
            jump mi

label lp2:
    scene bg lp2 ext with fade:
        zoom 1.9 yalign 0.2

    show lara closed smile blush:
        zoom 0.9 pos(0.65, 0.1)

    lara closed open blush "Hai! Selamat datang di lab LP2!"
    lara closed open "Namaku Lara, dan aku akan ngejelasin lab ini hari ini."
    lara open blush "LP2 berarti Laboratorium Pemrograman 2. Ini adalah salah satu dari 2 lab workshop di Informatika ITS."
    lara smile blush "Yang satunya lagi adalah LP1, yang ada di koridor selatan."
    lara open "Nanti kamu akan menggunakan lab ini untuk praktikum mata kuliah."
    lara frown "Biasanya, akan ada kelas sebelum praktikum, juga diadakan di lab ini, oleh asisten kelas kamu."
    lara open blush"Setelah itu, minggu-minggu depannya kamu akan diberi tugas untuk praktikum sendiri."
    lara closed smile "Kamu juga bisa datang ke lab ini kapan aja buat ngerjain praktikumnya, tapi kamu harus pastikan bahwa tidak ada kelas yang lagi berlangsung."
    lara closed open "Di semester pertama ini, sebenarnya ada kelas dengan praktikum. Aku yakin kita bakal ketemu lagi nanti!"

    show lara closed smile blush

    menu lp2_menu:

        "Keluar dari lab LP2":
            jump south_3f_corridor

label alpro:
    scene bg alpro ext with fade:
        zoom 1.9 yalign 0.2

    show alga closed smile:
        zoom 0.9 pos(0.65, 0.1)

    alga open "Halo! Yak kalian sekarang lagi di lab Alpro. Namaku Alga, aku bakal jelasin tentang lab ini."
    alga open blush "Alpro itu singkatan ya.. Algoritma dan Pemrograman. Alpro itu RMK yang fokus ke algoritma dan pemrograman."
    alga closed open "Matkul wajib kalian nanti paling banyak dari Alpro. Ya karena emang fokus Alpro tadi yaitu pemrograman."
    alga closed smile blush "Di semester pertama ini nanti kalian bakal dapet matkul Dasar Pemrograman. Di semester 2 ada Struktur data."
    alga closed open blush"Di tahun-tahun berikutnya bakal ada matkul Pemrograman Berorientasi Objek, Pemrograman Web, Perancangan dan Analisis Algoritma, dan lainnya."
    alga frown "Kalau kalian tertarik dengan pemrograman atau mungkin ada yang udah kenal competitive programming, kalian bisa gabung kami!"

    show alga smile blush

    menu alpro_menu:

        "Exit Alpro lab":
            jump south_3f_corridor

label mi:
    scene bg mi ext 2 with fade:
        zoom 1.9 yalign 0.2

    show mana upset blush:
        zoom 1.0 pos(0.6, 0)

    mana upset "Halo halo.. Jadi selamat datang di lab MI. Oke langsung aja ya MI itu kepanjangan dari Manajemen Informasi."
    mana smile "Eh iya namaku Mana. Lanjut. Jadi MI ini RMK di Informatika. MI itu tuh fokus ke pengembangan sistem dan manajemen informasi."
    mana upset blush "Beda sama yang lain, disini gak ada matkul wajib. Kalian bakal ketemu MI di matkul pilihan nanti."
    mana neutral blush "Di MI ada matkul pilihan Sistem Enterprise, Rekayasa Pengetahuan, Sistem Informasi Geografis, Audit Sistem, Tata Kelola Teknologi Informasi, Basis Data Terdistribusi, sama Big Data."
    mana upset blush "Udah sih itu aja. Udah paham kan? Iya udah ya. Oh iya kami lagi oprec admin, jadi kalau minta join aja."

    show mana neutral

    menu mi_menu:

        "Keluar dari lab MI":
            jump south_3f_corridor

label east_3f_corridor:
    scene bg east 3rd floor corridor with fade:
        zoom 1.9 yalign 0.8

    menu east_3f_corridor_menu:
        "Kamu sedang berada di koridor timur. Ke mana kamu ingin pergi?"

        "↑ Pergi ke lounge utara":
            jump north_3f_lounge

        "↓ Pergi ke lounge selatan":
            jump south_3f_lounge

        "→ Masuk ke lab AJK":
            jump ajk

        "→ Masuk ke lab IGS":
            jump igs

label ajk:
    scene bg ajk ext 3 with fade:
        zoom 1.9 yalign 0.3

    show arsi smile:
        zoom 0.9 pos(0.05, 0.15)

    arsi open blush "Apa ini kok rame? Hah? Oh iya lupa lupa maaffff..."
    arsi frown blush "Iya iya maaf yaa.. hehe.. aku Arsi. Aku admin di lab AJK ini.. Salam kenal.."
    arsi open "Hmm oke.. jadi langsung jelasin nih? Oke oke... Jadi... AJK itu singkatan dari Arsitektur dan Jaringan Komputer."
    arsi open blush"Udah tahu kan ya AJK itu juga RMK di Informatika? Jadi AJK ini fokus ke arsitektur dan jaringan komputer."
    arsi smile blush "Disini ada matkul wajib juga yang harus kalian ambil. Matkulnya itu.... bentar lupa.. oh iya.. hehe maaf ya... ada Sistem Digital, Organisasi Komputer, Sistem Operasi, sama satu lagi... Jaringan Komputer."
    arsi smile "Nah kalau kalian tertarik sama RMK ini, kalian juga bisa tuh nanti ambil matkul pilihannya. Ada Jaringan Nirkabel, Teknologi Antar Jaringan, IoT, sama Perancangan Keamanan Sistem dan Jaringan.."
    arsi frown "Oke oke.. udah paham kan? Haha.. oke oke.. maaf ya kalau aku kurang jelas.. hehe.."
    arsi open blush"Kalau kalian pengen tau lebih lanjut tentang AJK, kalian bisa tanya ke admin lab AJK ini.. hehe.."
    arsi open "Atau kalian juga bisa gabung jadi admin disini.. hehe.."

    show arsi smile blush

    menu ajk_menu:

        "Keluar dari lab AJK":
            jump east_3f_corridor

label igs:
    scene bg igs ext with fade:
        zoom 1.9 yalign 0.1

    show fika smile blush:
        zoom 1.0 pos(0.05, 0.1)

    fika open "Haii!! Namaku Fikaa dan selamat datang di lab IGS!!!!"
    fika open blush "Maaf ya, aku sedikit excited banget ketemu kalian semua haha...."
    fika smile "Okay okay, jadiii, IGS itu singkatan dari Interaksi, Grafika, dan Seni. Dan yess, IGS ini salah satu RMK di Informatika kita."
    fika open "Dari namanya tadi.... bisa tebak gak apa yang kita pelajari di lab ini? Ga ada yang bisa? Haha, oke oke, aku kasih tau tenang."
    fika frown "Oke seperti namanya, kita belajar tentang interaksi dan grafika komputer. Keren banget kan??"
    fika open "Jadi, kita ada 2 matkul wajib yang bakal kalian ambil di RMK ini. Yang pertama itu Interaksi Manusia dan Komputer, dan yang kedua Grafika Komputer."
    fika open blush "Di Interaksi Manusia dan Komputer kalian bakal belajar tentang bagaimana cara membuat user interface yang baik, dan bagaimana cara membuat interaksi yang baik antara user dan komputer."
    fika smile blush "Jadi di Informatika kita pengen kalian gak cuma bisa membuat program yang bagus, tapi juga bisa membuat program yang mudah digunakan."
    fika open "Kalau di Grafika Komputer, kalian bakal belajar.. yaa.. grafika komputer! Kalian bakal belajar tentang gimana kerja cahaya, simulasi fisika, dan lainnya!. Dan ya... FI-SI-KA! Jadi pasttin kalian fokus di kelas fisika semester ini ya!"
    fika frown blush "Dan kita juga ada beberapa matkul pilihan yang kalian bisa ambil. Contohnya ada Teknik Pengembangan Game, Sistem Game, AR/VR, Animasi Komputer dan Pemodelan 3D, dan banyak lagi."
    fika open blush "Jadi... kalo kalian suka game, dan... suka bikin game, kalian bakal suka banget di lab ini!"

    show fika smile blush

    menu igs_menu:

        "Keluar dari lab IGS":
            jump east_3f_corridor