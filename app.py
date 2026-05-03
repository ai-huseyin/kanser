import streamlit as st
from fpdf import FPDF

def render_risk_progress(level: str):
    progress_map = {"Düşük": 20, "Orta": 50, "Yüksek": 90}
    st.progress(progress_map.get(level, 0))
    st.markdown(f"**Risk Seviyesi:** {level}")


def render_maps_button():
    st.markdown(
        '<a href="https://www.google.com/maps/search/onkoloji+hastanesi/" target="_blank" rel="noreferrer">'
        '<button type="button">📍 En Yakın Onkoloji Merkezini Bul</button>'
        '</a>',
        unsafe_allow_html=True,
    )


def create_pdf(kanser_turu):
    safe_turu = (
        kanser_turu
        .replace("ı", "i")
        .replace("ş", "s")
        .replace("ğ", "g")
        .replace("ç", "c")
        .replace("ö", "o")
        .replace("ü", "u")
        .replace("İ", "I")
        .replace("Ş", "S")
        .replace("Ğ", "G")
        .replace("Ç", "C")
        .replace("Ö", "O")
        .replace("Ü", "U")
    )
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 12, "Yapay Zeka Kanser Tarama Platformu", ln=True, align="C")
    pdf.ln(6)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Klinik Degerlendirme Raporu - {safe_turu}", ln=True, align="C")
    pdf.ln(24)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(
        0,
        8,
        "Bu rapor tibbi tani amaci tasimaz; yalnizca risk degerlendirmesi icin hazirlanmistir.",
    )
    return bytes(pdf.output())

st.set_page_config(
    page_title="Yapay Zeka Kanser Tarama Platformu",
    page_icon="🫁",
    layout="wide",
)

secim = st.sidebar.selectbox(
    "Kanser Türünü Seçin",
    ["Akciğer", "Meme", "Kolon", "Prostat", "Mide"],
)

st.sidebar.markdown(
    '<div style="background:#ffebee;color:#d32f2f;border-radius:10px;padding:12px;margin-bottom:16px;text-align:center;">'
    '⚠️ Bu sorular tıbbi tanı amacı taşımaz; yalnızca kanser risk değerlendirmesi için hazırlanmıştır.'
    '</div>',
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    '<div style="text-align:center; margin-bottom:16px;">'
    '  <div style="font-weight:bold; font-size:1rem; margin-bottom:8px;">👨‍💻 Uygulamada Emeği Geçenler</div>'
    '  <div style="font-weight:bold;">Hüseyin Ahmet Altun</div>'
    '  <div style="font-weight:bold;">Yasin Efe Demir</div>'
    '  <div style="font-weight:bold;">Kemal Yılmaz</div>'
    '</div>',
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    '<div style="background:#e0f2f1;color:#00695c;border-radius:10px;padding:12px;margin-bottom:12px;text-align:center;">'
    '  <div style="font-weight:bold; font-size:1rem; margin-bottom:8px;">🔒 %100 Gizlilik Odaklı</div>'
    '  <div>Sağlık verileriniz hiçbir sunucuya aktarılmaz, cihazınızda anlık olarak işlenir.</div>'
    '</div>'
    '<div style="text-align:center;">'
    '  <div style="font-weight:bold;">Yapay Zeka Risk Analiz Motoru</div>'
    '  <div>Sürüm 1.1.0 | © 2026</div>'
    '</div>',
    unsafe_allow_html=True,
)

if 'form_id' not in st.session_state:
    st.session_state.form_id = 0

st.title("Yapay Zeka Kanser Tarama Platformu")


