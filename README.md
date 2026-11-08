# Proyek Lab Sains Data (P8): Dari Keputusan ke Data

- **Nama & NIM:**
- Lufthansa Daffa Gilbran (12010223140054)
- Ghiffari Muhammad (12010223140015)
- Muhammad Indra Mulya (12010223140067)
- **Program Studi:** S1 Bisnis Digital FEB Universitas Diponegoro

## 1. Lembar Rencana Data (1 Halaman)
- **KEPUTUSAN:** Tim produk memutuskan 1 fitur prioritas untuk dibangun pada rilis aplikasi layanan/jasa kampus sebelum Pertemuan 12.
- **PILIHAN:** A (Pelacakan status & kurir real-time) | B (Transparansi harga & garansi di muka) | C (Tetap seperti sekarang via WhatsApp)
- **ANGKA PEMBEDA:** Proporsi keluhan pengguna: persentase keluhan "ketidakpastian waktu/pengiriman/status" (dukung A) vs "ketidakjelasan harga/kualitas" (dukung B).
- **AMBANG:** Pilih A bila >35% ulasan negatif terkait waktu/status; pilih B bila >35% terkait harga/kualitas; pilih C bila total keduanya <15%.
- **DATA:** >=300 teks ulasan pelanggan berbahasa Indonesia (untuk memetakan topik keluhan & uji akurasi AI di P9).
- **SUMBER KANDIDAT:** (1) IndoNLU SmSA Dataset; (2) PRDECT-ID Mendeley Data; (3) YouTube Data API v3.
- **UBAH PILIHAN?:** Proporsi topik keluhan: YA | Data PDRB Jateng 10 tahun: TIDAK, DICORET | Survei umum "suka aplikasi jasa?": TIDAK, DICORET.
- **LAMPU DATA:** HIJAU (Dataset terbuka & sudah dianonimkan sesuai UU PDP No. 27 Tahun 2022).
- **JIKA TIDAK ADA:** Gunakan kombinasi dataset terbuka dari katalog NusaCrowd / IndoNLU dan PRDECT-ID.

## 2. Verifikasi 5 Sumber Usulan AI (DeepSeek & Qwen)
1. **IndoNLU SmSA Dataset** (`github.com/indobenchmark/indonlu`) -> Status: Hijau, Tautan hidup -> **PAKAI**
2. **PRDECT-ID Dataset** (`doi:10.1016/j.dib.2022.108554`) -> Status: Hijau, CC BY 4.0 -> **PAKAI**
3. **YouTube Data API v3** (`developers.google.com/youtube/v3`) -> Status: Kuning ke Hijau -> **PAKAI (Cadangan)**
4. **Statistik E-Commerce BPS** (`bps.go.id`) -> Status: Hijau, Tautan hanya beranda -> **CEK DULU**
5. **Dataset Ulasan Jasa Kampus Kaggle 2025** -> Status: Merah, Tautan 404 Not Found (Halusinasi AI) -> **TOLAK**
- **Persentase Usulan AI yang Salah:** 20% ditolak mutlak (halusinasi tautan), 20% perlu pencarian tabel manual.

## 3. Catatan Asal-Usul Data (README_data)
- **SUMBER:** IndoNLU - SmSA (`https://github.com/indobenchmark/indonlu/tree/master/dataset/smsa_doc-sentiment-prosa`)
- **TANGGAL AMBIL:** 7 November 2026
- **CARA AMBIL:** Unduh terprogram via Python (`ambil_data.py`)
- **PARAMETER:** Bahasa Indonesia; pemisah tab; sampel acak konsisten (`n=350`, `random_state=42`)
- **JUMLAH BARIS:** Mentah total 11.000 baris -> Sampel bersih 350 baris, 3 kolom
- **LISENSI/ATURAN:** Open-source akademik (Wilie dkk., AACL-IJCNLP 2020)
- **ANONIMISASI:** Pre-processed + regex `@username` menjadi `[USER]` (Status: HIJAU)
- **AI YANG DIPAKAI:** Gemini, DeepSeek, Qwen
- **VALIDASI:** Diisi di P9 (uji 50 sampel manual vs label AI)
- **KETERBATASAN:** Mencakup ulasan lintas layanan umum sehingga pada P9 akan diklasifikasikan ke topik spesifik.

## 4. Eksplorasi AI Video/Motion (Remotion / Seedance / Sunra) & AI Harness
- **Claude Motion / Remotion:** Pembuatan video/animasi presentasi data secara terprogram berbasis React.
- **Seedance & Sunra:** Eksplorasi workflow text-to-video generatif untuk aset visual studio AI.
- **AI Harness:** Eksekusi skrip langsung di folder proyek lokal (`INSTRUKSI_HARNESS.md` + `ambil_data.py`).

## 5. Log AI
- **DeepSeek & Qwen:** Mencari 5 sumber data ulasan Indonesia -> Diperiksa manual, 1 tautan 404 ditolak.
- **Gemini:** Menyusun Lembar Rencana Data & skrip pengambil sampel 350 baris -> Diverifikasi jumlah baris CSV.
