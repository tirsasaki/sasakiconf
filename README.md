# Dotfiles

Personal configuration files for my development environment — shell, editor, terminal emulators, and system utilities.

## Table of Contents

- [Contents](#contents)
- [Usage](#usage)
- [Before Reusing](#before-reusing)
- [License](#license)

## Contents

| Path | Description |
|---|---|
| `dot_files/.zshrc` | Zsh config (Oh My Zsh + Powerlevel10k) |
| `dot_files/.config/starship.toml` | Starship prompt config |
| `dot_files/.config/nvim/` | Neovim config (lazy.nvim, Dracula theme) |
| `dot_files/.config/kitty/` | Kitty terminal config (One Dark theme) |
| `dot_files/.config/alacritty/` | Alacritty terminal config |
| `dot_files/.config/ghostty/` | Ghostty terminal config (One Dark theme) |
| `dot_files/.config/fastfetch/` | Fastfetch config |
| `dot_files/.config/yazi/` | Yazi file manager config (Catppuccin Mocha theme) |
| `dot_files/.wallpaper/` | Wallpapers |

> **Note:** `dot_files/nvim/` and `dot_files/.config/nvim/` are duplicates.

## Usage

Clone the repository:

```bash
git clone https://github.com/tirsasaki/sasakiconf.git
cd sasakiconf
```

Copy the configs you need:

```bash
cp dot_files/.zshrc ~/.zshrc
cp -r dot_files/.config/nvim ~/.config/nvim
cp -r dot_files/.config/kitty ~/.config/kitty
cp -r dot_files/.config/alacritty ~/.config/alacritty
cp -r dot_files/.config/ghostty ~/.config/ghostty
cp -r dot_files/.config/fastfetch ~/.config/fastfetch
cp -r dot_files/.config/yazi ~/.config/yazi
cp dot_files/.config/starship.toml ~/.config/starship.toml
```

Reload your shell and finish setup:

```bash
source ~/.zshrc
```

Then open Neovim once to let `lazy.nvim` install plugins.

## Before Reusing

Double-check these before applying the configs on a new machine:

- **Fonts**: SauceCodePro, JetBrains Mono — install both beforehand.
- **Kitty**: uses the One Dark color scheme. Make sure the theme file is present in your Kitty config folder, or update the `include` line in `kitty.conf` to match the theme file's location on your system.
- **Fastfetch**: `config.jsonc` references a custom logo path — update it to a valid path on your machine.

## License

[MIT](./LICENSE)