if secim == "Akciğer":
    st.subheader("🫁 Akciğer Kanseri Risk Analiz Platformu")
    if 'akciger_form_id' not in st.session_state:
        st.session_state.akciger_form_id = 0

    with st.expander("ℹ️ Risk Analizi ve Kategori Rehberi", expanded=True):
        st.markdown(
            "Bu platform, yanıtlarınızı tıbbi bir karar ağacı algoritmasından geçirerek size özel bir risk skoru hesaplar. "
            "Soruların başındaki renk kodları şu anlama gelmektedir:"
        )
        st.markdown(
            "🔴 Kırmızı Bayraklar: Doğrudan tümör veya ciddi tahribat şüphesi taşıyan acil durum sinyalleridir."
        )
        st.markdown(
            "🟡 Klinik Semptomlar: Vücudun verdiği genel alarm durumlarıdır. Bir araya geldiklerinde risk oluştururlar."
        )
        st.markdown(
            "🟢 Risk Çarpanları: Genetik ve çevresel geçmişinizdir. Tek başlarına tanı koydurmaz ancak mevcut semptomların ağırlığını katlar."
        )
        st.markdown("### Hesaplama Mantığı (Nasıl Çalışır?)")
        st.markdown(
            "🔴 Yüksek Risk (Kırmızı Uyarı): Formda en az 1 tane Kırmızı Bayrak (🔴) sorusuna VEYA en az 3 tane Klinik Semptom (🟡) sorusuna \"Evet\" yanıtı verirseniz sistem acil durum alarmı verir. "
            "(Ayrıca risk çarpanlarının yoğunluğu da semptomları tetikleyip kırmızı alarma sebep olabilir)."
        )
        st.markdown(
            "🟡 Orta Risk (Sarı Uyarı): Herhangi bir kırmızı bayrağınız yoksa, ancak 1 veya 2 tane Klinik Semptom (🟡) sorusuna \"Evet\" dediyseniz sistem yakın takip (orta risk) uyarısı verir."
        )
        st.markdown(
            "🟢 Düşük Risk (Yeşil Uyarı): Aktif bir semptomunuz (🔴 veya 🟡) yoksa sonuç düşük risk çıkar. Ancak Risk Çarpanlarınız (🟢) bulunuyorsa, sistem size koruyucu önlemler almanız için özel bir uyarı mesajı gösterir."
        )

    st.markdown("---")
    st.markdown("### Klinik Değerlendirme Formu")
    with st.form(key=f"akciger_form_{st.session_state.akciger_form_id}"):
        q1 = st.radio(
            "🟡 1. Üç haftadan uzun süredir devam eden ve karakteri giderek değişen (şiddetlenen) bir öksürüğünüz var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q1_{st.session_state.akciger_form_id}",
        )
        q2 = st.radio(
            "🔴 2. Öksürük krizleri sırasında balgamınızda kan, pas rengi veya kırmızı ince çizgiler fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q2_{st.session_state.akciger_form_id}",
        )
        q3 = st.radio(
            "🟡 3. Son zamanlarda sesinizde açıklanamayan bir kısıklık, çatallanma veya kalınlaşma meydana geldi mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q3_{st.session_state.akciger_form_id}",
        )
        q4 = st.radio(
            "🟡 4. Derin nefes alırken, gülerken veya öksürürken göğsünüzde veya sırtınızda keskin bir ağrı hissediyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q4_{st.session_state.akciger_form_id}",
        )
        q5 = st.radio(
            "🟡 5. Merdiven çıkmak gibi daha önce rahatça yaptığınız günlük aktivitelerde artık nefes darlığı çekiyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q5_{st.session_state.akciger_form_id}",
        )
        q6 = st.radio(
            "🟡 6. Nefes alıp verirken göğsünüzden hırıltı, ıslık veya hışıltı benzeri sesler geliyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q6_{st.session_state.akciger_form_id}",
        )
        q7 = st.radio(
            "🟡 7. İstirahat halindeyken dahi omuzlarınıza, kürek kemiklerinize veya kolunuza vuran geçmeyen bir ağrınız var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q7_{st.session_state.akciger_form_id}",
        )
        q8 = st.radio(
            "🟡 8. Son 6 ay içinde diyet yapmadığınız halde istemsizce 4-5 kilonun üzerinde ağırlık kaybettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q8_{st.session_state.akciger_form_id}",
        )
        q9 = st.radio(
            "🟡 9. Parmak uçlarınızda genişleme, tırnaklarınızda bombeleşme (çomak parmak görünümü) fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q9_{st.session_state.akciger_form_id}",
        )
        q10 = st.radio(
            "🟡 10. Sık sık zatürre, bronşit gibi solunum yolu enfeksiyonları geçiriyor ve bu hastalıkları zor mu atlatıyorsunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q10_{st.session_state.akciger_form_id}",
        )
        q11 = st.radio(
            "🟡 11. Yutkunurken boğazınızda veya göğsünüzün arkasında takılma/ağrı hissediyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q11_{st.session_state.akciger_form_id}",
        )
        q12 = st.radio(
            "🔴 12. Boyun bölgenizde veya köprücük kemiğinizin hemen üzerindeki çukurlukta ele gelen şişlik/beze var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q12_{st.session_state.akciger_form_id}",
        )
        q13 = st.radio(
            "🟡 13. Sabahları uyandığınızda yüzünüzde, boynunuzda veya kollarınızda olağandışı bir şişlik (ödem) oluyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q13_{st.session_state.akciger_form_id}",
        )
        q14 = st.radio(
            "🔴 14. Göz kapağınızda düşme, göz bebeğinizde küçülme ve yüzünüzün tek tarafında terleme kaybı (Horner Sendromu belirtileri) fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q14_{st.session_state.akciger_form_id}",
        )
        q15 = st.radio(
            "🟡 15. Dinlenmekle dahi geçmeyen, sabahları yataktan kalkmanızı zorlaştıran bir bitkinlik hali yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q15_{st.session_state.akciger_form_id}",
        )
        q16 = st.radio(
            "🟢 16. Aktif olarak sigara, nargile, puro veya elektronik sigara kullanıyor musunuz? (Veya geçmişte 10 yıldan fazla kullandınız mı?)",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q16_{st.session_state.akciger_form_id}",
        )
        q17 = st.radio(
            "🟢 17. Kendiniz kullanmasanız bile, uzun yıllar boyunca kapalı ortamda yoğun sigara dumanına (pasif içicilik) maruz kaldınız mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q17_{st.session_state.akciger_form_id}",
        )
        q18 = st.radio(
            "🟢 18. Çalışma hayatınızda asbest, radon gazı, uranyum, kömür tozu veya ağır kimyasallara maruz kaldığınız bir iş yaptınız mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q18_{st.session_state.akciger_form_id}",
        )
        q19 = st.radio(
            "🟢 19. Birinci veya ikinci derece kan bağınız olan akrabalarınızda akciğer kanseri teşhisi konmuş birileri var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q19_{st.session_state.akciger_form_id}",
        )
        q20 = st.radio(
            "🟢 20. Daha önce KOAH (Kronik Obstrüktif Akciğer Hastalığı), amfizem veya verem (tüberküloz) tedavisi gördünüz mü?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"q20_{st.session_state.akciger_form_id}",
        )

        col1, col2 = st.columns(2)
        risk_submitted = col1.form_submit_button("Risk Analizi Yap")
        clear_button = col2.form_submit_button("Formu Temizle")

        if clear_button:
            st.session_state.akciger_form_id += 1
            st.rerun()

        if risk_submitted:
            kategori_a_sayisi = sum(
                1 for answer in [q2, q12, q14] if answer == "Evet"
            )
            kategori_b_sayisi = sum(
                1
                for answer in [
                    q1,
                    q3,
                    q4,
                    q5,
                    q6,
                    q7,
                    q8,
                    q9,
                    q10,
                    q11,
                    q13,
                    q15,
                ]
                if answer == "Evet"
            )
            kategori_c_sayisi = sum(
                1 for answer in [q16, q17, q18, q19, q20] if answer == "Evet"
            )

            if (
                kategori_a_sayisi >= 1
                or kategori_b_sayisi >= 3
                or (kategori_b_sayisi >= 1 and kategori_c_sayisi >= 2)
            ):
                render_risk_progress("Yüksek")
                st.error(
                    "Belirtileriniz akciğer sağlığınız açısından detaylı bir inceleme gerektirmektedir. "
                    "Lütfen vakit kaybetmeden bir Göğüs Hastalıkları veya Tıbbi Onkoloji uzmanına başvurunuz."
                )
                show_map = True
            elif kategori_b_sayisi == 1 or kategori_b_sayisi == 2:
                render_risk_progress("Orta")
                st.warning(
                    "Şikayetleriniz şu an için akut bir alarm seviyesinde görünmese de, akciğer sağlığınızı korumak adına "
                    "bu belirtilerin 2-3 haftadan uzun sürmesi halinde bir Göğüs Hastalıkları uzmanına muayene olmanızı öneririz."
                )
                show_map = True
            else:
                render_risk_progress("Düşük")
                risk_ek = (
                    "risk faktörleriniz bulunduğundan dolayı "
                    if kategori_c_sayisi >= 1
                    else ""
                )
                st.success(
                    f"Mevcut yanıtlarınıza göre akciğer kanserine yönelik belirgin bir şüphe saptanmamıştır. Ancak {risk_ek}"
                    "akciğer sağlığınızı korumak için sigarasız bir yaşam ve düzenli sağlık kontrollerinizi ihmal etmeyiniz."
                )
                show_map = False

    if risk_submitted:
        if show_map:
            col_download, col_map = st.columns([2, 1])
            with col_download:
                st.download_button(
                    "📄 Sonuclari Raporla (PDF)",
                    data=create_pdf(secim),
                    file_name="kanser_raporu.pdf",
                    mime="application/pdf",
                )
            with col_map:
                render_maps_button()
        else:
            st.download_button(
                "📄 Sonuclari Raporla (PDF)",
                data=create_pdf(secim),
                file_name="kanser_raporu.pdf",
                mime="application/pdf",
            )

