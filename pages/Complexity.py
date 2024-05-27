import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import time
from models.sos_game import SOSGame

def measure_time(game, depth):
    start_time = time.time()
    game.bot_move(depth)
    end_time = time.time()
    return end_time - start_time

def analyze_complexity(selected_page):
    st.title("Complexity Analysis")
    st.write("Welcome to the Complexity Analysis page.")
    
    if selected_page == "Complexity Analysis":
        if st.button("Mulai analisa"):
            dimensions = 3
            difficulties = {
                'Easy': 1,
                'Medium': 2,
                'Impossible': 3
            }
            
            times = {
                'Easy': [],
                'Medium': [],
                'Impossible': []
            }
            
            for difficulty, depth in difficulties.items():
                for _ in range(10):
                    game = SOSGame(dimensions)
                    game.initialize_game('S')
                    elapsed_time = measure_time(game, depth)
                    times[difficulty].append(elapsed_time)
            
            avg_times = {difficulty: sum(times[difficulty])/len(times[difficulty]) for difficulty in difficulties}
            
            # Membuat DataFrame
            df = pd.DataFrame(avg_times.values(), index=avg_times.keys(), columns=['Average Time (seconds)'])
            
            # Debug: Tampilkan DataFrame
            st.write("### Hasil Analisa Kompleksitas Waktu Game SOS")
            st.write(df)
            
            # Menampilkan range slider
            n = st.slider('Depth (n)', 1, 27, 3)
            
            # Debug: Tampilkan nilai n
            st.write(f"Selected depth (n): {n}")
            
            # Memperbarui DataFrame berdasarkan nilai n yang dipilih
            df_updated = df.apply(lambda x: x * (8 ** (n - 3)))
            
            # Debug: Tampilkan DataFrame yang diperbarui
            st.write("### Hasil Analisa Kompleksitas Waktu Game SOS Setelah Perubahan Nilai n")
            st.write(df_updated)
            
            # Menambahkan plot untuk memvisualisasikan perubahan
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(df_updated.index, df_updated['Average Time (seconds)'], color='skyblue')
            ax.set_xlabel('Difficulty')
            ax.set_ylabel('Average Time (seconds)')
            ax.set_title('Perbandingan Waktu Rata-rata Setelah Perubahan Nilai n')
            
            # Debug: Pastikan bahwa plt.show() tidak dipanggil
            st.pyplot(fig)
def main():
    st.title("Analisis Kompleksitas Game SOS")
    st.write("Selamat datang di halaman Analisis Kompleksitas.")

    if st.button("Tampilkan Analisis"):
        dimensions = 3
        difficulties = {
            'Easy': 1,
            'Medium': 2,
            'Impossible': 3
        }
        
        times = {
            'Easy': [],
            'Medium': [],
            'Impossible': []
        }
        
        for difficulty, depth in difficulties.items():
            for _ in range(10):
                game = SOSGame(dimensions)
                game.initialize_game('S')
                elapsed_time = measure_time(game, depth)
                times[difficulty].append(elapsed_time)
        
        avg_times = {difficulty: sum(times[difficulty])/len(times[difficulty]) for difficulty in difficulties}
        
        # Membuat DataFrame
        df = pd.DataFrame(avg_times.values(), index=avg_times.keys(), columns=['Average Time (seconds)'])
        
        # Debug: Tampilkan DataFrame
        st.write("### Hasil Analisa Kompleksitas Waktu Game SOS")
        st.write(df)
        
        # Menambahkan plot untuk memvisualisasikan perubahan sebagai grafik garis
        fig, ax = plt.subplots(figsize=(10, 6))
        df.plot(kind='line', ax=ax, marker='o')
        ax.set_xlabel('Difficulty')
        ax.set_ylabel('Average Time (seconds)')
        ax.set_title('Perbandingan Waktu Rata-rata Berdasarkan Kesulitan Permainan')
        ax.legend(['Easy', 'Medium', 'Impossible'])
        
        # Debug: Pastikan bahwa plt.show() tidak dipanggil
        st.pyplot(fig)

if __name__ == "__main__":
    main()
