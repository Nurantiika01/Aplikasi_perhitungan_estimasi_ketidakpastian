import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.sidebar.image('https://raw.githubusercontent.com/Nurantiika01/Aplikasi_perhitungan_estimasi_ketidakpastian/main/akabogor.png.png')
st.sidebar.header("WELCOME TO PROGRAM")
st.sidebar.subheader("KELOMPOK 2")
st.sidebar.text("""
        1. Afif Dwi Julianandi (@shdwind_)
        2. Hanan Dhiya Arrumaisha (@hanndhy.arr)
        3. Muhammad Haikel Assidqi (@mhaikel_a)
        4. Nuranti Ika Wulandari (@nurantiikaw_)
        5. Sahla Aulia (@shlayaa_)
        """)


with st.sidebar:
    selected2 = option_menu ('Menu', ['Tentang kami','Pengertian','Perhitungan μ Volume Titran', 'Perhitungan μ Faktor Pengali'])


# with st.sidebar:
#     selected = option_menu('DATA', ['Program Aplikasi', 'program lpk'])


if (selected2 == 'Tentang kami'):
        st.header("WELCOME TO PROGRAM")
        st.subheader("KELOMPOK 2")
        st.text("""
                1. Afif Dwi Julianandi	        NIM 2360061
                2. Hanan Dhiya Arrumaisha	NIM 2360135
                3. Muhammad Haikel Assidqi	NIM 2360186
                4. Nuranti Ika Wulandari	NIM 2360219
                5. Sahla Aulia                  NIM 2360250
                """)

if (selected2 == 'Pengertian'):
        st.title('Apa Itu Estimasi Ketidakpastian???')
        st.write('Estimasi ketidakpastian adalah aspek kritis dalam analisis data yang memungkinkan peneliti dan praktisi untuk mengukur seberapa tidak pastinya hasil pengukuran atau perhitungan. Dalam era sekarang ini dimana keputusan seringkali didasarkan pada data dan analisis, pemahaman yang mendalam tentang ketidakpastian menjadi semakin penting. Konsep ketidakpastian memiliki aplikasi yang luas di berbagai bidang, termasuk fisika, kimia, biologi, teknik, ekonomi dan banyak lagi. Dalam bidang kimia analis, ketidakpastian membantu dalam penafsiran hasil eksperimen atau praktikum dan memvalidasi teori. Aplikasi ini membantu para pengambil keputusan untuk memahami risiko yang terkait dengan berbagai pilihan yang tersedia. Dengan pemahaman yang baik tentang ketidakpastian, keputusan dapat dibuat secara lebih informan dan berbasis data. Dalam era digital yang terus berkembang, kemampuan dalam pemrograman komputer menjadi semakin penting. Pemahaman yang kuat tentang logika pemrograman adalah fondasi yang diperlukan untuk mengembangkan program komputer yang efektif dan efisien. Selain itu, dalam konteks analisis data, khususnya dalam pembuatan laporan estimasi ketidakpastian, perlunya perhitungan yang teliti dan akurat semakin mendesak.')

    