elif secim == "Meme":
    st.subheader("🎗️ Meme Kanseri Risk Analiz Platformu")
    if 'meme_form_id' not in st.session_state:
        st.session_state.meme_form_id = 0

    with st.expander("ℹ️ Risk Analizi ve Kategori Rehberi", expanded=True):
        st.markdown(
            "Bu platform, yanıtlarınızı tıbbi bir karar ağacı algoritmasından geçirerek size özel bir meme kanseri risk skoru hesaplar. "
            "Soruların başındaki renk kodları şu anlama gelmektedir:"
        )
        st.markdown(
            "🔴 Kırmızı Bayraklar: Doğrudan tümör veya ciddi tahribat şüphesi taşıyan acil durum sinyalleridir."
        )
        st.markdown(
            "🟡 Klinik Semptomlar: Vücudun verdiği genel alarm durumlarıdır. Bir araya geldiklerinde risk oluştururlar."
        )
        st.markdown(
            "🟢 Risk Çarpanları: Genetik ve çevresel geçmişinizdir. Tek başlarına tanı koydurmaz ancak mevcut semptomların ağırlığını katlar."
        )
        st.markdown("### Hesaplama Mantığı (Nasıl Çalışır?)")
        st.markdown(
            "🔴 Yüksek Risk (Kırmızı Uyarı): Formda en az 1 tane Kırmızı Bayrak (🔴) sorusuna VEYA en az 2 tane Klinik Semptom (🟡) sorusuna \"Evet\" yanıtı verirseniz sistem acil durum alarmı verir. "
            "Ayrıca 1 tane Klinik Semptom ve en az 2 tane Risk Çarpanı olduğunda da risk artışı söz konusudur."
        )
        st.markdown(
            "🟡 Orta Risk (Sarı Uyarı): Herhangi bir kırmızı bayrağınız yoksa ancak 1 tane Klinik Semptom (🟡) sorusuna \"Evet\" dediyseniz sistem yakın takip (orta risk) uyarısı verir."
        )
        st.markdown(
            "🟢 Düşük Risk (Yeşil Uyarı): Aktif bir semptomunuz (🔴 veya 🟡) yoksa sonuç düşük risk çıkar. Ancak Risk Çarpanlarınız (🟢) bulunuyorsa, sistem size koruyucu önlemler almanız için özel bir uyarı mesajı gösterir."
        )

    st.markdown("---")
    st.subheader(" Klinik Değerlendirme Formu")
    with st.form(key=f"meme_form_{st.session_state.meme_form_id}"):
        m_q1 = st.radio(
            "🔴 1. Meme dokusunda yeni veya hızla büyüyen bir kitle gördünüz veya elle hissedebildiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q1_{st.session_state.meme_form_id}",
        )
        m_q2 = st.radio(
            "🟡 2. Memede ağrı, batma, dolgunluk hissi veya dokununca hassasiyet yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q2_{st.session_state.meme_form_id}",
        )
        m_q3 = st.radio(
            "🔴 3. Meme ucundan kendiliğinden kanlı, sarımsı veya şeffaf akıntı geliyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q3_{st.session_state.meme_form_id}",
        )
        m_q4 = st.radio(
            "🔴 4. Meme cildinde portakal kabuğu görünümü, çökme veya kalınlaşma fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q4_{st.session_state.meme_form_id}",
        )
        m_q5 = st.radio(
            "🔴 5. Koltuk altı veya köprücük kemiği çevresinde ele gelen şişlik veya bezeler var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q5_{st.session_state.meme_form_id}",
        )
        m_q6 = st.radio(
            "🟡 6. Meme ucunda içe çekilme, şekil değişikliği veya renk değişikliği fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q6_{st.session_state.meme_form_id}",
        )
        m_q7 = st.radio(
            "🟡 7. Memede uzun süredir devam eden çıban, yara veya kızarıklık var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q7_{st.session_state.meme_form_id}",
        )
        m_q8 = st.radio(
            "🔴 8. Meme cildinde sürekli kaşıntı, döküntü veya iltihaplanma belirtileri gözlemlediniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q8_{st.session_state.meme_form_id}",
        )
        m_q9 = st.radio(
            "🟡 9. Meme veya koltuk altı bölgesinde uzun süredir inatçı şişlik ya da dolgunluk hissediyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q9_{st.session_state.meme_form_id}",
        )
        m_q10 = st.radio(
            "🟡 10. Memede adet döneminden bağımsız sürekli dolgunluk veya gerilme hissediyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q10_{st.session_state.meme_form_id}",
        )
        m_q11 = st.radio(
            "🟡 11. Daha önce memede kitle, kist veya fibroadenom gibi şikayetleriniz oldu mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q11_{st.session_state.meme_form_id}",
        )
        m_q12 = st.radio(
            "🟡 12. Meme cerrahisi, biyopsi veya tedavi geçmişiniz var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q12_{st.session_state.meme_form_id}",
        )
        m_q13 = st.radio(
            "🔴 13. Meme ucunda çökme, yara oluşumu veya cilde yapışma gibi değişiklik fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q13_{st.session_state.meme_form_id}",
        )
        m_q14 = st.radio(
            "🟢 14. Aile fertlerinizde meme kanseri veya yumurtalık kanseri öyküsü var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q14_{st.session_state.meme_form_id}",
        )
        m_q15 = st.radio(
            "🟢 15. Daha önce hormonal tedavi, uzun süreli doğum kontrol hapı kullanımı veya menopoz sonrası hormon replasman tedavisi gördünüz mü?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q15_{st.session_state.meme_form_id}",
        )
        m_q16 = st.radio(
            "🟢 16. 40 yaşın üzerinde misiniz veya menopoz sonrası dönemde misiniz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q16_{st.session_state.meme_form_id}",
        )
        m_q17 = st.radio(
            "🟢 17. Daha önce göğüs radyasyon tedavisi aldınız mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q17_{st.session_state.meme_form_id}",
        )
        m_q18 = st.radio(
            "🟡 18. Memede adet döngüsü dışı ani değişim veya kalıcı farklılıklar gözlemlediniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q18_{st.session_state.meme_form_id}",
        )
        m_q19 = st.radio(
            "🟢 19. Obezite, hareketsizlik veya yüksek yağlı diyet gibi risk faktörleriniz var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q19_{st.session_state.meme_form_id}",
        )
        m_q20 = st.radio(
            "🟢 20. Daha önce meme kanseri taraması dışında düzenli olarak mamografi veya ultrason yaptırdınız mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"m_q20_{st.session_state.meme_form_id}",
        )

        col1, col2 = st.columns(2)
        risk_submitted_meme = col1.form_submit_button(" Risk Analizi Yap")
        clear_button_meme = col2.form_submit_button(" Formu Temizle")

        if clear_button_meme:
            st.session_state.meme_form_id += 1
            st.rerun()

        if risk_submitted_meme:
            kat_a_meme = sum(
                1 for answer in [m_q1, m_q3, m_q4, m_q5, m_q8, m_q13] if answer == "Evet"
            )
            kat_b_meme = sum(
                1
                for answer in [
                    m_q2,
                    m_q6,
                    m_q7,
                    m_q9,
                    m_q10,
                    m_q11,
                    m_q12,
                    m_q18,
                ]
                if answer == "Evet"
            )
            kat_c_meme = sum(
                1 for answer in [m_q14, m_q15, m_q16, m_q17, m_q19, m_q20] if answer == "Evet"
            )

            if kat_a_meme >= 1 or kat_b_meme >= 2 or (kat_b_meme == 1 and kat_c_meme >= 2):
                render_risk_progress("Yüksek")
                st.error(
                    "Yanıtlarınız bir meme kanseri risk değerlendirmesi için acil inceleme gerektirebilir. "
                    "Lütfen mümkün olan en kısa sürede Genel Cerrahi veya Tıbbi Onkoloji uzmanına başvurunuz."
                )
                show_map = True
            elif kat_b_meme == 1:
                render_risk_progress("Orta")
                st.warning(
                    "Şikayetleriniz şu an için doğrudan acil alarm seviyesinde görünmese de, meme sağlığınız için "
                    "yakın takip ve uzman muayenesi önerilir."
                )
                show_map = True
            else:
                render_risk_progress("Düşük")
                risk_ek_meme = (
                    " Ancak risk faktörleriniz bulunduğu için düzenli mamografi kontrollerinizi ihmal etmeyin."
                    if kat_c_meme >= 1
                    else ""
                )
                st.success(
                    f"Mevcut yanıtlarınıza göre meme kanserine yönelik belirgin bir şüphe saptanmamıştır.{risk_ek_meme}"
                )
                show_map = False

    if risk_submitted_meme:
        if show_map:
            col_download, col_map = st.columns([2, 1])
            with col_download:
                st.download_button(
                    "📄 Sonuclari Raporla (PDF)",
                    data=create_pdf(secim),
                    file_name="kanser_raporu.pdf",
                    mime="application/pdf",
                )
            with col_map:
                render_maps_button()
        else:
            st.download_button(
                "📄 Sonuclari Raporla (PDF)",
                data=create_pdf(secim),
                file_name="kanser_raporu.pdf",
                mime="application/pdf",
            )

