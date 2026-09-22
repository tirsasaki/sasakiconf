#!/usr/bin/env python3
"""
Sasaki Dotfiles Installer
-------------------------
Skrip ini akan membuat symlink atau menyalin konfigurasi dari folder 'dot_files'
ke direktori home kamu (~/).
"""

import os
import shutil
import argparse
from pathlib import Path

def get_home_dir():
    return Path.home()

def get_dotfiles_dir():
    return Path(__file__).parent.resolve() / 'dot_files'

def backup_existing(target: Path):
    if target.exists() or target.is_symlink():
        backup_path = target.with_name(target.name + ".bak")
        if backup_path.exists():
            if backup_path.is_dir() and not backup_path.is_symlink():
                shutil.rmtree(backup_path)
            else:
                backup_path.unlink()
        
        print(f"[*] Mem-backup {target} -> {backup_path}")
        target.rename(backup_path)

def install_item(src: Path, dest: Path, use_copy=False):
    dest.parent.mkdir(parents=True, exist_ok=True)
    backup_existing(dest)
    
    try:
        if use_copy:
            if src.is_dir():
                shutil.copytree(src, dest)
            else:
                shutil.copy2(src, dest)
            print(f"[+] Menyalin: {src.name} -> {dest}")
        else:
            dest.symlink_to(src)
            print(f"[+] Symlink: {src.name} -> {dest}")
    except Exception as e:
        print(f"[!] Gagal memasang {src.name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Install Sasaki Dotfiles")
    parser.add_argument("--copy", action="store_true", help="Gunakan mode copy alih-alih symlink (default: symlink)")
    args = parser.parse_args()

    dot_dir = get_dotfiles_dir()
    home_dir = get_home_dir()

    if not dot_dir.exists():
        print(f"[!] Folder sumber {dot_dir} tidak ditemukan!")
        return

    print("=== Sasaki Dotfiles Installer ===")
    print(f"Mode: {'Copy' if args.copy else 'Symlink'}")
    print("---------------------------------")

    # Mapping custom kalau nama target berbeda dengan sumber
    # Kosongkan list untuk menscan isi dot_files secara dinamis
    print("[*] Memindai direktori dot_files...")
    
    for item in dot_dir.rglob('*'):
        # Lewati .git, backup file, folder assets dan nvim ganda jika ada
        if '.git' in item.parts or 'assets' in item.parts:
            continue
            
        # Kita hanya butuh file untuk di-link/copy. Folder akan dibuat otomatis oleh Path.mkdir()
        if item.is_file():
            # Path relatif dari folder 'dot_files'
            rel_path = item.relative_to(dot_dir)
            
            # Kalau jalurnya ada di 'nvim/' (bukan '.config/nvim/'), abaikan karena ganda
            if rel_path.parts[0] == 'nvim':
                continue
                
            dest_path = home_dir / rel_path
            
            # Khusus untuk wallpaper, pastikan masuk ke folder yang sesuai
            install_item(item, dest_path, use_copy=args.copy)
            
    print("---------------------------------")
    print("[✔] Instalasi selesai!")
    print("[*] Jalankan 'source ~/.zshrc' jika shell saat ini adalah Zsh.")

if __name__ == "__main__":
    main()