if (selected2 == 'Perhitungan μ Volume Titran'):
    def hitung():
        st.title('μ kalibrasi Buret')
        st.image('https://raw.githubusercontent.com/Nurantiika01/Aplikasi_perhitungan_estimasi_ketidakpastian/main/kalburet.png.jpg')
            
        plus_minus_buret_mL = st.number_input("Masukan nilai ±buret (mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(plus_minus_buret_mL)

        tombol = st.button("Hitung nilai μ Kalibrasi Buret(mL)")

        if tombol:
            nilai_μ_kalibrasi_buret =  plus_minus_buret_mL/1.73205
            st.success(f"Nilai μ Kalibrasi Buret (mL) adalah {nilai_μ_kalibrasi_buret:.2f}")
            st.balloons()


    def hitung1():
        st.title('μ Efek Temperatur')

        volume_rata_rata_mL = st.number_input("Masukan nilai volume rata-rata(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_rata_rata_mL)
        delta_suhu = st.number_input("Masukan nilai delta suhu(℃)",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu)
        koefisien_muai_air = st.number_input("Masukkan nilai koefisien muai air(℃)",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air)
    

        tombol = st.button("Hitung nilai μ Efek Temperatur(mL)")

        if tombol:
            nilai_μ_Efek_Temperatur = (volume_rata_rata_mL*delta_suhu*koefisien_muai_air)/1.73205
            st.success(f"Nilai μ Efek Temperatur (mL) adalah {nilai_μ_Efek_Temperatur:.4f}")
            st.balloons()
    
    
    
    def hitung2():
        st.title('μ Volume Endpoint')

        skala_terkecil_buret_mL = st.number_input("Masukan nilai skala terkecil buret(mL)",key="skala_terkecil_buret_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(skala_terkecil_buret_mL)
        delta_suhu_1 = st.number_input("Masukan nilai delta suhu(℃)",key="delta_suhu_1",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu_1)
        koefisien_muai_air_1 = st.number_input("Masukkan nilai koefisien muai air(℃)",key="koefisien_muai_air_1",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_1)

        tombol = st.button("Hitung nilai μ Volume Endpoint(mL)")

        if tombol:
            nilai_μ_Volume_Endpoint = (skala_terkecil_buret_mL*delta_suhu_1*koefisien_muai_air_1)/1.73205
            st.success(f"Nilai μ Volume Endponit (mL) adalah {nilai_μ_Volume_Endpoint:.5f}")
            st.balloons()
                
          

    def hitung3():
        tombol = st.button("Hitung nilai μ Volume Titran(mL)")

        if tombol:
            nilai_μ_Volume_Titran = (((nilai_μ_kalibrasi_buret)**2)+((nilai_μ_Efek_Temperatur)**2)+((nilai_μ_Volume_Endpoint)**2))**0.5
            st.success(f"Nilai μ Volume Titran (mL) adalah {nilai_μ_Volume_Titran}")
            st.balloons()
       


    tab1,tab2,tab3,tab4 = st.tabs(["Perhitungan μ kalibrasi buret", "Perhitungan μ Efek Temperatur", "Perhitungan μ Volume Endpoint","Perhitungan μ Volume Titran"])
    with tab1:
        tab1.write(hitung())
    with tab2:
        tab2.write(hitung1())
    with tab3:
        tab3.write(hitung2())
    with tab4:
        tab4.write(hitung3())
    



if (selected2 == 'Perhitungan μ Faktor Pengali'):
    def hitung4():
        st.title('μ Pipet')

        miu_kal_pipet_mL = st.number_input("Masukan nilai μ kalibrasi pipet(mL)",key="miu_kal_pipet_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_kal_pipet_mL)
        volume_pipet_mL = st.number_input("Masukan nilai volume pipet(mL)",key="volume_pipet_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_pipet_mL)
        delta_suhu_2 = st.number_input("Masukan nilai delta suhu(℃)",key="delta_suhu_2",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu_2)
        koefisien_muai_air_2 = st.number_input("Masukkan nilai koefisien muai air(℃)",key="koefisien_muai_air_2",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_2)
        

        tombol = st.button("Hitung nilai μ Pipet(mL)")

        if tombol:
            nilai_μ_Pipet = (((miu_kal_pipet_mL/1.73205)**2)+((volume_pipet_mL*delta_suhu_2*koefisien_muai_air_2/1.73205)**2))**0.5
            st.success(f"Nilai μ Pipet (mL) adalah {nilai_μ_Pipet}")
            st.balloons()
            



    def hitung5():
        st.title('μ Labu Takar')

        miu_kal_labu_takar_mL = st.number_input("Masukan nilai μ kalibrasi labu takar(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_kal_labu_takar_mL)
        volume_labu_takar_mL_2 = st.number_input("Masukan nilai volume labu takar(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_labu_takar_mL_2)
        delta_suhu_4 = st.number_input("Masukan nilai delta suhu(℃)",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu_4)
        koefisien_muai_air_4 = st.number_input("Masukkkan nilai koefisien muai air(℃)",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_4)
        

        tombol = st.button("Hitung nilai μ Labu Takar(mL)")

        if tombol:
            nilai_μ_Labu_Takar = (((miu_kal_labu_takar_mL/1.73205)**2)+((volume_labu_takar_mL_2*delta_suhu_4*koefisien_muai_air_4/1.73205)**2))**0.5
            st.success(f"Nilai μ Labu Takar (mL) adalah {nilai_μ_Labu_Takar}")
            st.balloons()
         


    def hitung6():
        st.title('μ Faktor Pengali')

        faktor_pengali_2 = st.number_input("Masukan nilai faktor pengali",key="faktor_pengali_2",value=None, placeholder='Ketikkan angka...' )
        st.write(faktor_pengali_2)    
        miu_labu_takar_mL = st.number_input("Masukan nilai μ labu takar(mL)",key="miu_labu_takar_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_labu_takar_mL)
        volume_labu_takar_mL = st.number_input("Masukan nilai volume labu takar(mL)",key="volume_labu_takar_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_labu_takar_mL)
        miu_pipet_mL= st.number_input("Masukan nilai μ pipet(mL)",key="miu_pipet_mL_2",value=None, placeholder='Ketikkan angka...')
        st.write(miu_pipet_mL)
        volume_pipet_mL_1 = st.number_input("Masukan nilai volume pipet(mL)",key="volume_pipet_mL_1",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_pipet_mL_1)
        
        tombol = st.button("Hitung nilai μ Faktor Pengali")

        if tombol:
            nilai_μ_Faktor_Pengali = faktor_pengali_2*(((miu_labu_takar_mL/volume_labu_takar_mL)**2)+((miu_pipet_mL/volume_pipet_mL_1)**2))**0.5
            st.success(f"Nilai μ Faktor Pengali adalah {nilai_μ_Faktor_Pengali}")
            st.balloons()
               


    tab1,tab2,tab3 = st.tabs(["Perhitungan μ Pipet", "Perhitungan μ Labu Takar","Perhitungan μ Faktor Pengali"])
    with tab1:
        tab1.write(hitung4())
    with tab2:
        tab2.write(hitung5())
    with tab3:
        tab3.write(hitung6())