elif secim == "Kolon":
    st.subheader("🧬 Kolon Kanseri Risk Analiz Platformu")
    if 'kolon_form_id' not in st.session_state:
        st.session_state.kolon_form_id = 0

    with st.expander("ℹ️ Risk Analizi ve Kategori Rehberi", expanded=True):
        st.markdown(
            "Bu platform, yanıtlarınızı tıbbi bir karar ağacı algoritmasından geçirerek size özel bir kolon kanseri risk skoru hesaplar. "
            "Soruların başındaki renk kodları şu anlama gelmektedir:"
        )
        st.markdown(
            "🔴 Kırmızı Bayraklar: Doğrudan tümör veya ciddi tahribat şüphesi taşıyan acil durum sinyalleridir."
        )
        st.markdown(
            "🟡 Klinik Semptomlar: Vücudun verdiği genel alarm durumlarıdır. Bir araya geldiklerinde risk oluştururlar."
        )
        st.markdown(
            "🟢 Risk Çarpanları: Genetik ve çevresel geçmişinizdir. Tek başlarına tanı koydurmaz ancak mevcut semptomların ağırlığını katlar."
        )
        st.markdown("### Hesaplama Mantığı (Nasıl Çalışır?)")
        st.markdown(
            "🔴 Yüksek Risk (Kırmızı Uyarı): Formda en az 1 tane Kırmızı Bayrak (🔴) sorusuna VEYA en az 3 tane Klinik Semptom (🟡) sorusuna \"Evet\" yanıtı verirseniz sistem acil durum alarmı verir. "
            "Ayrıca 1 tane Klinik Semptom ve en az 2 tane Risk Çarpanı olduğunda da risk artışı söz konusudur."
        )
        st.markdown(
            "🟡 Orta Risk (Sarı Uyarı): Herhangi bir kırmızı bayrağınız yoksa ancak 1 tane Klinik Semptom (🟡) sorusuna \"Evet\" dediyseniz sistem yakın takip (orta risk) uyarısı verir."
        )
        st.markdown(
            "🟢 Düşük Risk (Yeşil Uyarı): Aktif bir semptomunuz (🔴 veya 🟡) yoksa sonuç düşük risk çıkar. Ancak Risk Çarpanlarınız (🟢) bulunuyorsa, sistem size koruyucu önlemler almanız için özel bir uyarı mesajı gösterir."
        )

    st.subheader(" Klinik Değerlendirme Formu")
    with st.form(key=f"kolon_form_{st.session_state.kolon_form_id}"):
        k_q1 = st.radio(
            "🟡 1. Son birkaç aydır tuvalete çıkma alışkanlıklarınızda (rutin dışı uzun süreli kabızlık veya ishal) belirgin bir değişim oldu mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q1_{st.session_state.kolon_form_id}",
        )
        k_q2 = st.radio(
            "🔴 2. Kabızlık ve ishal durumlarının birbirini takip ettiği (birkaç gün kabız, ardından ishal) düzensiz döngüler yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q2_{st.session_state.kolon_form_id}",
        )
        k_q3 = st.radio(
            "🟡 3. Dışkınızın şeklinde bir incelme (kurşun kalem veya şerit gibi ince çıkma) fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q3_{st.session_state.kolon_form_id}",
        )
        k_q4 = st.radio(
            "🟡 4. Dışkılamadan hemen sonra bile bağırsağınızın tam boşalmadığı, tekrar tuvalete gitme hissi (tenesmus) yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q4_{st.session_state.kolon_form_id}",
        )
        k_q5 = st.radio(
            "🟡 5. Dışkınızın üzerinde veya tuvalet kağıdında parlak kırmızı, taze kan gördünüz mü?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q5_{st.session_state.kolon_form_id}",
        )
        k_q6 = st.radio(
            "🟡 6. Dışkınızın renginde zift gibi simsiyah bir renk, katran benzeri bir kıvam ve çok kötü bir koku fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q6_{st.session_state.kolon_form_id}",
        )
        k_q7 = st.radio(
            "🟡 7. Karın bölgenizde sık sık gaz sancısı, kramp tarzında ağrılar veya açıklanamayan bir şişkinlik oluyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q7_{st.session_state.kolon_form_id}",
        )
        k_q8 = st.radio(
            "🟡 8. Herhangi bir diyet uygulamadığınız halde son 6 ay içinde belirgin ve hızlı bir kilo kaybı yaşadınız mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q8_{st.session_state.kolon_form_id}",
        )
        k_q9 = st.radio(
            "🟡 9. Yapılan kan tahlillerinizde nedeni bulunamayan demir eksikliği anemisi (kansızlık) teşhisi kondu mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q9_{st.session_state.kolon_form_id}",
        )
        k_q10 = st.radio(
            "🟡 10. Sürekli bir uyku hali, merdiven çıkarken nefes nefese kalma ve kronik bir yorgunluk çekiyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q10_{st.session_state.kolon_form_id}",
        )
        k_q11 = st.radio(
            "🟡 11. Midenizde sık sık bulantı veya yemeklerden sonra açıklanamayan kusma nöbetleri yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q11_{st.session_state.kolon_form_id}",
        )
        k_q12 = st.radio(
            "🔴 12. Makat bölgenizde (anüs) ağrı, baskı hissi veya ele gelen bir kitle/şişlik var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q12_{st.session_state.kolon_form_id}",
        )
        k_q13 = st.radio(
            "🟡 13. Yaşınız 50'nin üzerinde mi? (Kolon kanseri riski 50 yaş sonrası belirgin artar).",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q13_{st.session_state.kolon_form_id}",
        )
        k_q14 = st.radio(
            "🔴 14. Birinci derece akrabalarınızda (anne, baba, kardeş, çocuk) kolon kanseri veya bağırsak polibi öyküsü var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q14_{st.session_state.kolon_form_id}",
        )
        k_q15 = st.radio(
            "🟡 15. Daha önce size kolonoskopi yapıldı ve bağırsağınızda adenomatöz polip (et beni) bulunduğu söylendi mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q15_{st.session_state.kolon_form_id}",
        )
        k_q16 = st.radio(
            "🟢 16. Ülseratif Kolit veya Crohn Hastalığı gibi kronik iltihabi bağırsak hastalığı tanınız var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q16_{st.session_state.kolon_form_id}",
        )
        k_q17 = st.radio(
            "🟢 17. Günlük beslenmenizde kırmızı et (dana, kuzu) ve işlenmiş et ürünlerini (sosis, salam, sucuk) çok sık tüketir misiniz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q17_{st.session_state.kolon_form_id}",
        )
        k_q18 = st.radio(
            "🟢 18. Beslenme düzeninizde sebze, meyve ve tam tahıllar (lifli gıdalar) oldukça az bir yer mi kaplıyor?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q18_{st.session_state.kolon_form_id}",
        )
        k_q19 = st.radio(
            "🟢 19. Boyunuza oranla kilonuz belirgin şekilde fazla mı? (Obezite kolon kanseri risk faktörüdür).",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q19_{st.session_state.kolon_form_id}",
        )
        k_q20 = st.radio(
            "🟢 20. Düzenli ve yüksek miktarda alkol tüketiminiz var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"k_q20_{st.session_state.kolon_form_id}",
        )

        col1, col2 = st.columns(2)
        risk_submitted_kolon = col1.form_submit_button("Risk Analizi Yap")
        clear_button_kolon = col2.form_submit_button("Formu Temizle")

        if clear_button_kolon:
            st.session_state.kolon_form_id += 1
            st.rerun()

        if risk_submitted_kolon:
            kat_a_kolon = sum(
                1 for answer in [k_q2, k_q12, k_q14] if answer == "Evet"
            )
            kat_b_kolon = sum(
                1
                for answer in [
                    k_q1,
                    k_q3,
                    k_q4,
                    k_q5,
                    k_q6,
                    k_q7,
                    k_q8,
                    k_q9,
                    k_q10,
                    k_q11,
                    k_q13,
                    k_q15,
                ]
                if answer == "Evet"
            )
            kat_c_kolon = sum(
                1 for answer in [k_q16, k_q17, k_q18, k_q19, k_q20] if answer == "Evet"
            )

            if kat_a_kolon >= 1 or kat_b_kolon >= 3 or (kat_b_kolon >= 1 and kat_c_kolon >= 2):
                render_risk_progress("Yüksek")
                st.error(
                    "Yanıtlarınız bir kolon kanseri risk değerlendirmesi için acil inceleme gerektirebilir. "
                    "Lütfen Gastroenteroloji veya Genel Cerrahi uzmanına mümkün olan en kısa sürede başvurunuz."
                )
                show_map = True
            elif kat_b_kolon >= 1:
                render_risk_progress("Orta")
                st.warning(
                    "Şikayetleriniz şu an için doğrudan acil alarm seviyesinde görünmese de, kolon sağlığınızı korumak için "
                    "yakın takip ve uzman muayenesi önerilir."
                )
                show_map = True
            else:
                render_risk_progress("Düşük")
                risk_ek_kolon = (
                    " Ancak risk faktörleriniz bulunduğu için düzenli kontrollerinizi ihmal etmeyin."
                    if kat_c_kolon >= 1
                    else ""
                )
                st.success(
                    f"Mevcut yanıtlarınıza göre kolon kanserine yönelik belirgin bir şüphe saptanmamıştır.{risk_ek_kolon}"
                )
                show_map = False

    if risk_submitted_kolon:
        if show_map:
            col_download, col_map = st.columns([2, 1])
            with col_download:
                st.download_button(
                    "📄 Sonuclari Raporla (PDF)",
                    data=create_pdf(secim),
                    file_name="kanser_raporu.pdf",
                    mime="application/pdf",
                )
            with col_map:
                render_maps_button()
        else:
            st.download_button(
                "📄 Sonuclari Raporla (PDF)",
                data=create_pdf(secim),
                file_name="kanser_raporu.pdf",
                mime="application/pdf",
            )

