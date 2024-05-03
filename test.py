import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.sidebar.image('https://raw.githubusercontent.com/Nurantiika01/Aplikasi_perhitungan_estimasi_ketidakpastian/main/nur1.png.png')
st.sidebar.header("WELCOME TO PROGRAM")
st.sidebar.subheader("KELOMPOK 2")


with st.sidebar:
    selected2 = option_menu ('Menu', ['Program Aplikasi Perhitungan μ VT', 'Program Aplikasi Perhitungan μ FP'])


# with st.sidebar:
#     selected = option_menu('DATA', ['Program Aplikasi', 'program lpk'])



    
if (selected2 == 'Program Aplikasi Perhitungan μ VT'):
    def hitung():
        st.title('Aplikasi Perhitungan μ ET')

        volume_rata_rata_mL = st.number_input("Masukan nilai volume rata-rata(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_rata_rata_mL)
        delta_suhu = st.number_input("Masukan nilai delta suhu(℃)",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu)
        koefisien_muai_air = st.number_input("Masukkan nilai koefisien muai air(℃)",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air)
    

        tombol = st.button("Hitung nilai μ ET(mL)")

        if tombol:
            nilai_μ_ET = (volume_rata_rata_mL*delta_suhu*koefisien_muai_air)/1.73205
            st.success(f"Nilai μ ET (mL) adalah {nilai_μ_ET}")
            st.balloons()
    
    
    
    def hitung1():
        st.title('Aplikasi Perhitungan μ Vendpoit')

        skala_terkecil_buret_mL = st.number_input("Masukan nilai skala terkecil buret(mL)",key="skala_terkecil_buret_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(skala_terkecil_buret_mL)
        delta_suhu_1 = st.number_input("Masukan nilai delta suhu(℃)",key="delta_suhu_1",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu_1)
        koefisien_muai_air_1 = st.number_input("Masukkan nilai koefisien muai air(℃)",key="koefisien_muai_air_1",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_1)

        tombol = st.button("Hitung nilai μ Vendpoit(mL)")

        if tombol:
            nilai_μ_Vendpoit = (skala_terkecil_buret_mL*delta_suhu*koefisien_muai_air)/1.73205
            st.success(f"Nilai μ Vendpoit (mL) adalah {nilai_μ_Vendpoit}")
            st.balloons()

    def hitung2():
        st.title('Aplikasi Perhitungan μ Volume Titran')

        miu_kal_buret_mL = st.number_input("Masukan nilai μ kalibrasi buret(mL)",key="miu_kal_buret_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_kal_buret_mL)
        miu_ET_mL= st.number_input("Masukan nilai μ ET(mL)",key="miu_ET_mL",value=None, placeholder='Ketikkan angka...')
        st.write(miu_ET_mL)
        miu_Vendpoint_mL = st.number_input("Masukan nilai μ Vendpoint(mL)",key="miu_Vendpoint_mL",value=None, placeholder='Ketikkan angka....')
        st.write(miu_Vendpoint_mL)

        tombol = st.button("Hitung nilai μ Vtitran(mL)")

        if tombol:
            nilai_μ_VT = (((miu_kal_buret_mL)**2)+((miu_ET_mL)**2)+((miu_Vendpoint_mL)**2))**0.5
            st.success(f"Nilai μ Volume Titran (mL) adalah {nilai_μ_VT}")
            st.balloons()


    tab1,tab2,tab3 = st.tabs(["Perhitungan μ ET", "Perhitungan μ Vendpoit","Perhitungan μ VT"])
    with tab1:
        tab1.write(hitung())
    with tab2:
        tab2.write(hitung1())
    with tab3:
        tab3.write(hitung2())
    



if (selected2 == 'Program Aplikasi Perhitungan μ FP'):
    def hitung3():
        st.title('Aplikasi Perhitungan μ pipet')

        miu_kal_pipet_mL = st.number_input("Masukan nilai μ kalibrasi pipet(mL)",key="miu_kal_pipet_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_kal_pipet_mL)
        volume_pipet_mL = st.number_input("Masukan nilai volume pipet(mL)",key="volume_pipet_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_pipet_mL)
        delta_suhu_2 = st.number_input("Masukan nilai delta suhu(℃)",key="delta_suhu_2",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu_2)
        koefisien_muai_air_2 = st.number_input("Masukkan nilai koefisien muai air(℃)",key="koefisien_muai_air_2",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_2)
        

        tombol = st.button("Hitung nilai μ pipet(mL)")

        if tombol:
            nilai_μ_pipet = (((miu_kal_pipet_mL/1.73205)**2)+((volume_pipet_mL*delta_suhu_3*koefisien_muai_air_3/1.73205)**2))**0.5
            st.success(f"Nilai μ pipet adalah {nilai_μ_pipet}")
            st.balloons()



    def hitung4():
        st.title('Aplikasi Perhitungan μ labu takar')

        miu_kal_labu_takar_mL = st.number_input("Masukan nilai μ kalibrasi labu takar(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_kal_labu_takar_mL)
        volume_labu_takar_mL_2 = st.number_input("Masukan nilai volume labu takar(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_labu_takar_mL_2)
        delta_suhu_4 = st.number_input("Masukan nilai delta suhu(℃)",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu_4)
        koefisien_muai_air_4 = st.number_input("Masukkkan nilai koefisien muai air(℃)",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_4)
        

        tombol = st.button("Hitung nilai μ labu takar(mL)")

        if tombol:
            nilai_μ_labu_takar = (((miu_kal_labu_takar_mL/1.73205)**2)+((volume_labu_takar_mL_2*delta_suhu_4*koefisien_muai_air_4/1.73205)**2))**0.5
            st.success(f"Nilai μ labu takar (mL) adalah {nilai_μ_labu_takar }")
            st.balloons()


    def hitung5():
        st.title('Aplikasi Perhitungan μ FP')

        faktor_pengali_2 = st.number_input("Masukan nilai faktor pengali",key="faktor_pengali_2",value=None, placeholder='Ketikkan angka...' )
        st.write(faktor_pengali_2)    
        miu_labu_takar = st.number_input("Masukan nilai μ labu takar",key="miu_labu_takar",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_labu_takar)
        volume_labu_takar_mL = st.number_input("Masukan nilai volume labu takar(mL)",key="volume_labu_takar_mL",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_labu_takar_mL)
        miu_ET_mL_2= st.number_input("Masukan nilai μ ET(mL)",key="miu_ET_mL_2",value=None, placeholder='Ketikkan angka...')
        st.write(miu_ET_mL_2)
    
        tombol = st.button("Hitung nilai μ FP")

        if tombol:
            nilai_μ_FP = faktor_pengali_2*(((miu_labu_takar/volume_labu_takar)**2)+((miu_ET_mL)**2))**0.5
            st.success(f"Nilai μ FP adalah {nilai_μ_FP}")
            st.balloons()


    tab1,tab2,tab3 = st.tabs(["Perhitungan μ pipet", "Perhitungan μ labu takar","Perhitungan μ FP"])
    with tab1:
        tab1.write(hitung3())
    with tab2:
        tab2.write(hitung4())
    with tab3:
        tab3.write(hitung5())
