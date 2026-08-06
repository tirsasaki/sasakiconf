# My personal dotfiles

## Contents

- `dot_files/.zshrc` — Zsh config (Oh My Zsh + Powerlevel10k)
- `dot_files/.config/nvim/` — Neovim config (lazy.nvim, Dracula theme)
- `dot_files/.config/kitty/` — Kitty terminal config (One Dark theme)
- `dot_files/.config/alacritty/` — Alacritty terminal config
- `dot_files/.config/ghostty/` — Ghostty terminal config (Dracula theme)
- `dot_files/.config/fastfetch/` — Fastfetch config
- `dot_files/.wallpaper/` — Wallpapers

Note: `dot_files/nvim/` and `dot_files/.config/nvim/` are duplicates.

## Usage

```
git clone https://github.com/tirsasaki/sasakiconf.git
cd sasakiconf

cp dot_files/.zshrc ~/.zshrc
cp -r dot_files/.config/nvim ~/.config/nvim
cp -r dot_files/.config/kitty ~/.config/kitty
cp -r dot_files/.config/alacritty ~/.config/alacritty
cp -r dot_files/.config/ghostty ~/.config/ghostty
cp -r dot_files/.config/fastfetch ~/.config/fastfetch
```

Then `source ~/.zshrc` and open Neovim once to let lazy.nvim install plugins.

## To check before reusing

- Fonts used: SauceCodePro, JetBrains Mono
- `kitty.conf` uses the One Dark color scheme — pastikan file tema One Dark (mis. `one-dark.conf`) sudah ada di folder kitty kamu, atau ganti baris `include` di `kitty.conf` sesuai lokasi file tema di sistemmu.
- `fastfetch/config.jsonc` references a custom logo path

## License

MIT