elif secim == "Prostat":
    st.subheader("🚹 Prostat Kanseri Risk Analiz Platformu")
    if 'prostat_form_id' not in st.session_state:
        st.session_state.prostat_form_id = 0

    with st.expander("ℹ️ Risk Analizi ve Kategori Rehberi", expanded=True):
        st.markdown(
            "Bu platform, yanıtlarınızı tıbbi bir karar ağacı algoritmasından geçirerek size özel bir prostat kanseri risk skoru hesaplar. "
            "Soruların başındaki renk kodları şu anlama gelmektedir:"
        )
        st.markdown(
            "🔴 Kırmızı Bayraklar: Doğrudan tümör veya ciddi tahribat şüphesi taşıyan acil durum sinyalleridir."
        )
        st.markdown(
            "🟡 Klinik Semptomlar: Vücudun verdiği genel alarm durumlarıdır. Bir araya geldiklerinde risk oluştururlar."
        )
        st.markdown(
            "🟢 Risk Çarpanları: Genetik ve çevresel geçmişinizdir. Tek başlarına tanı koydurmaz ancak mevcut semptomların ağırlığını katlar."
        )
        st.markdown("### Hesaplama Mantığı (Nasıl Çalışır?)")
        st.markdown(
            "🔴 Yüksek Risk (Kırmızı Uyarı): Formda en az 1 tane Kırmızı Bayrak (🔴) sorusuna VEYA en az 3 tane Klinik Semptom (🟡) sorusuna \"Evet\" yanıtı verirseniz sistem acil durum alarmı verir. "
            "Ayrıca 1 tane Klinik Semptom ve en az 2 tane Risk Çarpanı olduğunda da risk artışı söz konusudur."
        )
        st.markdown(
            "🟡 Orta Risk (Sarı Uyarı): Herhangi bir kırmızı bayrağınız yoksa ancak 1 tane Klinik Semptom (🟡) sorusuna \"Evet\" dediyseniz sistem yakın takip (orta risk) uyarısı verir."
        )
        st.markdown(
            "🟢 Düşük Risk (Yeşil Uyarı): Aktif bir semptomunuz (🔴 veya 🟡) yoksa sonuç düşük risk çıkar. Ancak Risk Çarpanlarınız (🟢) bulunuyorsa, sistem size koruyucu önlemler almanız için özel bir uyarı mesajı gösterir."
        )

    st.subheader(" Klinik Değerlendirme Formu")
    with st.form(key=f"prostat_form_{st.session_state.prostat_form_id}"):
        p_q1 = st.radio(
            "🟡 1. Geceleri uyuduktan sonra idrar yapma ihtiyacıyla sık sık (iki veya daha fazla kez) uyanıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q1_{st.session_state.prostat_form_id}",
        )
        p_q2 = st.radio(
            "🔴 2. İdrar yapmaya başlamak için beklemeniz, ıkınmanız veya zorlanmanız gerekiyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q2_{st.session_state.prostat_form_id}",
        )
        p_q3 = st.radio(
            "🟡 3. İdrar tazyikinizde eskisine göre belirgin bir zayıflama, kesik kesik yapma veya çatallanma var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q3_{st.session_state.prostat_form_id}",
        )
        p_q4 = st.radio(
            "🟡 4. İdrarınızı yaptıktan sonra bile mesanenizin tam boşalmadığını, içeride hala idrar kaldığını hissediyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q4_{st.session_state.prostat_form_id}",
        )
        p_q5 = st.radio(
            "🟡 5. İdrar yapma ihtiyacı aniden ve acil olarak geliyor, tuvalete yetişmekte zorlanıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q5_{st.session_state.prostat_form_id}",
        )
        p_q6 = st.radio(
            "🟡 6. İdrar yaparken idrar yolunuzda yanma, sızı veya ağrı (dizüri) hissediyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q6_{st.session_state.prostat_form_id}",
        )
        p_q7 = st.radio(
            "🟡 7. İdrarınızda pembe, kırmızı veya kahverengi renk değişikliği (kanama/hematüri) gördünüz mü?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q7_{st.session_state.prostat_form_id}",
        )
        p_q8 = st.radio(
            "🟡 8. Cinsel ilişki sonrası meninizde (sperm sıvısında) kan, pas rengi veya pembelik fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q8_{st.session_state.prostat_form_id}",
        )
        p_q9 = st.radio(
            "🟡 9. Boşalma (ejakülasyon) sırasında pelvik bölgede veya testislerde derin bir ağrı yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q9_{st.session_state.prostat_form_id}",
        )
        p_q10 = st.radio(
            "🟡 10. Son aylarda daha önce olmayan, açıklanamayan bir sertleşme sorunu (erektil disfonksiyon) yaşamaya başladınız mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q10_{st.session_state.prostat_form_id}",
        )
        p_q11 = st.radio(
            "🟡 11. Makat ile testisler arasındaki bölgede (perine) sürekli bir baskı hissi, dolgunluk veya ağrı var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q11_{st.session_state.prostat_form_id}",
        )
        p_q12 = st.radio(
            "🔴 12. Belinizin alt kısmında, kalçalarınızda veya uyluk (üst bacak) kemiklerinizde derin, künt ve geçmeyen ağrılar hissediyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q12_{st.session_state.prostat_form_id}",
        )
        p_q13 = st.radio(
            "🟡 13. Bacaklarınızda veya ayaklarınızda açıklanamayan şişlikler (ödem) veya zayıflık, uyuşma hissi var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q13_{st.session_state.prostat_form_id}",
        )
        p_q14 = st.radio(
            "🔴 14. Herhangi bir travma yaşamadığınız halde kemiklerinizde kolay kırılmalar veya çatlamalar meydana geldi mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q14_{st.session_state.prostat_form_id}",
        )
        p_q15 = st.radio(
            "🟡 15. İştahsızlık, istemsiz kilo kaybı ve sürekli devam eden bir yorgunluk/halsizlik hali yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q15_{st.session_state.prostat_form_id}",
        )
        p_q16 = st.radio(
            "🟢 16. Yaşınız 50 ve üzerinde mi? (Risk 50 yaştan sonra, özellikle 65 yaş üzerinde belirgin artar).",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q16_{st.session_state.prostat_form_id}",
        )
        p_q17 = st.radio(
            "🟢 17. Babanız, erkek kardeşiniz veya amcanız gibi kan bağınız olan akrabalarınızda prostat kanseri teşhisi konmuş biri var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q17_{st.session_state.prostat_form_id}",
        )
        p_q18 = st.radio(
            "🟢 18. Ailenizdeki kadınlarda erken yaşta görülmüş şiddetli meme kanseri (BRCA gen mutasyonu kaynaklı) öyküsü bulunuyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q18_{st.session_state.prostat_form_id}",
        )
        p_q19 = st.radio(
            "🟢 19. Beslenmenizde doymuş yağlar (kırmızı et, tam yağlı süt ürünleri, margarin) çok yüksek oranda mı yer alıyor?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q19_{st.session_state.prostat_form_id}",
        )
        p_q20 = st.radio(
            "🟢 20. Yakın zamanda kanda PSA (Prostat Spesifik Antijen) testi yaptırdınız mı ve değerleriniz referans aralığının üzerinde mi çıktı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"p_q20_{st.session_state.prostat_form_id}",
        )

        col1, col2 = st.columns(2)
        risk_submitted_prostat = col1.form_submit_button(" Risk Analizi Yap")
        clear_button_prostat = col2.form_submit_button(" Formu Temizle")

        if clear_button_prostat:
            st.session_state.prostat_form_id += 1
            st.rerun()

        if risk_submitted_prostat:
            kat_a_prostat = sum(
                1 for answer in [p_q2, p_q12, p_q14] if answer == "Evet"
            )
            kat_b_prostat = sum(
                1
                for answer in [
                    p_q1,
                    p_q3,
                    p_q4,
                    p_q5,
                    p_q6,
                    p_q7,
                    p_q8,
                    p_q9,
                    p_q10,
                    p_q11,
                    p_q13,
                    p_q15,
                ]
                if answer == "Evet"
            )
            kat_c_prostat = sum(
                1 for answer in [p_q16, p_q17, p_q18, p_q19, p_q20] if answer == "Evet"
            )

            if kat_a_prostat >= 1 or kat_b_prostat >= 3 or (kat_b_prostat >= 1 and kat_c_prostat >= 2):
                render_risk_progress("Yüksek")
                st.error(
                    "Yanıtlarınız bir prostat kanseri risk değerlendirmesi için acil inceleme gerektirebilir. "
                    "Lütfen Üroloji veya Tıbbi Onkoloji uzmanına mümkün olan en kısa sürede başvurunuz ve PSA testi ile prostat muayenesi yaptırınız."
                )
                show_map = True
            elif kat_b_prostat >= 1:
                render_risk_progress("Orta")
                st.warning(
                    "Şikayetleriniz şu an için doğrudan acil alarm seviyesinde görünmese de, prostat sağlığınız için "
                    "yakın takip ve Üroloji uzmanı muayenesi önerilir."
                )
                show_map = True
            else:
                render_risk_progress("Düşük")
                risk_ek_prostat = (
                    " Ancak yaş ve genetik risk faktörleriniz varsa rutin PSA testi takibini ihmal etmeyin."
                    if kat_c_prostat >= 1
                    else ""
                )
                st.success(
                    f"Mevcut yanıtlarınıza göre prostat kanserine yönelik belirgin bir şüphe saptanmamıştır.{risk_ek_prostat}"
                )
                show_map = False

    if risk_submitted_prostat:
        if show_map:
            col_download, col_map = st.columns([2, 1])
            with col_download:
                st.download_button(
                    "📄 Sonuclari Raporla (PDF)",
                    data=create_pdf(secim),
                    file_name="kanser_raporu.pdf",
                    mime="application/pdf",
                )
            with col_map:
                render_maps_button()
        else:
            st.download_button(
                "📄 Sonuclari Raporla (PDF)",
                data=create_pdf(secim),
                file_name="kanser_raporu.pdf",
                mime="application/pdf",
            )

elif secim == "Mide":
    st.subheader("🍽️ Mide Kanseri Risk Analiz Platformu")
    if 'mide_form_id' not in st.session_state:
        st.session_state.mide_form_id = 0

    with st.expander("ℹ️ Risk Analizi ve Kategori Rehberi", expanded=True):
        st.markdown(
            "Bu platform, yanıtlarınızı tıbbi bir karar ağacı algoritmasından geçirerek size özel bir mide kanseri risk skoru hesaplar. "
            "Soruların başındaki renk kodları şu anlama gelmektedir:"
        )
        st.markdown(
            "🔴 Kırmızı Bayraklar: Doğrudan tümör veya ciddi tahribat şüphesi taşıyan acil durum sinyalleridir."
        )
        st.markdown(
            "🟡 Klinik Semptomlar: Vücudun verdiği genel alarm durumlarıdır. Bir araya geldiklerinde risk oluştururlar."
        )
        st.markdown(
            "🟢 Risk Çarpanları: Genetik ve çevresel geçmişinizdir. Tek başlarına tanı koydurmaz ancak mevcut semptomların ağırlığını katlar."
        )
        st.markdown("### Hesaplama Mantığı (Nasıl Çalışır?)")
        st.markdown(
            "🔴 Yüksek Risk (Kırmızı Uyarı): Formda en az 1 tane Kırmızı Bayrak (🔴) sorusuna VEYA en az 3 tane Klinik Semptom (🟡) sorusuna \"Evet\" yanıtı verirseniz sistem acil durum alarmı verir. "
            "Ayrıca 1 tane Klinik Semptom ve en az 2 tane Risk Çarpanı olduğunda da risk artışı söz konusudur."
        )
        st.markdown(
            "🟡 Orta Risk (Sarı Uyarı): Herhangi bir kırmızı bayrağınız yoksa ancak 1 tane Klinik Semptom (🟡) sorusuna \"Evet\" dediyseniz sistem yakın takip (orta risk) uyarısı verir."
        )
        st.markdown(
            "🟢 Düşük Risk (Yeşil Uyarı): Aktif bir semptomunuz (🔴 veya 🟡) yoksa sonuç düşük risk çıkar. Ancak Risk Çarpanlarınız (🟢) bulunuyorsa, sistem size koruyucu önlemler almanız için özel bir uyarı mesajı gösterir."
        )

    st.subheader(" Klinik Değerlendirme Formu")
    with st.form(key=f"mide_form_{st.session_state.mide_form_id}"):
        md_q1 = st.radio(
            "🟡 1. Erken doyma yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q1_{st.session_state.mide_form_id}",
        )
        md_q2 = st.radio(
            "🟡 2. Hazımsızlık veya yemek sonrası devam eden dolgunluk hissi yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q2_{st.session_state.mide_form_id}",
        )
        md_q3 = st.radio(
            "🟡 3. Sık sık mide ağrısı veya yanma hissi oluyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q3_{st.session_state.mide_form_id}",
        )
        md_q4 = st.radio(
            "🟡 4. Yutma güçlüğü, özellikle katı gıdaları geçirme zorluğu yaşanıyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q4_{st.session_state.mide_form_id}",
        )
        md_q5 = st.radio(
            "🟡 5. Bulantı veya kusma şikayetiniz var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q5_{st.session_state.mide_form_id}",
        )
        md_q6 = st.radio(
            "🟡 6. Kusmukta kahve telvesi benzeri koyu, kanlı bir içerik fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q6_{st.session_state.mide_form_id}",
        )
        md_q7 = st.radio(
            "🟡 7. Siyah dışkı veya melena (kanlı, katran gibi dışkı) gözlemlediniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q7_{st.session_state.mide_form_id}",
        )
        md_q8 = st.radio(
            "🟡 8. Et tiksintisi veya et tüketimine ilişkin ani reddetme hissi oluyor mu?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q8_{st.session_state.mide_form_id}",
        )
        md_q9 = st.radio(
            "🟡 9. İştahsızlık yaşıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q9_{st.session_state.mide_form_id}",
        )
        md_q10 = st.radio(
            "🟡 10. Sarılık veya göz/deri renginde sararma fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q10_{st.session_state.mide_form_id}",
        )
        md_q11 = st.radio(
            "🟡 11. Karın bölgesinde belirgin şişlik ya da dolgunluk hissi var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q11_{st.session_state.mide_form_id}",
        )
        md_q12 = st.radio(
            "🔴 12. Boynunuzun sol üst kısmında Virchow nodülü (ele gelen sert, ağrısız lenf bezi) fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q12_{st.session_state.mide_form_id}",
        )
        md_q13 = st.radio(
            "🟡 13. Göbek çevresinde ele gelen kitle veya sertlik fark ettiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q13_{st.session_state.mide_form_id}",
        )
        md_q14 = st.radio(
            "🔴 14. Daha önce Helicobacter pylori enfeksiyonu veya tedavisi öykünüz var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q14_{st.session_state.mide_form_id}",
        )
        md_q15 = st.radio(
            "🟡 15. Salamura, tütsülenmiş veya işlenmiş gıdaları sık tüketiyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q15_{st.session_state.mide_form_id}",
        )
        md_q16 = st.radio(
            "🟢 16. Sebze tüketiminiz düşük mü?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q16_{st.session_state.mide_form_id}",
        )
        md_q17 = st.radio(
            "🟢 17. Aile bireylerinizde mide kanseri öyküsü var mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q17_{st.session_state.mide_form_id}",
        )
        md_q18 = st.radio(
            "🟢 18. Daha önce mide ameliyatı geçirdiniz mi?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q18_{st.session_state.mide_form_id}",
        )
        md_q19 = st.radio(
            "🟢 19. Önceki prekanseröz tanı (örneğin atrofi, metaplazi veya displazi) aldınız mı?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q19_{st.session_state.mide_form_id}",
        )
        md_q20 = st.radio(
            "🟢 20. Sigara kullanıyor musunuz?",
            ["Hayır", "Evet"],
            horizontal=True,
            index=None,
            key=f"md_q20_{st.session_state.mide_form_id}",
        )

        col1, col2 = st.columns(2)
        risk_submitted_mide = col1.form_submit_button("Risk Analizi Yap")
        clear_button_mide = col2.form_submit_button("Formu Temizle")

        if clear_button_mide:
            st.session_state.mide_form_id += 1
            st.rerun()

        if risk_submitted_mide:
            kat_a_mide = sum(
                1 for answer in [md_q1, md_q12, md_q14] if answer == "Evet"
            )
            kat_b_mide = sum(
                1
                for answer in [
                    md_q2,
                    md_q3,
                    md_q4,
                    md_q5,
                    md_q6,
                    md_q7,
                    md_q8,
                    md_q9,
                    md_q10,
                    md_q11,
                    md_q13,
                    md_q15,
                ]
                if answer == "Evet"
            )
            kat_c_mide = sum(
                1 for answer in [md_q16, md_q17, md_q18, md_q19, md_q20] if answer == "Evet"
            )

            if kat_a_mide >= 1 or kat_b_mide >= 3 or (kat_b_mide >= 1 and kat_c_mide >= 2):
                render_risk_progress("Yüksek")
                st.error(
                    "Yanıtlarınız bir mide kanseri risk değerlendirmesi için acil inceleme gerektirebilir. "
                    "Lütfen Gastroenteroloji veya İç Hastalıkları uzmanına mümkün olan en kısa sürede başvurunuz."
                )
                show_map = True
            elif kat_b_mide >= 1:
                render_risk_progress("Orta")
                st.warning(
                    "Şikayetleriniz şu an için doğrudan acil alarm seviyesinde görünmese de, mide sağlığınızı korumak için "
                    "yakın takip ve uzman muayenesi önerilir."
                )
                show_map = True
            else:
                render_risk_progress("Düşük")
                risk_ek_mide = (
                    " Ancak risk faktörleriniz bulunduğundan düzenli takibi ve erken endoskopik değerlendirmeyi ihmal etmeyin."
                    if kat_c_mide >= 1
                    else ""
                )
                st.success(
                    f"Mevcut yanıtlarınıza göre mide kanserine yönelik belirgin bir şüphe saptanmamıştır.{risk_ek_mide}"
                )
                show_map = False

    if risk_submitted_mide:
        if show_map:
            col_download, col_map = st.columns([2, 1])
            with col_download:
                st.download_button(
                    "📄 Sonuclari Raporla (PDF)",
                    data=create_pdf(secim),
                    file_name="kanser_raporu.pdf",
                    mime="application/pdf",
                )
            with col_map:
                render_maps_button()
        else:
            st.download_button(
                "📄 Sonuclari Raporla (PDF)",
                data=create_pdf(secim),
                file_name="kanser_raporu.pdf",
                mime="application/pdf",
            )

if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.expander("💬 Yapay Zeka Sağlık Asistanına Danışın", expanded=False):
    for message in st.session_state.messages:
        if message.get("role") == "user":
            st.chat_message("user").write(message.get("content"))
        else:
            st.chat_message("assistant").write(message.get("content"))

    user_message = st.chat_input("Sorunuzu yazın...")
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})
        assistant_reply = (
            "Merhaba! Ben platformun yapay zeka asistanıyım. Sorduğunuz soruyu anladım. "
            "Ancak sistemin API bağlantısı henüz test aşamasında olduğu için şimdilik sadece bu demo mesajı iletiyorum. "
            "Lütfen unutmayın, ben bir doktor değilim ve tavsiyelerim tıbbi tanı yerine geçmez."
        )
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        for message in st.session_state.messages:
            if message.get("role") == "user":
                st.chat_message("user").write(message.get("content"))
            else:
                st.chat_message("assistant").write(message.get("content"))
